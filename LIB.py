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

""""
Receives sigma and size of kerne
Returns gauss blur kernel

Function gaussBlur made by Ruben Ruiz
Based on: https://stackoverflow.com/questions/29731726/how-to-calculate-a-gaussian-kernel-matrix-efficiently-in-numpy

"""
#
def gaussBlur(sigma, K):
    ax = numpy.linspace(-(K-1)/2., (K-1)/2.,K)
    gauss = numpy.exp(-0.5 * numpy.square(ax) / numpy.square(sigma))
    M = numpy.outer(gauss, gauss)
    return M / numpy.sum(M)


"""
Function laplacianOfGaussian made by Myron Bean
Receives sigma and size of kernel
Returns laplacian of gaussian kernel
Formula from: https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm

"""
def laplacianOfGaussian(sigma, K):
    M = numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            M[x][y] = -(1/(numpy.pi*sigma4)) * (1-((x2+y2)/(2*sigma2))) \
                        * numpy.exp(-(x2+y2)/(2*sigma**2))
    return M
