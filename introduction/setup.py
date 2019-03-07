try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Skeleton',
  'author': 'Ben Hong',
  'url': 'www.github.com/bencodezen',
  'author_email': 'bencodezen@gmail.com',
  'install_requires': ['nose'],
  'packages': ['Skeleton']
}

setup(**config)