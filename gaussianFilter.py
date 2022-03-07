import numpy as np
from scipy.ndimage.filters import convolve

def gaussianFilter(sigma):
    size = 2*np.ceil(3*sigma)+1 
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1] 
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2))) / (2*np.pi*sigma**2)
    return g/g.sum()

def convolucao(image, gaussianfilter):
    image = convolve(image, gaussianfilter)
    return image

