# FlowUI terminal interface
#
# Copyright (c) 2012-2013, David Holm <dholmster@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author of FlowUI nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL DAVID HOLM BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import abc
import re

import flowui.theme


class Terminal(object):
    '''Abstract base class for terminals

    Provides the base class for any terminal emulator used as an output device
    with FlowUI.

    '''

    __metaclass__ = abc.ABCMeta

    DEFAULT_WIDTH = 80
    DEFAULT_HEIGHT = 25
    DEFAULT_DEPTH = 8

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT,
                 depth=DEFAULT_DEPTH):
        '''
        Keyword arguments:
        width -- visible width of terminal in characters
        height -- visible height of terminal in rows
        depth -- depth of terminal in number of colors

        '''
        self._width = width
        self._height = height
        self._depth = depth

    @abc.abstractmethod
    def reset(self):
        '''Reset terminal formatting back to normal output'''
        raise NotImplementedError()

    @abc.abstractmethod
    def write(self, string, dictionary=None):
        '''Write output to the terminal

        Writes the specified string formatted using the optional dictionary on
        the terminal device.

        Keyword arguments:
        string -- string containing optional formatting
        dictionary -- optional dictionary used together with string formatting

        '''
        raise NotImplementedError()

    def len(self, string, dictionary=None):
        '''Calculate the length of a string

        Calculates the length of a string, after formatting, in number of
        characters when displayed on the terminal.

        '''
        if dictionary is not None:
            string = string % dictionary
        return len(string)

    def depth(self):
        '''Get the terminal color depth as number of colors'''
        return self._depth

    def width(self):
        '''Get the terminal width as number of characters'''
        return self._width

    def height(self):
        '''Get the terminal height as number of rows'''
        return self._height


class AnsiTerminal(Terminal):
    '''Themed terminal decorator

    A decorator for terminal objects that combines the terminal instance with a
    theme instance. This is a convenience class so that the terminal and theme
    instances don't have to be passed around together everywhere in the code.

    '''
    _ansi_escape_expression = re.compile((r'\x1B\[((\d+|"[^"]*")'
                                          r'(;(\d+|"[^"]*"))*)?'
                                          r'[A-Za-z]'))

    _properties = {flowui.theme.Regular: 0,
                   flowui.theme.Bold: 1,
                   flowui.theme.Italic: 2,
                   flowui.theme.Underline: 4}

    def _sgr(self, *args):
        return ''.join(['\x1b[', ';'.join([str(x) for x in args]), 'm'])

    def reset(self):
        self._terminal.write(self._sgr(0))

    def _fmt_depth(self, components, depth):
        tf = self._properties[components[flowui.theme.Typeface]]
        fg = components[flowui.theme.fg]
        bg = components[flowui.theme.bg]
        if 16 <= depth:
            return self._sgr(tf, 38, 5, fg, 48, 5, bg)
        else:
            return self._sgr(tf, (30 + fg), (40 + bg))

    def _faces_dict(self, theme_, depth):
        d = {}
        for f in theme_.faces.keys():
            face = theme_.face(f, depth)
            d[repr(f)] = self._fmt_depth(face, depth)
        return d

    def __init__(self, terminal, theme_):
        '''
        Keyword arguments:
        terminal -- instance of terminal emulator
        theme_ -- instance of theme

        '''
        super(AnsiTerminal, self).__init__(terminal.width(),
                                           terminal.height(),
                                           terminal.depth())
        self._faces = self._faces_dict(theme_, terminal.depth())
        self._terminal = terminal

    def _fmt_string(self, string, dictionary=None):
        d = self._faces
        if dictionary:
            d.update(dictionary)
        return string % d

    def len(self, string, dictionary=None):
        return len(self._fmt_string(string, dictionary))

    def write(self, string, dictionary=None):
        '''Apply theme formatting and return the resulting string'''
        self._terminal.write(self._fmt_string(string, dictionary))
