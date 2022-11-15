import sys

from setuptools import setup

if sys.version_info < (3, 8):
    print("Python 3.8 or higher required, please upgrade.")
    sys.exit(1)

VERSION = "2022.1.0"

REQUIREMENTS = [
    "numpy",
    "scipy",
    "pyyaml",
]


setup(
    name='refractiveindex', version=VERSION,
    author='Michele Castriotta',
    description='A Python3 + SQLite wrapper for the refractiveindex database',
    long_description='',
    packages=["refractiveindex"],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    package_data={'refractiveindex': ['data.txt', 'refractiveindex.info-database/database/data/*/*/*.yml']},)
