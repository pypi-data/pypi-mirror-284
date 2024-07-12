"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

from setuptools import setup, find_packages

setup(
    name='TuiToy',
    version='0.0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'TuiToy = tuitoy.tuitoy:main',
            ],
    },
    install_requires=[
        'windows-curses',
    ],
)

"""
Copyright (C) 2023 Austin Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
