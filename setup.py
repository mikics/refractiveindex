import sys

from setuptools import setup, find_namespace_packages

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
    description='A Python wrapper for the refractiveindex.info database',
    long_description='',
    packages=find_namespace_packages(where="./"),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    package_data={"refractiveindex.ridb.database.data.*.*": ["*.yml"]},)