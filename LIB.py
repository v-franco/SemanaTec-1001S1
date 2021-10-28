import numpy


"""
Functions laplaceA & laplaceB made by Horacio Lamas

The laplace set of functions are used to find edges on an image. 
The function "laplaceA" creates and returns a KxK matrix without diagonals.
The function "laplaceB" creates and returns a KxK matrix with diagonals.
Kernels from: https://aishack.in/tutorials/image-convolution-examples/
"""
def laplaceA(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 4
    M[K//2 + 1][K//2] = -1
    M[K//2 - 1][K//2] = -1
    M[K//2][K//2 + 1] = -1
    M[K//2][K//2 - 1] = -1
    return M

def laplaceB(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 8
    M[K//2 + 1][K//2] = -1
    M[K//2 - 1][K//2] = -1
    M[K//2][K//2 + 1] = -1
    M[K//2][K//2 - 1] = -1
    M[K//2 + 1][K//2 + 1] = -1
    M[K//2 + 1][K//2 - 1] = -1
    M[K//2 - 1][K//2 + 1] = -1
    M[K//2 - 1][K//2 - 1] = -1
    return M
