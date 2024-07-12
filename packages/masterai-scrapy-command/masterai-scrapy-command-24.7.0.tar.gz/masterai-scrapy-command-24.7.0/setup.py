# -*- coding: utf-8 -*-
from setuptools import setup

def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


packages = ['masterai_scrapy_command']

package_data = {'': ['*']}

install_requires = read_requirements('requirements.txt')


entry_points = {
    'scrapy.commands': [
        'report = masterai_scrapy_command.report:ReportCommand'
    ]
}

setup_kwargs = {
    'name': 'masterai-scrapy-command',
    'version': '24.7.0',
    'description': 'A package providing some command for scrapy CLI',
    'author': 'welwel',
    'author_email': 'walwel@yeah.net',
    'maintainer': None,
    'maintainer_email': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}

setup(**setup_kwargs)