import numpy as np

def numeroOitavas(shape):
    numOitavas = int(round(np.log(min(shape)) / np.log(2) - 1))
    return numOitavas
