#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:52:48 2022

@author: ys2af
"""
from matplotlib.colors import hsv_to_rgb
from mpl_toolkits.mplot3d.axes3d import get_test_data
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mimage
import cv2
from copy import deepcopy
from scipy import ndimage
from skimage import measure,color
from skimage.measure import label, regionprops
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimage
from PIL import Image
import cv2
import scipy.signal
import os, os.path
from scipy import ndimage
from skimage import measure,color
from skimage.segmentation import find_boundaries
from skimage.morphology import thin, skeletonize, medial_axis
from skimage.measure import label, regionprops
from scipy.spatial import Voronoi
from scipy.spatial import cKDTree
import os
import matplotlib.pyplot as plt
from skimage import data
#from skimage.filters import threshold_otsu, threshold_adaptive
from scipy.spatial import distance
import math
from copy import deepcopy
from scipy.ndimage import gaussian_filter
from skimage import img_as_float
from skimage.morphology import reconstruction

from scipy.signal import argrelextrema
from skimage import data
from skimage.filters.rank import entropy
from skimage.morphology import disk
import timeit
import cmapy
import argparse


parser = argparse.ArgumentParser(description='Masking some images')
parser.add_argument("-i","--input_path", type=str,
                    help="type input path", required = True)
parser.add_argument("-o", "--output_path", type=str,
                    help="type output path", required = True)
args = parser.parse_args()

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
	
	ORO = cv2.imread(args.input_path,0)
	source = deepcopy(ORO)

	ent = entropy(source, disk(5))

	hist = list(np.histogram(ent,30))

	minindex = list(argrelextrema(hist[0], np.less))

	for i in range(len(minindex[0])):
	    temp_thresh = hist[1][minindex[0][i]]
	    if temp_thresh>1 and temp_thresh<4:
		thresh_localminimal = temp_thresh

	thresh1 = (255*filter_entropy_image(ORO, thresh_localminimal)).astype('uint8')

	mask_255 = cv2.bitwise_not(deepcopy(thresh1))
	cv2.imwrite(args.output_path, mask_255)

	
if __name__ == "__main__":
	main()

