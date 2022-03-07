from rgbToGray import *
from gaussianFilter import *
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

    cv2.namedWindow("gray image",2)
    cv2.imshow("gray image",imgGaussiana)
    cv2.waitKey(0)
    cv2.destroyAllWindows
