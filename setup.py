from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='torcheck',
    version='0.1',
    description='Torch implementation for STL monitoring',
    license="GPLv3",
    long_description=long_description,
    url="https://github.com/ailab-units/Feat2Vec",
    install_requires=['torch'],  # external packages as dependencies
)