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

import itertools


__all__ = ['Normal', 'Comment', 'Constant', 'Identifier', 'Statement',
           'Define', 'Type', 'Special', 'Underlined', 'Error', 'Attention',
           'Header', 'Regular', 'Italic', 'Bold', 'Underline', 'depth', 'fg',
           'bg', 'Theme']


class _Face(tuple):
    def __init__(self, *_):
        super(_Face, self).__init__()
        self.subtypes = set()

    def __getattr__(self, value):
        if not value or not value[0].isupper():
            return tuple.__getattribute__(self, value)

        face = _Face(self + (value,))
        setattr(self, value, face)
        self.subtypes.add(face)
        return face

    def __repr__(self):
        return 'face' + (self and '-' or '') + '-'.join(self).lower()


Face = _Face()
Normal = Face.Normal
Comment = Face.Comment
Constant = Face.Constant
Identifier = Face.Identifier
Statement = Face.Statement
Define = Face.Define
Type = Face.Type
Special = Face.Special
Underlined = Face.Underlined
Error = Face.Error
Attention = Face.Attention
Header = Face.Header


class _Typeface(tuple):
    # pylint: disable=W0231
    def __init__(self, *_):
        self.subtypes = set()

    def __getattr__(self, value):
        if not value or not value[0].isupper():
            return tuple.__getattribute__(self, value)

        tp = _Typeface(self + (value,))
        setattr(self, value, tp)
        self.subtypes.add(tp)
        return tp

    def __repr__(self):
        return 'typeface' + (self and '-' or '') + '-'.join(self).lower()


Typeface = _Typeface()
Regular = Typeface.Regular
Italic = Typeface.Italic
Bold = Typeface.Bold
Underline = Typeface.Underline


class depth(int):
    pass


class fg(int):
    pass


class bg(int):
    pass


class ThemeMeta(type):
    def _process_definition(cls, fdef):
        if type(fdef) is _Typeface:
            return (Typeface, fdef)

        elif type(fdef) is fg:
            return (fg, fdef)

        elif type(fdef) is bg:
            return (bg, fdef)

        else:
            assert False, 'unknown definition %r' % fdef

    def _process_color(cls, facesdefs):
        face_attr = {}
        for fdef in facesdefs:
            attr = cls._process_definition(fdef)
            face_attr[attr[0]] = attr[1]

        return face_attr

    def _process_face(cls, facesdefs, face):
        face_colors = {}
        for colors, fdefs in facesdefs[face].items():
            assert type(colors) is depth
            face_colors[colors] = cls._process_color(fdefs)

        return face_colors

    def process_faces(cls, name, facesdefs=None):
        faces = {}
        facesdefs = facesdefs or cls.faces[name]
        for face in facesdefs.keys():
            if type(face) is _Face:
                faces[face] = cls._process_face(facesdefs, face)

            else:
                assert False, 'unknown face type %r' % face

        return faces

    def get_facesdefs(cls):
        faces = {}
        for c in itertools.chain((cls,), cls.__mro__):
            fcs = c.__dict__.get('faces', {})
            for name, components in fcs.items():
                current = faces.get(name)
                if current is None:
                    faces[name] = components

        return faces

    def __call__(cls, *args, **kwds):
        if '_faces' not in cls.__dict__ or not cls.__dict__['_faces']:
            # pylint: disable=W0201
            cls._faces = cls.process_faces('', cls.get_facesdefs())

        return type.__call__(cls, *args, **kwds)


class Theme(object):
    '''Base class for all FlowUI themes

    The Theme class provides all the basic functionality required to make a
    FlowUI theme work together with a Terminal instance. The purpose is to
    abstract as much as possible of the functionality so that the Theme only
    has to define the colors relevant to it.

    Controls:
    clear-screen -- Clear the screen and reset the cursor

    Typefaces:
    regular
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
    __metaclass__ = ThemeMeta

    name = None
    colors = []
    faces = {}

    def face(self, f, depth_):
        '''Get the specified face'''
        # pylint: disable=E1101
        assert f in self._faces, 'face %r not found' % f
        face = self._faces[f]
        assert depth_ in face, 'depth %r not available in %f' % (depth_, face)
        return face[depth_]
