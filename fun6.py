import numpy as np
import cv2 as cv

def fun6():
    mat1=np.ones((3,4), np.int32)
    mat2=np.arange(12).reshape(3,4)
    mat3=mat1+mat2
    mat4=mat2*2

    print("mat1 : ")
    print(mat1)
    print("mat2 : ")
    print(mat2)
    print("mat3 : ")
    print(mat3)
    print("mat4 : ")
    print(mat4)

fun6()