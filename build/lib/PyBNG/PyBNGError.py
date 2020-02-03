'''
    PyBNG -- https://github.com/ThunderStruct/PyBNG
    Created on 1 Feb 2020
    @author: thunderstruct
'''

import traceback

class PyBNGError(Exception):
    """Exception sub-class used for raising custom PyBNG errors"""

    def __init__(self, message, error_type=None, inner=None):
        super(PyBNGError, self)
        msg_prefix = 'PyBNG Error: ' if error_type == None else 'PyBNG Error ({}): '.format(error_type)
        self.message = msg_prefix + message
        self.inner = inner
        self.traceback = traceback.format_stack()
        
    def __str__(self):
        return self.message