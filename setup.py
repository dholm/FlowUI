#!/usr/bin/env python

from distutils.core import setup

from flowui import __version__


setup(name='FlowUI',
      packages=['flowui', 'flowui.widgets', 'flowui.themes',
                'flowui.terminals'],
      version=__version__,
      description='A flow-based data presentation framework for terminals',
      author='David Holm',
      author_email='dholmster@gmail.com',
      url='http://github.com/dholm/FlowUI/',
      download_url=('https://github.com/dholm/FlowUI/archive/%s.zip' %
                    __version__),
      license='BSD',
      keywords=['ui', 'widget', 'text', 'console', 'terminal', 'themes'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Widget Sets'],
      long_description='''FlowUI is a simple presentation toolkit for
      text-based displays. What makes it different from other, similar user
      interfaces, is that it has been designed so that it can easily be
      embedded into a third-party application's interface without disrupting
      it.

      All widgets in FlowUI are designed so that they are rendered one
      character at a time and assuming the cursor is moved forward by one
      character so that the cursor never has to be repositioned.''')
