

cpdef conv_operation(img, filter):
    cdef float result = 0
    cdef int pixel  = 0
    for pixel in range(len(img)):
        result+=(img[pixel]*filter[pixel])
    return result
