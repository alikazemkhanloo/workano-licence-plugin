#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='workano-licence-plugin',
    version='1.0',
    description='workano licence plugin',
    author='workano team',
    author_email='info@workano.com',
    packages=find_packages(),
    url='https://workano.com',
    include_package_data=True,
    package_data={
        'workano_confd_licence': ['api.yml'],
    },

    entry_points={
        'wazo_confd.plugins': [
            'licence = workano_confd_licence.plugin:Plugin'
        ]
    }
)
