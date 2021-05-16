import numpy as np
import cv2

def translate(img, shift=5, direction='right', roll=True):

    assert direction in ['right', 'left', 'down', 'up'], 'Directions should be top|up|left|right'
    copied_image = img
    copied_image = copied_image.reshape(1, 48, 48, 1)
    if direction == 'right':
        right_slice = copied_image[:, -shift:].copy()
        copied_image[:, shift:] = copied_image[:, :-shift]
        if roll:
            copied_image[:,:shift] = np.fliplr(right_slice)
    if direction == 'left':
        left_slice = copied_image[:, :shift].copy()
        copied_image[:, :-shift] = copied_image[:, shift:]
        if roll:
            copied_image[:, -shift:] = left_slice
    if direction == 'up':
        upper_slice = copied_image[:shift, :].copy()
        copied_image[:-shift, :] = copied_image[shift:, :]
        if roll:
            copied_image[-shift:,:] = upper_slice
    return copied_image

def flip(img):
    copied_image = img
    copied_image = copied_image.reshape(1, 48, 48, 1)
    return cv2.flip(copied_image[0], 1)