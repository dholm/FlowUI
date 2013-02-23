# FlowUI Solarized theme
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


class Solarized(Theme):
    '''Solarized theme

    This theme is based on Ethan Schoonover's excellent theme as described on
    his page: http://ethanschoonover.com/solarized

    '''
    name = 'Solarized'

    pal = {'base03': {8: (Bold, 0), 16: 8, 256: 234},
           'base02': {8: (Regular, 0), 16: 0, 256: 235},
           'base01': {8: (Bold, 2), 16: 10, 256: 240},
           'base00': {8: (Bold, 3), 16: 11, 256: 241},
           'base0': {8: (Bold, 4), 16: 12, 256: 244},
           'base1': {8: (Bold, 6), 16: 14, 256: 245},
           'base2': {8: (Regular, 7), 16: 7, 256: 254},
           'base3': {8: (Bold, 7), 16: 15, 256: 230},
           'yellow': {8: (Regular, 3), 16: 3, 256: 136},
           'orange': {8: (Bold, 1), 16: 9, 256: 166},
           'red': {8: (Regular, 1), 16: 1, 256: 160},
           'magenta': {8: (Regular, 5), 16: 5, 256: 125},
           'violet': {8: (Bold, 5), 16: 13, 256: 61},
           'blue': {8: (Regular, 4), 16: 4, 256: 33},
           'cyan': {8: (Regular, 6), 16: 6, 256: 37},
           'green': {8: (Regular, 2), 16: 2, 256: 64}}

    faces = {
        Normal: {depth(8): [pal['base0'][8][0],
                            fg(pal['base0'][8][1]),
                            bg(pal['base03'][8][1])],

                 depth(16): [Regular,
                             fg(pal['base0'][16]),
                             bg(pal['base03'][16])],

                 depth(256): [Regular,
                              fg(pal['base0'][256]),
                              bg(pal['base03'][256])]},

        Comment: {depth(8): [pal['base01'][8][0],
                             fg(pal['base01'][8][1]),
                             bg(pal['base03'][8][1])],

                  depth(16): [Italic,
                              fg(pal['base01'][16]),
                              bg(pal['base03'][16])],

                  depth(256): [Italic,
                               fg(pal['base01'][256]),
                               bg(pal['base03'][256])]},

        Constant: {depth(8): [pal['cyan'][8][0],
                              fg(pal['cyan'][8][1]),
                              bg(pal['base03'][8][1])],

                   depth(16): [Regular,
                               fg(pal['cyan'][16]),
                               bg(pal['base03'][16])],

                   depth(256): [Regular,
                                fg(pal['cyan'][256]),
                                bg(pal['base03'][256])]},

        Identifier: {depth(8): [pal['blue'][8][0],
                                fg(pal['blue'][8][1]),
                                bg(pal['base03'][8][1])],

                     depth(16): [Regular,
                                 fg(pal['blue'][16]),
                                 bg(pal['base03'][16])],

                     depth(256): [Regular,
                                  fg(pal['blue'][256]),
                                  bg(pal['base03'][256])]},

        Statement: {depth(8): [pal['green'][8][0],
                               fg(pal['green'][8][1]),
                               bg(pal['base03'][8][1])],

                    depth(16): [Regular,
                                fg(pal['green'][16]),
                                bg(pal['base03'][16])],

                    depth(256): [Regular,
                                 fg(pal['green'][256]),
                                 bg(pal['base03'][256])]},

        Define: {depth(8): [pal['orange'][8][0],
                            fg(pal['orange'][8][1]),
                            bg(pal['base03'][8][1])],

                 depth(16): [Regular,
                             fg(pal['orange'][16]),
                             bg(pal['base03'][16])],

                 depth(256): [Regular,
                              fg(pal['orange'][256]),
                              bg(pal['base03'][256])]},

        Type: {depth(8): [pal['yellow'][8][0],
                          fg(pal['yellow'][8][1]),
                          bg(pal['base03'][8][1])],

               depth(16): [Regular,
                           fg(pal['yellow'][16]),
                           bg(pal['base03'][16])],

               depth(256): [Regular,
                            fg(pal['yellow'][256]),
                            bg(pal['base03'][256])]},

        Special: {depth(8): [pal['red'][8][0],
                             fg(pal['red'][8][1]),
                             bg(pal['base03'][8][1])],

                  depth(16): [Regular,
                              fg(pal['red'][16]),
                              bg(pal['base03'][16])],

                  depth(256): [Regular,
                               fg(pal['red'][256]),
                               bg(pal['base03'][256])]},

        Underlined: {depth(8): [pal['violet'][8][0],
                                fg(pal['violet'][8][1]),
                                bg(pal['base03'][8][1])],

                     depth(16): [Regular,
                                 fg(pal['violet'][16]),
                                 bg(pal['base03'][16])],

                     depth(256): [Regular,
                                  fg(pal['violet'][256]),
                                  bg(pal['base03'][256])]},

        Error: {depth(8): [pal['red'][8][0],
                           fg(pal['red'][8][1]),
                           bg(pal['base03'][8][1])],

                depth(16): [Regular,
                            fg(pal['red'][16]),
                            bg(pal['base03'][16])],

                depth(256): [Regular,
                             fg(pal['red'][256]),
                             bg(pal['base03'][256])]},

        Attention: {depth(8): [pal['magenta'][8][0],
                               fg(pal['magenta'][8][1]),
                               bg(pal['base03'][8][1])],

                    depth(16): [Regular,
                                fg(pal['magenta'][16]),
                                bg(pal['base03'][16])],

                    depth(256): [Regular,
                                 fg(pal['magenta'][256]),
                                 bg(pal['base03'][256])]},

        Header: {depth(8): [pal['base1'][8][0],
                            fg(pal['base1'][8][1]),
                            bg(pal['base02'][8][1])],

                 depth(16): [Regular,
                             fg(pal['base1'][16]),
                             bg(pal['base02'][16])],

                 depth(256): [Regular,
                              fg(pal['base1'][256]),
                              bg(pal['base02'][256])]}}
