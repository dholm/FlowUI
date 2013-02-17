# FlowUI theme support
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

import re


class Theme(object):
    '''Base class for all FlowUI themes

    The Theme class provides all the basic functionality required to make a
    FlowUI theme work together with a Terminal instance. The purpose is to
    abstract as much as possible of the functionality so that the Theme only
    has to define the colors relevant to it.

    Controls:
    clear-screen -- Clear the screen and reset the cursor

    Properties:
    normal -- normal face
    bold
    italic
    underline

    Faces:
    face-normal
    face-comment
    face-constant   -- string, char, number etc constants
    face-identifier -- variable/function name
    face-statement  -- statements (if, else, for etc)
    face-define     -- definitions (i.e. #define X)
    face-type       -- types (integer, static, struct etc)
    face-special    -- special symbols or characters
    face-underlined -- text that stands out (i.e. links)
    face-error
    face-attention  -- anything that needs extra attention
    face-header     -- section headers etc

    '''
    _ansi_escape_expression = re.compile((r'\x1B\[((\d+|"[^"]*")'
                                          r'(;(\d+|"[^"]*"))*)?'
                                          r'[A-Za-z]'))

    _controls = {'clear-screen': '\x1b[2J'}
    _property_fmt = '\x1b[%dm'
    _properties = {'normal': 0,
                   'bold': 1,
                   'italic': 2,
                   'underline': 4}
    _colors_fmt = {8: '\x1b[%d;3%1d;4%1dm',
                   16: '\x1b[%d;38;5;%d;48;5;%dm',
                   256: '\x1b[%d;38;5;%d;48;5;%dm'}

    def _add_face(self, face, color, prop='normal'):
        if prop in self._properties:
            prop = self._properties[prop]

        self._faces['face-' + face] = '%s%s' % (self._property_fmt % prop,
                                                color)

    def _color(self, depth, fg, bg, prop='normal'):
        if prop in self._properties:
            prop = self._properties[prop]
        return (self._colors_fmt.get(depth, 8) %
                (prop, fg, bg))

    def __init__(self, default_color):
        '''
        Keyword arguments:
        default_color -- the default color to fall back to

        '''
        self._default_color = default_color

        self._faces = {}
        self._add_face('normal', default_color)
        self._faces['face-reset'] = self.property('normal')

    def control(self, name):
        '''Get the control sequence of the specified name'''
        assert name in self._controls
        return self._controls[name]

    def property(self, name):
        '''Get the property sequence of the specified name'''
        assert name in self._properties
        return (self._property_fmt % self._properties[name])

    def faces(self):
        '''Get the dictionary of all defined faces'''
        return self._faces

    def face(self, name):
        '''Get the face sequence of the specified name'''
        assert ('face-%s' % name) in self._faces
        return self._faces.get('face-%s' % name, self._faces['face-normal'])

    def _filter_string(self, string):
        if not len(string):
            return string

        string = string.expandtabs()
        if string[-1] == '\n':
            string = string[:-1] + ('%s\n' % self.property('normal'))
        return string

    def len(self, string, format_dictionary=None):
        '''Calculate the length of a string

        Calculates the length of a string, after formatting, in number of
        characters, including eventual theme formatting, when displayed on the
        terminal.

        '''
        d = self._faces
        if format_dictionary:
            d.update(format_dictionary)

        filtered = self._filter_string(string)
        return len(self._ansi_escape_expression.sub('', (filtered % d)))

    def write(self, string, format_dictionary=None):
        '''Apply theme formatting and return the resulting string'''
        d = self._faces
        if format_dictionary:
            d.update(format_dictionary)

        filtered = self._filter_string(string)
        return '%s%s' % (self.face('normal'), (filtered % d))
