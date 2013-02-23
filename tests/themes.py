# FlowUI themes unit tests
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

from unittest import TestCase

from flowui import AnsiTerminal
from flowui.terminals import SysTerminal
from flowui.themes import Solarized
from flowui.themes import Zenburn


class ThemeTest(object):
    def setUp(self, terminal, theme):
        self._theme = theme
        self._terminal = AnsiTerminal(terminal, theme)

    def tearDown(self):
        self._terminal.reset()

    def test_faces(self):
        self._terminal.reset()
        for name in self._theme.faces.keys():
            self._terminal.write('\n\t%%(%s)s[%s]' % (name, name))

        self._terminal.reset()
        self._terminal.write('\n')


class SolarizedTest(ThemeTest, TestCase):
    def setUp(self, terminal=None, theme=None):
        super(SolarizedTest, self).setUp(SysTerminal(), Solarized())


class ZenburnTest(ThemeTest, TestCase):
    def setUp(self, terminal=None, theme=None):
        super(ZenburnTest, self).setUp(SysTerminal(), Zenburn())
