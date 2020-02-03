'''
    PyBNG -- https://github.com/ThunderStruct/PyBNG
    Created on 1 Feb 2020
    @author: thunderstruct
'''


from OSGridConverter import grid2latlong, latlong2grid
import PyBNGError
import math

class PyBNG:
    """
    Description:
        PyBNG is a library built on-top of OSGridConverter and is used to convert coordinates
        from the Ordnance Survey National Grid system (often called the British National Grid (BNG)) to
        latitude and longitude (WGS84 -- other geodetic reference systems available).

        While OSGridConverter can convert BNG to WGS84, it does not support all-numeric grid references, 
        which is the primary feature in this library.
    """

    __alpha = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
    __mat = None

    def __init__(self, **kwargs):
        """
        PyBNG constructor

        Parameters:
            easting: int, northing: int, lat: float, lon: float, datum: str
            provide (easting and northing) OR (lat and long)

            Acceptable datum values:
                WGS84 (default), OSGB36, ED50, Irl1975, NTF, TokyoJapan, NAD83
        """

        self.easting, self.northing = None, None
        self.lat, self.lon = None, None

        if 'easting' in kwargs and 'northing' in kwargs:
            self.easting = kwargs['easting']
            self.northing = kwargs['northing']
        elif 'lon' in kwargs and 'lat' in kwargs:
            self.lon = kwargs['lon']
            self.lat = kwargs['lat']
        else:
            raise PyBNGError('Expected ("easting" and "northing") or ("lon" and "lat") arguments.', error_type='Missing Argument')

    #=======================#
    #     PUBLIC METHODS    #
    #=======================#

    def get_latlon(self, datum='WGS84'):
        """
        Calculates the latitude and logitude based on the given BNG coordinates

        Parameters: none (passed to constructor)
        
        Return value: tuple -- latitude, longitude
        """

        # return pre-calculated lat/lon values if they exist
        if self.lat is not None and self.lon is not None:
            return (self.lat, self.lon)

        # lat/lon are None, easting and northing must exist by the init constraint
        return self.__calculate_latlon(datum)

    def get_bng(self, datum='WGS84'):
        """
        Calculates the BNG coordinates given a latitude and a longitude
        
        Parameters: none (passed to constructor)
        
        Return value: tuple -- easting, northing
        """

        # return pre-calculated easting/northing values if they exist
        if self.easting is not None and self.northing is not None:
            return (self.easting, self.northing)

        # lat/lon are None, easting and northing must exist by the init constraint
        return self.__calculate_bng(datum)


    #=======================#
    #    PRIVATE METHODS    #
    #=======================#

    def __calculate_latlon(self, datum):

        e_digits = int(math.log10(self.easting)) + 1
        n_digits = int(math.log10(self.northing)) + 1

        multi_dig_n = n_digits > e_digits

        extracted_e_dig = self.easting // 10 ** (e_digits - 1)
        extracted_n_dig = self.northing // 10 ** (n_digits - (2 if multi_dig_n else 1))
        str_easting = str(self.easting)[1:]
        str_northing = str(self.northing)[(2 if multi_dig_n else 1):]

        convmat = PyBNG.__gen_conv_matrix()

        grid_ref = None
        for i in range(len(convmat)):
            for j in range(len(convmat[i])):
                if (convmat[i][j][2] == extracted_e_dig) and (convmat[i][j][3] == extracted_n_dig):
                    letters = convmat[i][j][0] + convmat[i][j][1]
                    grid_ref = letters + ' ' + str_easting + ' ' + str_northing
                    break

        if grid_ref is None:
            raise PyBNGError('The entered easting and northing values are invalid', error_type='Invalid Grid Reference')

        latlon = grid2latlong(grid_ref, datum)
        return (latlon.latitude, latlon.longitude)


    def __calculate_bng(self, datum):
        
        bng = latlong2grid(self.lat, self.lon, datum)

        return (bng.E, bng.N)



    # #=======================#
    # #    STATIC METHODS     #
    # #=======================#

    @staticmethod
    def __gen_conv_matrix():
        """
        Generates the conversion matrix required for standard BNG to all-numeric 
        reference conversions

        Parameters: none

        Return value: matrix (2D List) of tuple -- [[(l1, l2, n1, n2)]]
        """

        if PyBNG.__mat is not None:
            # already generated and stored statically -- prevents redundant calculation
            return PyBNG.__mat

        # start point -- SV (lower-left)
        l1_i, l2_i = 17, 20
        n1, n2 = 0, 0
        dim_w, dim_h = 8, 13

        PyBNG.__mat = [[0 for x in range(dim_w)] for y in range(dim_h)]

        for i in range(dim_h):
            row_l2i = l2_i
            row_l1i = l1_i
            for j in range(dim_w):
                PyBNG.__mat[dim_h - i - 1][j] = (PyBNG.__alpha[l1_i], PyBNG.__alpha[l2_i], n1, n2)

                # Update values
                n1 += 1
                if j == 4:
                    l2_i = row_l2i - 1
                    l1_i = (l1_i + 1) % len(PyBNG.__alpha)
                l2_i = (l2_i + 1) % len(PyBNG.__alpha)

            n1 = 0
            n2 += 1
            l2_i = (row_l2i - 5) % len(PyBNG.__alpha)
            if row_l2i == 0:
                row_l1i -= 5
            l1_i = row_l1i

        return PyBNG.__mat


    # @staticmethod
    # def to_latlon(easting, northing):
    #     pass

    # @staticmethod
    # def from_latlon(lat, lon):
    #     pass
        



    