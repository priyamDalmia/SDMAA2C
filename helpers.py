import numpy as np
import pycuda
import pycuda.driver as drv

import time

def print_device_count():
    """
    List the number of CUDA capable deivices, !
    """
    drv.init()
    print(f"CUDA Capable devices detected: {drv.Device.count()}")


def build_env():
    pass


def time_function(*args):
    time_start = time.perf_counter()
    time_end = time.perf_counter()
    return time_end - time_start



