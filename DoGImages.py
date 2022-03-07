import numpy as np
def DogImages(imagensOitava):
    imagensdaDoG = []
    for imgGaussianOitava in imagensOitava:
        DoGOitava = []
        for image1, image2 in zip(imgGaussianOitava, imgGaussianOitava[1:]):
            DoGOitava.append(np.subtract(image1, image2)) 
        imagensdaDoG.append(imgGaussianOitava)
    return np.array(imagensdaDoG, dtype=object)