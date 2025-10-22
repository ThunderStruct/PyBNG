

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
	from PyBNG import PyBNG
	bng = PyBNG(easting=519080, northing=185050)

	print(bng.get_latlon())

	print(PyBNG(lat=51.55178424773851, lon= -0.2835125528796557).get_bng())