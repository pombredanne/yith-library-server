# Yith Library Server is a password storage server.
# Copyright (C) 2012 Yaco Sistemas
# Copyright (C) 2012 Alejandro Blanco Escudero <alejandro.b.e@gmail.com>
# Copyright (C) 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# This file is part of Yith Library Server.
#
# Yith Library Server is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Yith Library Server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Yith Library Server.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'deform==0.9.5',
    'pymongo==2.3',
    'pyramid==1.3.4',
    'pyramid_beaker==0.7',
    'pyramid_debugtoolbar==1.0.2',
    'pyramid_mailer==0.9',
    'pyramid_tm==0.5',
    'requests==0.14.0',
    'waitress==0.8.1',
    ]

if sys.version_info[0] < 3:
    # Babel does not work with Python 3
    requires.append('Babel==0.9.6')

test_requires = [
    'WebTest',
    'mock',
    'nose',
    'coverage',
    ]

setup(name='yith-library-server',
      version='0.0',
      description='yith-library-server',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pyramid",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires + test_requires,
      test_suite="yithlibraryserver",
      entry_points = """\
      [paste.app_factory]
      main = yithlibraryserver:main
      [console_scripts]
      yith_usage_report = yithlibraryserver.scripts.reports:usage
      yith_apps_report = yithlibraryserver.scripts.reports:applications
      """,
      )

