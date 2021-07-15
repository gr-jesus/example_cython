from conv_cython import conv_operation
from conv_c import c_conv
import ctypes


def conv_operation_py(img, filter):
    result = 0
    for pixel in range(len(img)):
        result+=(img[pixel]*filter[pixel])
    return result



img=[255.,255.,255.,255.,255.,255.,5.,128.,0.]
filter=[-1.,0.,-1.,0.,4.,0.,-1.,0.,-1.]

print(conv_operation(img, filter))

print(conv_operation_py(img, filter))
print(c_conv(img, filter))


