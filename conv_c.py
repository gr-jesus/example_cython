import ctypes
import sys
import os 

lib = ctypes.cdll.LoadLibrary("./libtest.so")
arg_type=ctypes.c_float * 9

def c_conv(img, fil):
    result=ctypes.c_float(0.0)
    lib.c_convolution(arg_type(*img), arg_type(*fil), ctypes.byref(result))
    return result.value
