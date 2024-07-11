""" Univsersal setup file for silixa, that detects sampling rate and number of channels by itself. 
The root directory shall be supplied by the user via an argument
"""

import sys as SYS
from os import path as P
import datetime as DT
import numpy as NP
from ..filefinder import FileFinder, to_posix_timestamp_ms
from ..chunk import Chunk
from .light_tdms_reader import TdmsReader


CALIBRATE = True





def init(root_path, num_worker_threads):
    assert P.isdir(root_path)
    file_time_sample_amount = 20000
    file_finder = FileFinder(root_path, ".tdms", filename_to_posix_timestamp)
    example_file_path = file_finder.get_first()[1]
    tdms = TdmsReader(example_file_path)
    shape = tdms.get_mmap().shape
    file_time_sample_amount = shape[0]
    channel_amount = shape[1]
    #channel_amount = tdms.fileinfo['n_channels']
    #props = tdms.get_properties()
    #fs = props.get('SamplingFrequency[Hz]') #TODO read sampling freq from file
    return Chunk(
                file_finder,
                channel_amount, 
                file_time_sample_amount, 
                True,
                num_worker_threads,
                False,
                load_file
            )

def filename_to_posix_timestamp(file_name:str) -> int:
    return to_posix_timestamp_ms(DT.datetime.strptime(file_name[-24:], "%Y%m%d_%H%M%S.%f.tdms"))



def load_file(file_path, rel_t_start, rel_t_end, t_step, channel_start, channel_end, channel_step) -> NP.ndarray:
    #assert rel_t_end <= FILE_TIME_SAMPLE_AMOUNT
    assert rel_t_start != rel_t_end
    assert rel_t_start < rel_t_end
    assert rel_t_start >= 0

    tdms = TdmsReader(file_path)
    data = tdms.get_mmap()
    data = data[rel_t_start:rel_t_end, channel_start:channel_end]
    if t_step != 1:
        data = data[::t_step]
    if channel_step != 1:
        data = data[:, ::channel_step]
    assert len(data) > 0

    if CALIBRATE:
        data = calibrate(data)

    return data





def calibrate(data:NP.ndarray) -> NP.ndarray:
    """ Convert raw data to strain rate data. 
    As the resulting values are decimals, the datatype should be float. Otherwise an assertion fails. """
    #assert data.dtype in (NP.float, NP.float32, NP.float64), f"The data should be floating point. It is {data.dtype}"
    if data.dtype not in (NP.float, NP.float32, NP.float64):
        NEW_TYPE = NP.float32
        #print("Warning: For calibration the data has to be of type float. Converting from {data.dtype} to {NEW_TYPE}")
        data = data.astype(NEW_TYPE)

    SAMPLE_FREQ = 1000.0
    EICHLAENGE = 10.0
    factor = 116.0 * 10.0**(-9.0) / 8192.0 * SAMPLE_FREQ / EICHLAENGE
    return data * factor # Result: 1 / s




