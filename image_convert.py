# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:24:35 2019

@author: surkov
"""
from PIL import Image
import image_list

img = image_list.img()

#print(len(img))

elem_index = 0
red_val = 0
green_val = 0
blue_val = 0
alfa_val = 0

img_arr = []

for elem in img:
    if elem_index == 0:
        red_val = elem
    if elem_index == 1:
        green_val = elem    
    if elem_index == 2:
        blue_val = elem
    if elem_index == 3:
        alfa_val = elem
    elem_index = elem_index + 1
    if elem_index == 4:
        img_arr.append((red_val, green_val, blue_val))
        elem_index = 0
        
#print(img_arr)
img_ = Image.new("RGB", (160,160))
img_.putdata(img_arr)

img_.save('sample.jpg')