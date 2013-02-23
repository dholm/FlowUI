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

from flowui.theme import *


class Zenburn(Theme):
    '''Zenburn theme

    This theme is based on Zenburn by Jani Nurminen which is a low-contrast
    color scheme designed to be easy on the eyes.

    http://slinky.imukuppi.org/zenburnpage/

    '''
    name = 'Zenburn'

    faces = {
        Normal: {depth(256): [Regular, fg(188), bg(237)]},
        Comment: {depth(256): [Regular, fg(108), bg(237)]},
        Constant: {depth(256): [Bold, fg(181), bg(237)]},
        Identifier: {depth(256): [Regular, fg(223), bg(237)]},
        Statement: {depth(256): [Regular, fg(187), bg(234)]},
        Define: {depth(256): [Bold, fg(223), bg(237)]},
        Type: {depth(256): [Bold, fg(187), bg(237)]},
        Special: {depth(256): [Regular, fg(181), bg(237)]},
        Underlined: {depth(256): [Bold, fg(188), bg(234)]},
        Error: {depth(256): [Bold, fg(115), bg(236)]},
        Attention: {depth(256): [Bold, fg(108), bg(234)]},
        Header: {depth(256): [Regular, fg(108), bg(235)]}}
