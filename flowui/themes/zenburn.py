# FlowUI Zenburn theme
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

from flowui.theme import Theme


class Zenburn(Theme):
    '''Zenburn theme

    This theme is based on Zenburn by Jani Nurminen which is a low-contrast
    color scheme designed to be easy on the eyes.

    http://slinky.imukuppi.org/zenburnpage/

    '''
    def __init__(self, depth):
        default_bg = 237
        super(Zenburn, self).__init__(self._color(depth, 188, default_bg))

        self._add_face('comment', self._color(depth, 108, default_bg))
        self._add_face('constant', self._color(depth, 181, default_bg, 'bold'))
        self._add_face('identifier', self._color(depth, 223, default_bg))
        self._add_face('statement', self._color(depth, 187, 234))
        self._add_face('preproc', self._color(depth, 223, default_bg, 'bold'))
        self._add_face('type', self._color(depth, 187, default_bg))
        self._add_face('special', self._color(depth, 181, default_bg))
        self._add_face('underlined', self._color(depth, 188, 234, 'bold'))
        self._add_face('error', self._color(depth, 115, 236, 'bold'))
        self._add_face('todo', self._color(depth, 108, 234, 'bold'))

        self._add_face('header', self._color(depth, 108, 235))

    @classmethod
    def name(cls):
        return 'zenburn'
