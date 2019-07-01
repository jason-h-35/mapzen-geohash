# Mapzen Geohash

[![Circle CI](https://circleci.com/gh/transitland/mapzen-geohash.png?style=badge)](https://circleci.com/gh/transitland/mapzen-geohash)

A geohash is a convenient method for encoding geographic coordinates, where each character in the geohash adds additional precision. This makes geohashes well suited for indexing mechanisms, grouping geographically located entities, and compactly encoding coordinates based on the level of detail required.

More information about Geohashes:

 * http://www.movable-type.co.uk/scripts/geohash.html
 * http://en.wikipedia.org/wiki/Geohash
 * http://geohash.org/

This Python package contains simple tools for encoding and decoding geohashes.

## Installation

Installation using pip:

```
pip install mz2geohash
```

Alternatively, [download from PyPi](https://pypi.python.org/pypi/mz2geohash) or clone this repository, and install using setup.py:

```
python ./setup.py install
```

## Example usage

```
>>> import mz2geohash
>>> mz2geohash.decode('xn76urwe1g9y')
(139.76608408614993, 35.681382017210126)
>>> mz2geohash.encode((139.76608408614993, 35.681382017210126))
'xn76urwe1g9y'
>>> mz2geohash.neighbors('xn76urwe1g9y')
{'c': 'xn76urwe1g9y',
 'e': 'xn76urwe1gdn',
 'n': 'xn76urwe1g9z',
 'ne': 'xn76urwe1gdp',
 'nw': 'xn76urwe1g9x',
 's': 'xn76urwe1g9v',
 'se': 'xn76urwe1gdj',
 'sw': 'xn76urwe1g9t',
 'w': 'xn76urwe1g9w'}
```
