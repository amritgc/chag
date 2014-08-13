#!/usr/bin/env python

from setuptools import setup, find_packages


readme = open('README.rst').read()

requirements = [
    'click==3.0',
]

test_requirements = [
    'pytest'
]

setup(
    name='chag',
    version='0.3.0',
    description="Parses changelog files and helps with changelog workflows",
    long_description=readme,
    author='Michael Dowling',
    author_email='mtdowling@gmail.com',
    url="https://github.com/mtdowling/chag",
    packages=[
        'chag'
    ],
    package_dir={'chag': 'chag'},
    install_requires=requirements,
    license='MIT',
    keywords="changelog",
    py_modules=['chag'],
    entry_points="""
        [console_scripts]
        chag=chag.main:main
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT'
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)