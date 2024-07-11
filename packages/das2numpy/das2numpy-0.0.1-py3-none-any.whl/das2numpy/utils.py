"""
Everything, that modifies the signal.
author: Erik Genthe
"""

import numpy as NP
from numba import njit
import scipy.signal as SS

TIME_AXIS = 0

@DeprecationWarning
def remove_channel_offset(data:NP.ndarray):
    """Removes a constant value from each channel from the data.
        Expecting the time-axis to be the first axis! 
        The constant values are initially calculated and save to a file.
    """  

    print("Warning! Untested function!") #TODO
    #for i in range(data.shape[1]):
    #    data[:,i] -= data[:,i].mean(dtype=data.dtype)
    data -= data.mean(axis=0)

@njit
def differentiate(data: NP.ndarray, axis: int) -> NP.ndarray:
    """Differentiate the 2-dimensional signal over one axis
     A 2-d array is expected as input
     The return-value is None. The array is copied, modified and returned.
     :return: differentiated array
    """
    assert axis == 0 or axis == 1
    data = data.copy()
    if data.shape[axis] < 2:
        raise Exception("Integration with less then two samples makes no sense.")
    if axis == 0:
        for i in range(0, data.shape[0]-1):
            data[i] = data[i+1] - data[i]
    elif axis == 1:
        for i in range(0, data.shape[1]-1):
            data[:,i] = data[:,i+1] - data[:,i]
    return data

#@njit
#def integrate(data: NP.ndarray, axis: int) -> NP.ndarray:
#    """Integrate the 2-dimensional signal over one axis
#     A 2-d array is expected as input
#     The return-value is None. The array is copied, modified and returned.
#     :return: integrated array
#    """
#    assert axis == 0 or axis == 1
#    data = data.copy()
#
#    if data.shape[axis] < 2:
#        raise Exception("Integration with less then two samples makes no sense.")
#    if axis == 0:
#        for i in range(1, data.shape[0]):
#            data[i] = data[i] + data[i-1]
#    elif axis == 1:
#        for i in range(1, data.shape[1]):
#            data[:, i] = data[:, i] + data[:, i-1]
#    return data
def integrate(data: NP.ndarray, axis: int, sample_rate_hz:float) -> NP.ndarray:
    """Integrate the 2-dimensional signal over one axis
       A 2-d array is expected as input
       The array is copied, modified and returned.
       :return: integrated array
    """
    integral = NP.cumsum(data, axis=axis) / sample_rate_hz
    return integral


def butterworth_filter(
            array : NP.ndarray,
            freq : float, 
            order : int, 
            btype, #: {‘lowpass’, ‘highpass’}
            fs : float) -> NP.ndarray:
    """
    Apply a butterwort high-pass-filter on time-axis.
    :array: The input data. Two dimensions expected. First dimension is expected to be the time dimension.
    return: The filtered array
    """
    sos = SS.iirfilter(order, freq, rp=None, rs=None, btype=btype, analog=False, ftype='butter', output='sos', fs=fs)
    array = SS.sosfiltfilt(sos, array, axis=TIME_AXIS, padtype='odd', padlen=None)
    return array

#https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft
def fft(array):
    raise NotImplementedError("Not implemented yet")
    return None



def bin(arr: NP.ndarray, bin_factors:tuple):
    """ Returns a binned version of arr. If factors were 1, the original array is returned."""
    assert len(bin_factors) == len(arr.shape)
    #assert arr.dtype == NP.float32 or arr.dtype == NP.float64
    assert len(arr.shape) == 2
    for factor in bin_factors:
        assert factor > 0

    if bin_factors[0] == 1 and bin_factors[1] == 1:
        return arr

    newshape = NP.array(arr.shape) // NP.array(bin_factors)
    newarr = NP.empty(newshape, dtype=arr.dtype)
    _bin_helper(arr, newarr, bin_factors)
    return newarr

@njit
def _bin_helper(arr, newarr, bin_factors):
    for x in range(newarr.shape[0]):
        for y in range(newarr.shape[1]):
            x_ = x * bin_factors[0]
            y_ = y * bin_factors[1]
            newarr[x][y] = NP.mean(arr[x_ : x_ + bin_factors[0], y_ : y_ + bin_factors[1]])


def log_scale_symmetric(arr:NP.ndarray) -> NP.ndarray:
    """ Symmetric logarithmic scaling. For negative values it is applied as if they were positive"""

    zeros = NP.zeros(arr.shape)
    positives = NP.maximum(zeros, arr)
    negatives = NP.minimum(zeros, arr)

    positives += 1
    positives = NP.log2(positives, dtype=NP.float32)

    negatives *= -1
    negatives += 1
    negatives = NP.log2(negatives, dtype=NP.float32)
    negatives *= -1

    result = zeros
    result = negatives + positives
    return result
