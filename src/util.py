import numpy as np
import cv2

def pre_process_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)  # convert color image into gray scale image
    resized_image = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(resized_image,
                                            255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 61, 12)
    return processed_image