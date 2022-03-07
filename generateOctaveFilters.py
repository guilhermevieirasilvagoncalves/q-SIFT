import numpy as np

def generateOctaveFilters(sigma, numintervalos):
    imagensPorOitava = numintervalos + 3
    i = imagensPorOitava
    k = 2 ** (1 / i)
    filtrosGaussianos = np.zeros(i)
    filtrosGaussianos[0] = sigma
    for indexdaImagem in range(1,i):
        sigmaAnterior = (k ** (indexdaImagem - 1)) * sigma
        totalSigma = k * sigmaAnterior
        filtrosGaussianos[indexdaImagem] = np.sqrt(totalSigma ** 2 - sigmaAnterior ** 2)
    return filtrosGaussianos 