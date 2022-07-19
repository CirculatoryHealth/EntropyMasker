#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:52:48 2022
@author: ys2af
"""
import numpy as np
from copy import deepcopy
from PIL import Image
import cv2
import scipy.signal
from scipy.signal import argrelextrema
from skimage.filters.rank import entropy
from skimage.morphology import disk
import argparse


parser = argparse.ArgumentParser(description='Masking some images')
parser.add_argument("-i","--input_path", type=str,
                    help="type input path", required = True)
parser.add_argument("-o", "--output_path", type=str,
                    help="type output path", required = True)


def filter_entropy_image(image, filter, disk_radius:int = 3):
	
	eimage = entropy(image, disk(disk_radius))
	new_picture =  np.ndarray(shape=eimage.shape) #[[False] * image.shape[1]] * image.shape[0]
	for rn, row in enumerate(eimage):
		for pn, pixel in enumerate(row):
			if pixel < filter:
				new_picture[rn,pn] = True
			else:
				new_picture[rn,pn] = False
	return new_picture.astype('b')


def main():

    args = parser.parse_args()
    ORO = cv2.imread(args.input_path,0)
    source = deepcopy(ORO)
    ent = entropy(source, disk(5))
    
    hist = list(np.histogram(ent,30))
    minindex = list(argrelextrema(hist[0], np.less))

    for i in range(len(minindex[0])):
        temp_thresh = hist[1][minindex[0][i]]
        if temp_thresh > 1 and temp_thresh < 4:
            thresh_localminimal = temp_thresh
    
    thresh1 = (255*filter_entropy_image(ORO, thresh_localminimal)).astype('uint8')
    mask_255 = cv2.bitwise_not(deepcopy(thresh1))
    cv2.imwrite(args.output_path, mask_255)

	
if __name__ == "__main__":
	main()
