import cv2
import numpy as np
from skimage import color

def rgbToGray(image):
    image = color.rgb2gray(image)
    return image