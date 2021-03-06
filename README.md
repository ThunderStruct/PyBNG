# PyBNG
[![Build Status](https://travis-ci.org/ThunderStruct/PyBNG.svg?branch=master)](https://travis-ci.org/ThunderStruct/PyBNG) [![pypi](https://img.shields.io/badge/pypi%20package-0.1.8-lightgrey.svg)](https://pypi.org/project/PyBNG/0.1.8/) [![Python](https://img.shields.io/badge/python-3.5^-blue.svg)](https://github.com/ThunderStruct/PyBNG) [![License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](https://github.com/ThunderStruct/PyBNG/blob/master/LICENSE)

An Ordinance-Survey National Grid coordinates converter

------------------------

## Getting Started
PyBNG is built on top of [OSGridConverter](https://github.com/jdstmporter/OSGridConverter/) and is used to convert coordinates from the Ordnance Survey National Grid system (often called the British National Grid -- *BNG*) to latitude and longitude using `WGS84` (other geodetic reference systems available).

While OSGridConverter can convert BNG to latitude and longitude, it does not support all-numeric grid references, which is the primary feature in this library.

### Installation
#### PIP (recommended)

```sh
pip install PyBNG
```
#### Manual Installation
Simply clone the entire repo and extract the files in the `PyBNG` folder, then copy all the content to your project folder

Or use one of the shorthand methods below
##### GIT
  - `cd` into your project directory
  - Use `sparse-checkout` to pull the library files only into your project directory
    ```sh
    git init PyBNG
    cd PyBNG
    git remote add -f origin https://github.com/ThunderStruct/PyBNG.git
    git config core.sparseCheckout true
    echo "PyBNG/*" >> .git/info/sparse-checkout
    git pull --depth=1 origin master
    ```
   - Import the newly pulled files into your project folder

##### SVN
  - `cd` into your project directory
  - `checkout` the library files
    ```sh
    svn checkout https://github.com/ThunderStruct/PyBNG/trunk/PyBNG
    ```
  - Import the newly checked out files into your project folder
  

### Usage
#### Initialization
A `PyBNG` object can be instantiated as follows:

```python
from PyBNG import PyBNG

bng = PyBNG(easting=519080, northing=185050)

latlon = PyBNG(lat=51.55178424773851, lon= -0.2835125528796557)
```
The initializer expects `easting` and `northing` *OR* `lat` and `lon` parameters, depending on the required conversion


### Methods

  - `get_latlon(datum='WGS84')`:
    - Description: calculates the latitude and logitude based on the given BNG coordinates
    - Parameters: none (passed to constructor)
    - Return Value: tuple -- (latitude, longitude)
    - Usage: 
        ```python
        from PyBNG import PyBNG

        bng = PyBNG(easting=519080, northing=185050)
        bng.get_latlon()     # (51.55178424773851, -0.2835125528796557)
        ```
  - `get_bng(datum='WGS84')`:
    - Description: calculates the BNG coordinates given a latitude and a longitude
    - Parameters: none (passed to constructor)
    - Return Value: typle -- (easting, northing)
    - Usage: 
        ```python
        from PyBNG import PyBNG

        latlon = PyBNG(lat=51.55178424773851, lon= -0.2835125528796557)
        latlon.get_bng()     # (519107, 185051)
        ```
*Please note that converting BNG coordinates to latitude/longitude and back to BNG will yield different results due to internal float rounding*

### Acknowledgment
I would like to thank [Dr. Lakshmi Babu-Saheer](mailto:lakshmi.babu-saheer@anglia.ac.uk) for her unwavering support, encouragement, and advice. 

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ThunderStruct/PyBNG/blob/master/LICENSE) file for details


