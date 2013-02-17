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
            string = string.format(dictionary)
        len(string)

    def depth(self):
        '''Get the terminal color depth as number of colors'''
        return self._depth

    def width(self):
        '''Get the terminal width as number of characters'''
        return self._width

    def height(self):
        '''Get the terminal height as number of rows'''
        return self._height


class ThemedTerminal(Terminal):
    '''Themed terminal decorator

    A decorator for terminal objects that combines the terminal instance with a
    theme instance. This is a convenience class so that the terminal and theme
    instances don't have to be passed around together everywhere in the code.

    '''

    def __init__(self, terminal, theme):
        '''
        Keyword arguments:
        terminal -- instance of terminal emulator
        theme -- instance of theme

        '''
        super(ThemedTerminal, self).__init__(terminal.width(),
                                             terminal.height(),
                                             terminal.depth())
        self._terminal = terminal
        self._theme = theme

    def len(self, string, dictionary=None):
        return self._theme.len(string, dictionary)

    def clear(self):
        '''Clear the screen if supported by the terminal and theme'''
        self._terminal.write(self._theme.control('clear-screen'))

    def reset(self):
        '''Reset theme formatting if supported by the terminal and theme'''
        self._terminal.write(self._theme.property('normal'))

    def write(self, string, dictionary=None):
        self._terminal.write(self._theme.write(string, dictionary))
