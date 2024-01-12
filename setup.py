from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(name='findlang',
      version=version,
      description="findlang is a standalone Language Identification based on (LangID) tool.",
      long_description="""\
      findlang is a standalone Language Identification based on (LangID) tool. It is a Python 3 port of the original langid.py by Marco Lui and Tim Baldwin.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='language detection',
      author='Bayangmbe Mounmo',
      author_email='bayangp0@gmail.com',
      url='https://github.com/deepfile/findlang',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'numpy'
      ],
      entry_points= {
        'console_scripts': [
          'findlang = findlang.findlang:main',
        ],
      },
      )
