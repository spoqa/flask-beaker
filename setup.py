"""
Flask-Beaker
------------

Flask extension for Beaker
"""
from setuptools import setup

setup(name='Flask-Beaker',
      version='0.1',
      description='Flask extension for Beaker',
      long_description=__doc__,
      author='longfin',
      author_email='longfin@spoqa.com',
      url='http://github.com/spoqa/flask-beaker',
      packages=['flaskext'],
      test_suite='test_beaker',
      install_requires=[
        'setuptools',
        'Flask>=0.8',
        'flask-testing',
        'Beaker'
        ],
      )
