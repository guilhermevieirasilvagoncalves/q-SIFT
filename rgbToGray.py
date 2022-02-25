def rgbToGray(image):
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    img = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return image