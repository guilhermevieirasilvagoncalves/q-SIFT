from numpy import imag
from generateOctaveFilters import generateOctaveFilters
from generateOctaveImages import generateOctaveImages
from rgbToGray import *
from gaussianFilter import *
from octaves import *
import cv2

if __name__ == '__main__':
    image1 = cv2.imread("lena.jpg")
    image2 = cv2.imread("lena.jpg")
    
    sigma = 1.6
    numintervalos = 3

    grayImg1 = rgbToGray(image1)
    grayImg2 = rgbToGray(image2)

    filtroGaussiano = gaussianFilter(sigma)
    imgGaussiana = convolucao(grayImg1, filtroGaussiano)
    numOitavas = numeroOitavas(imgGaussiana.shape)
    filtrosOitavas = generateOctaveFilters(sigma, numintervalos)
    imagensOitavas = generateOctaveImages(imgGaussiana, numOitavas,filtrosOitavas)
    cv2.namedWindow("gray image",2) 
    cv2.imshow("gray image",imagensOitavas[0][0])
    print("Geração de imagem com filtro gaussino\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows
