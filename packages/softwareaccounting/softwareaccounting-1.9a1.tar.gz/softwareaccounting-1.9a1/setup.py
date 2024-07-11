"""
SAMS Software accounting
Copyright (C) 2018-2021  Swedish National Infrastructure for Computing (SNIC)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

from sams import __version__


setup(
    name="softwareaccounting",
    version=__version__,
    description="SAMS Software Accounting",
    packages=[
        "sams",
        "sams.aggregator",
        "sams.loader",
        "sams.output",
        "sams.pidfinder",
        "sams.sampler",
        "sams.backend",
        "sams.software",
        "sams.xmlwriter",
        "sams.listener",
    ],
    scripts=[
        "sams-aggregator.py",
        "sams-collector.py",
        "sams-post-receiver.py",
        "sams-software-extractor.py",
        "sams-software-updater.py",
        "extras/sgas-sa-registrant/bin/sgas-sa-registrant",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httplib2",
        "peewee",
        "PyYAML",
    ],
    extras_require={
        "sams-post-receiver": ["Flask"],
    },
)
