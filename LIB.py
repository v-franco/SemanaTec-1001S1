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
            M[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2))) \
                        * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return M

"""
Functions mexHat, topSobel, rightSobel, and leftSobel made by Victor Franco
mexHat formula from: https://en.wikipedia.org/wiki/Ricker_wavelet
sobel kernels from: https://setosa.io/ev/image-kernels/

mexHat recevies sigma and size of kernel
sobel functions receive size of kernel
All functions returns respective generated kernels
"""
def mexHat(sigma, K):
    M = numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            M[x][y] = 1/(numpy.pi*sigma**4) * (1-(1/2)*((x**2+y**2)/(sigma**2))) \
                      * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return M

def topSobel(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = -2
    M[K//2 - 1][K//2] = 2
    M[K//2][K//2 + 1] = 0
    M[K//2][K//2 - 1] = 0
    M[K//2 + 1][K//2 + 1] = -1
    M[K//2 + 1][K//2 - 1] = -1
    M[K//2 - 1][K//2 + 1] = 1
    M[K//2 - 1][K//2 - 1] = 1
    return M

def rightSobel(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = 0
    M[K//2 - 1][K//2] = 0
    M[K//2][K//2 + 1] = 2
    M[K//2][K//2 - 1] = -2
    M[K//2 + 1][K//2 + 1] = 1
    M[K//2 + 1][K//2 - 1] = -1
    M[K//2 - 1][K//2 + 1] = 1
    M[K//2 - 1][K//2 - 1] = -1
    return M

def leftSobel(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = 0
    M[K//2 - 1][K//2] = 0
    M[K//2][K//2 + 1] = -2
    M[K//2][K//2 - 1] = 2
    M[K//2 + 1][K//2 + 1] = -1
    M[K//2 + 1][K//2 - 1] = 1
    M[K//2 - 1][K//2 + 1] = -1
    M[K//2 - 1][K//2 - 1] = 1
    return M
