from distutils.core import setup

import mzgeohash

setup(
  name='mz2geohash',
  version=mzgeohash.__version__,
  description='Mapzen Geohash',
  author='Jason Hatton',
  author_email='jason@hatton.io',
  url='https://github.com/jason-h-simplifi/mapzen-geohash',
  license='License :: OSI Approved :: MIT License',
  packages=['mzgeohash']
)