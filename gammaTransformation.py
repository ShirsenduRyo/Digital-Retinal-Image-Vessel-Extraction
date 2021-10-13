import numpy as np
import cv2

def transform_img(image):
    #Red Channel
    red_mean, red_std = int(41), int(25)
    red_channel = advanced_gamma(image[:,:,0], red_mean, red_std)
    
    #Green Channel
    green_mean, green_std = int(69), int(45)
    green_channel = advanced_gamma(image[:,:,1], green_mean, green_std)
    
    #Blue Channel
    blue_mean, blue_std = int(127), int(85)
    blue_channel = advanced_gamma(image[:,:,2], blue_mean, blue_std)
    
    merge = cv2.merge([blue_channel, green_channel, red_channel])
    return merge

def advanced_gamma(image, mean, std, gamma= 1/2.2, gamma2 = 1/3.6):
    r1 = mean - std
    r2 = mean + std

    
    invGamma = 1.0 / gamma
    invGamma2 = 1.0 / gamma2
    
    table = np.array([(i / 255.0) * 255 for i in np.arange(0, 256)]).astype("uint8")

    for i in range(0,r1+1):
        table[i] = int(((i / 255.0) ** invGamma) * 255)
    
    for i in range(r1, r2 + 1):
        table[i] = int(((i / 255.0) ** invGamma2) * 255)
    
    for i in range(r2,256):
        table[i] = int(((i / 255.0) ** invGamma) * 255)
    
    
    return cv2.LUT(image, table)