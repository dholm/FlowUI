#!/usr/bin/env python

from distutils.core import setup

from flowui import __version__


setup(name='FlowUI',
      version=__version__,
      description='A flow-based textual presentation interface',
      author='David Holm',
      author_email='dholmster@gmail.com',
      url='http://github.com/dholm/FlowUI/',
      packages=['flowui', 'flowui/widgets', 'flowui/themes',
                'flowui/terminals'],
      platforms='unix-like',
      keywords='ui widget text console terminal themes',
      license='BSD')
