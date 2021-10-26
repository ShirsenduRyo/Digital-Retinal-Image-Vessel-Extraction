import numpy as np
import cv2

def advanced_gamma(image, mean, std, gamma= 1/2.2):
    r1 = mean - std
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) * 255 for i in np.arange(0, 256)]).astype("uint8")

    for i in range(r1, 256):
        table[i] = int(((i / 255.0) ** invGamma) * 255)

    return cv2.LUT(image, table)

def image_stat(image, ch = 1):
    channel = image[:,:,ch]
    return int(np.mean(channel)), int(np.std(channel))

def transform_adaimg(image):
    #Red Channel
    red_mean, red_std = image_stat(image,0)
    red_channel = advanced_gamma(image[:,:,0], red_mean, red_std)
#     print(red_mean, red_std)
    
    #Green Channel
    green_mean, green_std = image_stat(image,1)
    green_channel = advanced_gamma(image[:,:,1], green_mean, green_std)
    
    #Blue Channel
    blue_mean, blue_std = image_stat(image,2)
    blue_channel = advanced_gamma(image[:,:,2], blue_mean, blue_std)
    
    merge = cv2.merge([red_channel, green_channel, blue_channel])
    return merge

def green_adaimg(image):
    l,w,h = image.shape
    
    #Red and blue
    null = np.array([0 for i in np.arange(0, 256)]).astype("uint8")
    null_channel = cv2.LUT(image[:,:,0], null)
    
    #Green Channel
    green_mean, green_std = image_stat(image,1)
    green_channel = advanced_gamma(image[:,:,1], green_mean, green_std)
    print(null.shape)
    
    merge = cv2.merge([null_channel, green_channel, null_channel])
    return merge

def blue_adaimg(image):
    l,w,h = image.shape
    
    #Red and blue
    null = np.array([0 for i in np.arange(0, 256)]).astype("uint8")
    null_channel = cv2.LUT(image[:,:,0], null)
    
    #Green Channel
    green_mean, green_std = image_stat(image,2)
    green_channel = advanced_gamma(image[:,:,2], green_mean, green_std)
    print(null.shape)
    
    merge = cv2.merge([null_channel, null_channel, green_channel])
    return merge

def red_adaimg(image):
    l,w,h = image.shape
    
    #Red and blue
    null = np.array([0 for i in np.arange(0, 256)]).astype("uint8")
    null_channel = cv2.LUT(image[:,:,0], null)
    
    #Green Channel
    green_mean, green_std = image_stat(image,0)
    green_channel = advanced_gamma(image[:,:,0], green_mean, green_std)
    print(null.shape)
    
    merge = cv2.merge([green_channel, null_channel, null_channel])
    return merge