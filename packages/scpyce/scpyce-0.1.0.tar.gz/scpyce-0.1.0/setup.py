# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='scpyce',
    version='0.1.0',
    description='SQL based finite element solver in Python',
    long_description=readme,
    author='Nicolo Bencini',
    author_email='nicbencini@gmail.com',
    url='https://https://github.com//nicbencini//scpyce',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    
)