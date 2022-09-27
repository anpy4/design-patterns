from setuptools import setup, find_packages

setup(
   name='design-patterns',
   version='1.0.0',
   description='This module implements design patterns frequently used in object-oriented programming',
   author='André Schiefer',
   author_email='cgndre@yahoo.com',
   packages=find_packages(),
   requires=['pillow'],
   tests_requires=['pytest']
)