import numpy as np
from scipy.ndimage.filters import convolve
from cv2 import GaussianBlur, INTER_NEAREST, resize
from gaussianFilter import *

def generateOctaveImages(image, numOitavas, filtrosGaussianos):
    imagensGaussianas = []
    for indexdaOitava in range(numOitavas):
        imgGaussianOitava = []
        imgGaussianOitava.append(image)
        for filtrosGaussianos in filtrosGaussianos[1:]:
            image = GaussianBlur(image, (0, 0), sigmaX=filtrosGaussianos, sigmaY=filtrosGaussianos)
            #image = convolucao(image, filtrosGaussianos)
            imgGaussianOitava.append(image)
        imagensGaussianas.append(imgGaussianOitava)
        baseOitava = imgGaussianOitava[-3]
        image = resize(baseOitava, (int(baseOitava.shape[1] / 2), int(baseOitava.shape[0] / 2)), interpolation=INTER_NEAREST)
        return np.array(imagensGaussianas)