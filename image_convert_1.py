# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:24:35 2019

картинка в массив

@author: surkov
"""
from PIL import Image

i = Image.open("agama.jpg")

pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        for pixel_ in cpixel:
            all_pixels.append(pixel_)
        all_pixels.append(127)    
        #all_pixels.append(cpixel)

print(len(all_pixels))