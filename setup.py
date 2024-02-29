from setuptools import setup

setup(
    name='pysplit',
    version='0.1',
    py_modules=['pysplit'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        pysplit=pysplit:main
    ''',
    options={
        'build_scripts': {
            'executable': '/usr/bin/env python'
        }
    }
)