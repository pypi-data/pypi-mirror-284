#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='freecell_solver',
      version='0.6.0',
      description='Freecell Solver bindings',
      keywords='freecell_solver',
      author='Shlomi Fish',
      author_email='shlomif@cpan.org',
      url='https://github.com/shlomif/freecell_solver',
      license='3-clause BSD',
      long_description=io.open(
          './docs/README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                   'Programming Language :: Python :: 3.11',
                   ],
      packages=find_packages(exclude=('tests', 'tests.*')),
      include_package_data=True,
      install_requires=['cffi'],
      entry_points={
          'console_scripts': [
              'freecell_solver = freecell_solver.__main__:main',
          ]
      },
      )
