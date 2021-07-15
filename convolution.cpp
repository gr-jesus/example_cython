#include<stdio.h>

/* Program to apply the convolution operation in a part of an image*/
float convolution(float img[], float filter[], float *result){
    int size=9;
    for(int i=0; i<size; i++){
        *result+=(img[i]*filter[i]);
    }
}

extern "C"{
    float c_convolution(float im[], float f[], float *res){
        return convolution(im, f, res);
    }
}