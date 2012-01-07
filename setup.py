"""
Flask-Beaker
------------

Flask extension for Beaker
"""
from setuptools import setup

setup(name='Flask-Beaker',
      version='0.2',
      description='Flask extension for Beaker',
      long_description=__doc__,
      author='longfin',
      author_email='longfin@spoqa.com',
      url='http://github.com/spoqa/flask-beaker',
      packages=['flaskext', 'flaskext.beaker'],
      test_suite='test_beaker',
      tests_require=['flask-testing'],
      zip_safe = True,
      install_requires=[
        'setuptools',
        'Flask>=0.8',
        'Beaker'
        ],
      )
