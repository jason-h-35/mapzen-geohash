import setuptools
from distutils.core import setup

import mz2geohash

setup(
  name='mz2geohash',
  version=mz2geohash.__version__,
  description='Mapzen Geohash Fork.  The original is long unmaintained.',
  author='Jason Hatton',
  author_email='jason@hatton.io',
  url='https://github.com/jason-h-simplifi/mapzen-geohash',
  license='License :: OSI Approved :: MIT License',
  packages=['mz2geohash']
)