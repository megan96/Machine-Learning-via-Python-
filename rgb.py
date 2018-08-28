import sys
import os
import numpy as np
import cv2

def split_into_rgb_channels(image):
    red = image[:,:,2]
    green = image[:,:,1]
    blue = image[:,:,0]
    return red, green, blue

def main():
    img= cv2.imread("flower.jpg")
    red, green, blue = split_into_rgb_channels(img)
    print (img)
    for values, color, channel in zip((red, green, blue), 
            ('red', 'green', 'blue'), (2,1,0)):
        img = np.zeros((values.shape[0], values.shape[1], 3), dtype = values.dtype) 
        img[:,:,channel] = values

if __name__ == "__main__":
    main()
