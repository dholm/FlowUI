# FlowUI containers
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

from flowui.widget import Widget


class Section(Widget):
    '''Section widget

    This widget provides a section into which other widgets can be grouped. It
    supports an optional headline which can be used to describe its contents.

    '''
    _name = None
    _components = None

    def __init__(self, name=None):
        '''
        Keyword arguments:
        name -- optional name to use in section headline

        '''
        self._name = name
        self._components = []

    def _draw_header(self, terminal, width):
        title = ''
        if self._name:
            title = ('[%s]' % self._name)
        assert terminal.len(title) <= width

        header = ['%(face-header)s']
        dashes = int(width - len(title))
        header += ['-' for _ in range(dashes)]
        header += [title, '\n']
        terminal.write(''.join(header))

    def add_component(self, component):
        '''Adds the specified component to the section'''
        self._components.append(component)

    def draw(self, terminal, width):
        width -= (width / 20)
        self._draw_header(terminal, width)

        for component in self._components:
            component.draw(terminal, width)
