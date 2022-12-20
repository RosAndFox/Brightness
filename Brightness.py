from PIL import Image, ImageEnhance
from scipy import ndimage
import os
import cv2
import numpy
os.chdir(r'C:\Users\Ros\Downloads')
im_enh=cv2.imread('1_264_0.png')/255
im_blurred=ndimage.gaussian_filter(im_enh, 5)
im_out=numpy.clip((2*im_enh-im_blurred)*255, 0, 255)
os.chdir(r'C:\Users\Ros\Магистратура\NIR\Good_tooth')
cv2.imwrite('1_264_1.png', im_out)
im=Image.open('1_264_1.png')
enhancer=ImageEnhance.Brightness(im)
im_out=enhancer.enhance(0.15)
enhancer=ImageEnhance.Contrast(im_out)
im_enh=enhancer.enhance(3)
im_enh.save('1_264_2.png')
