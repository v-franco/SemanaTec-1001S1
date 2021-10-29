import matplotlib.pyplot as plt
import numpy
import argparse

from PIL import Image
from scipy import ndimage

from LIB import *

"""
Function imageProcessing converts image to greyscale, adds padding, 
generates kernels using the functions from LIB, convolutes the images
using the kernels (kernelTS-kernelLG) and generates a 3*3 plot with the results
"""
def imageProcessing(image):
    #Process image, change to grayscale, and numeric conversion 0-1
    ogImage = Image.open(image)
    Is = ogImage.convert('L')
    Is = numpy.asarray(Is)
    Is = Is / 255.0

    #Function pad_with generates padding 
    def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

    Is = numpy.pad(Is, 10, pad_with, padder=1)

    #Generate the kernel for each image convolution
    kernelTS = topSobel(3) #Size of kernel
    kernelRS = rightSobel(3) #Size of kernel
    kernelLS = leftSobel(3) #Size of kernel
    kernelGB = gaussBlur(9,9) #Sigma & size of kernel
    kernelMH = mexHat(3,9) #Sigma & size of kernel
    kernelLA = laplaceA(9) #Size of kernel
    kernelLB = laplaceB(9) #Size of kernel
    kernelLG = laplacianOfGaussian(9,9) #Sigma & size of kernel
  
    #Generate each image convolution
    imageTS = ndimage.convolve(Is, kernelTS, mode='constant', cval=0.0)
    imageRS = ndimage.convolve(Is, kernelRS, mode='constant', cval=0.0)
    imageLS = ndimage.convolve(Is, kernelLS, mode='constant', cval=0.0)
    imageGB = ndimage.convolve(Is, kernelGB, mode='constant', cval=0.0)
    imageMH = ndimage.convolve(Is, kernelMH, mode='constant', cval=0.0)
    imageLA = ndimage.convolve(Is, kernelLA, mode='constant', cval=0.0)
    imageLB = ndimage.convolve(Is, kernelLB, mode='constant', cval=0.0)
    imageLG = ndimage.convolve(Is, kernelLG, mode='constant', cval=0.0)

    #Show the new images in a 3x3 matrix 
    plt.figure(figsize = (15,15))

    plt.subplot(3,3,1)
    plt.imshow(ogImage)
    plt.xlabel('Input Image')

    plt.subplot(3,3,2)
    plt.imshow(imageTS)
    plt.xlabel('Top Sobel')

    plt.subplot(3,3,3)
    plt.imshow(imageRS)
    plt.xlabel('Right Sobel')

    plt.subplot(3,3,4)
    plt.imshow(imageLS)
    plt.xlabel('Left Sobel')

    plt.subplot(3,3,5)
    plt.imshow(imageGB)
    plt.xlabel('Gaussian blur')

    plt.subplot(3,3,6)
    plt.imshow(imageMH)
    plt.xlabel('Ricker Wavelet (Mexican hat)')

    plt.subplot(3,3,7)
    plt.imshow(imageLA)
    plt.xlabel('Laplacian Operator')

    plt.subplot(3,3,8)
    plt.imshow(imageLB)
    plt.xlabel('Laplacian Operator w/diagonals')

    plt.subplot(3,3,9)
    plt.imshow(imageLG)
    plt.xlabel('Laplacian of Gaussian')

    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    #get image arguments from the shell  "python main.py test_images/image.jpg"
    ap = argparse.ArgumentParser()
    ap.add_argument("image", help="Path to the image", type=str)
    args = ap.parse_args()
    imageProcessing(args.image)