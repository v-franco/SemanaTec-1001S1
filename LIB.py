import numpy

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