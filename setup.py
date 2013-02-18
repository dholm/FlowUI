#!/usr/bin/env python

from distutils.core import setup

from flowui import __version__


setup(name='FlowUI',
      packages=['flowui', 'flowui.widgets', 'flowui.themes',
                'flowui.terminals'],
      version=__version__,
      description='A flow-based data presentation interface',
      author='David Holm',
      author_email='dholmster@gmail.com',
      url='http://github.com/dholm/FlowUI/',
      download_url=('https://github.com/dholm/FlowUI/archive/%s.zip' %
                    __version__),
      license='BSD',
      keywords=['ui', 'widget', 'text', 'console', 'terminal', 'themes'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Software Development :: User Interfaces',
                   'Topic :: Software Development :: Widget Sets'],
      long_description='''FlowUI is a simple presentation toolkit for
      text-based displays where it is not possible to move the cursor
      backwards. All widgets are designed so that they are rendered one
      character at a time and assuming the cursor is moved forward one
      character each time.

      One typical use case for FlowUI is when having to present data through
      the terminal interface of a third party application. In these cases it
      might not be feasible to use ncurses or similar frameworks as they may
      disrupt the applications normal output.''')
