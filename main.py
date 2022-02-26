from rgbToGray import * 
import cv2


if __name__ == '__main__':
    image1 = cv2.imread("lena.jpg")
    image2 = cv2.imread("lena.jpg")

    grayImg1 = rgbToGray(image1)
    grayImg2 = rgbToGray(image2)

    cv2.namedWindow("gray image",2)
    cv2.imshow("gray image",grayImg1)
    cv2.waitKey(0)
    cv2.destroyAllWindows
