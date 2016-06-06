'''
    Write some helper method for the product
'''

import numpy as numpy
def RemoveNaN ( x ) :
    '''
    Remove all NaN value from input array
    '''
    #x = x[numpy.logical_not(numpy.isnan(x))]
    x = x[~numpy.isnan(x)]
    return x;    