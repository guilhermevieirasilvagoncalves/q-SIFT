from skimage import color

def rgbToGray(image):
    image = color.rgb2gray(image)
    return image