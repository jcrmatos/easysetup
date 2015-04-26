#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009-2015 Joao Carlos Roseta Matos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Application basic information."""

# Python 3 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# sometimes py2exe requires the following import to be commented
#from __future__ import unicode_literals

#import builtins  # Python 3 compatibility
import datetime as dt
#import future  # Python 3 compatibility
#import io  # Python 3 compatibility


APP_NAME = 'easysetup'
APP_VERSION = '0.0.9'
APP_LICENSE = 'GNU General Public License v2 or later (GPLv2+)'
APP_URL = 'https://github.com/jcrmatos/easysetup'
APP_AUTHOR = 'Joao Carlos Roseta Matos'
APP_EMAIL = 'jcrmatos@gmail.com'
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'Natural Language :: English',
               'License :: OSI Approved ::' + ' ' + APP_LICENSE,
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Topic :: Software Development :: Build Tools',
              ]
APP_KEYWORDS = 'easy setup setuptools'

COPYRIGHT = 'Copyright 2009-' + str(dt.date.today().year) + ' '  + APP_AUTHOR

APP_TYPE = 'application'  # it can be application or module

README_FILE = 'README.rst'
REQUIREMENTS_FILE = 'requirements.txt'
