#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:52:48 2022
@author: ys2af
"""

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                                                  EntropyMasker                                             +")
print("+                    An automatic entropy method to efficiently mask histology whole-slide images            +")
print("+                                                                                                            +")
print("+* Version          : v1.0.0                                                                                 +")
print("+                                                                                                            +")
print("+* Last update      : 2022-07-06                                                                             +")
print("+* Written by       : Yipei Song | Craig Glastonbury | Sander W. van der Laan | Clint L. Miller.             +")
print("+                                                                                                            +")
print("+* Description      : This method will mask background from whole-slide images for downstream image          +")
print("+                     analyses.                                                                              +")
print("+                     The (path) to an image is given (e.g. path_to/img.png) and a named masked image is     +")
print("+                     saved (e.g. path_to/img.emask.png).                                                    +")
print("+                                                                                                            +")
print("+                     Note: It may be necessary to first extract the relevant layer from .TIF or .ndpi       +")
print("+                     whole-slide images.                                                                    +")
print("+                                                                                                            +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# general
import glob
import os
from pathlib import Path

# import required packages
import numpy as np
from copy import deepcopy
from PIL import Image
import cv2
import openslide
from openslide import *
import scipy.signal
from scipy.signal import argrelextrema
from skimage.filters.rank import entropy
from skimage.morphology import disk

# for argument parser
from sys import exit, argv
import argparse
import textwrap
# import argparse

# old version
# parser = argparse.ArgumentParser(description='Masking some images')
# parser.add_argument("-i","--input_path", type=str,
#                     help="type input path", required = True)
# parser.add_argument("-o", "--output_path", type=str,
#                     help="type output path", required = True)


# new version
parser = argparse.ArgumentParser(
	prog='EntropyMasker',
	description='This script will mask background from whole-slide images and save masked-images for downstream image analyses.',
	usage='python EntropyMasker.py -i/--input_img -o/--output_img; for help: -h/--help',
	# usage='python EntropyMasker.py -i/--input_img -o/--output_img; optional: -d/--display -s/--suffix -t/--type -f/--force -v/--verbose; for help: -h/--help',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=textwrap.dedent("Copyright (c) 2022. Yipei Song | Craig Glastonbury | Sander W. van der Laan | Clint L. Miller."))

parser.add_argument("-i","--input_img", type=str,
                    help="An input image (or directory containing image files) should be given. Try: IMG012.ndpi, *.TIF or /path_to/images/*.ndpi.", 
                    required = True)
parser.add_argument("-o", "--output_img", type=str,
                    help="An output directory should be given. Try: /path_to/images/.", 
                    required = True)

# parser.add_argument("-d", "--display", help="Only shows the image on display, no masking takes place.", action="store_true")
# parser.add_argument("-s", "--suffix", help="Suffix to append to end of file, default is 'm' for thumbnail and '#' for a given level.", default="", type=str)
# parser.add_argument("-t", "--type", help="Output file type, default is png (which is slower), other options are tif.", default="png", type=str)
# parser.add_argument("-f", "--force", help="Force output even if it exists.", default=False, action="store_true")
# parser.add_argument("-v", "--verbose", help="While writing images also display image properties.", default=False, action="store_true")

args = parser.parse_args()

if not args.input_img:
    print("\nOh, computer says no! You must supply correct arguments when running a *** EntropyMasker ***!")
    print("Note that -i/--input_img and -o/--output_img are required, i.e. an input image and output image should be given. Try: IMG012.ndpi, IMG012.TIF or /path_to/images/IMG012.ndpi.\n")
    parser.print_help()
    exit()

# # FIX
# # if a type is given, the extension of the output-image is changed
# # if a suffix is given, this is also added
# fnameout=f"{Path(fname).stem}{args.suffix}.!!.{args.type if args.type[0] == '' else ''+args.type}"
# fnameout=Path(args.outdir,fnameout)
    
# # FIX
# # this will get the file with the path: os.path.splitext
# # this will get the file name: os.path.basename
# # the [0] will get the first part of the multiple parts
# fname_base = os.path.splitext(os.path.basename(fname))[0]
# fname_base_ext = os.path.splitext(os.path.basename(fname))[1]

# # FIX
# # if a directory is given, instead of a file, all the files are listed and
# # processed; if a wildcard was used (e.g. *.png) all these files are listed
# # and processed
# if len(args.input) > 1:  # bash has sent us a list of files
#     files = args.input
# else:  # user sent us a wildcard, need to use glob to find files
#     files = glob.glob(args.input[0])

# # FIX
# # if an output directory does not exist, we create it
# if not args.outdir:
# 	print("Output directory was not given, set to [",os.path.dirname(fname),"].")
# 	fname_base_dir = os.path.dirname(fname)
# else:
# 	print("Output directory was given, set to [",args.outdir,"].")
# 	fname_base_dir = args.outdir

# # FIX
# # Display the image, -d/--display
#
# # if an image is given, it is opened with OpenSlide
# fimage=openslide.OpenSlide(fname)
#
# img = fimage.associated_images["macro"] # macro will get the color thumbnail from an image
# img = np.asarray(img)[:,:, 0:3]
# img_r = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 
# print("Displaying [",fname_base,"] at path [",fname_base_dir,"] with extension [",fname_base_ext,"].")
# 
# # Let's print each dimension of the image
# print('* image dimensions (height x width in pixels):', img.shape)
# img_size = img.size/1024 # to get kilobytes
# print('* image size:', '{:,.2f}'.format(img_size), 'KB') # to get Kb
# 
# # To display our image variable, we use 'imshow'
# # The first parameter will be title shown on image window
# # The second parameter is the image variable
# # rotate the image for easy reading (https://www.geeksforgeeks.org/python-opencv-cv2-rotate-method/)
# cv2.imshow(print('Display image [',fname_base,']'), cv2.cvtColor(img_r, cv2.COLOR_RGB2BGR))
# print('(hit any key on the image to close)') # how waitKey works
# 
# # waitKey - ref: https://stackoverflow.com/questions/22274789/cv2-imshow-function-is-opening-a-window-that-always-says-not-responding-pyth
# # 'waitKey' allows us to wait for a key stroke 
# # when a image window is open
# # By leaving it blank it just waits for any key to be 
# # pressed before continuing. 
# # By placing numbers (except 0), we can specify a delay for
# # how long you keep the window open (time is in millisecs here)
# cv2.waitKey(0)
    
# function to apply the entropy mask/filter
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

# main program to apply to a given image
def main():

    print("Processing image [",args.input_img,"].")
    ORO = cv2.imread(args.input_img,0)
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

    redolbl = measure.label(np.array(mask_255),connectivity=2)
    redprops = regionprops(redolbl)

    redAreaData = []
    for r in range(len(redprops)):
        redAreaData.append(redprops[r].area)


    max_value = max(redAreaData)
    max_index = redAreaData.index(max_value)
        
    max_mask = (redolbl==(max_index+1))*255
    print("Writing entropy-based masked image at [",args.output_img,"].")
    
    # # FIX
    # if not args.force and os.path.exists(args.output_img):
    #   print(f"Skipping {output_img} as output file exists and --force is not set")
    #   continue

    # # FIX
    # if args.verbose:
    #   print("Processing [",fname,"] at level [",level,"].")
    #   print('* image dimensions (height x width in pixels):', img.shape)
    #   img_size = img.size/1024 # to get kilobytes
    #   print('* image size:', '{:,.2f}'.format(img_size), 'KB') # to get Kb
    #   cv2.imwrite(str(fnameout).replace("!!",str(level)),cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    # else:
    #   print("Writing images for [",fname,"] at level [",level,"].")
    #   cv2.imwrite(str(fnameout).replace("!!",str(level)),cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    cv2.imwrite(args.output_img, max_mask)

# start the main program
if __name__ == "__main__":
	main()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Creative Commons BY-NC-ND 4.0                                                                                   +")
print("+ Copyright (c) 2022. Yipei Song | Craig Glastonbury | Sander W. van der Laan | Clint L. Miller.                  +")
print("+                                                                                                                 +")
print("+  This is a human-readable summary of (and not a substitute for) the license.                                    +")
print("+                                                                                                                 +")
print("+  You are free to: Share, copy and redistribute the material in any medium or format. The licencor cannot revoke +")
print("+  these freedoms as long as you follow the license terms.                                                        +")
print("+                                                                                                                 +")
print("+  Under the following terms:                                                                                     +")
print("+                                                                                                                 +")
print("+  * Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were  +")
print("+                  made. You may do so in any reasonable manner, but not in any way that suggests the licensor    +")
print("+                  endorses you or your use.                                                                      +")
print("+  * NonCommercial — You may not use the material for commercial purposes.                                        +")
print("+  * NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified     +")
print("+                    material.                                                                                    +")
print("+  * No additional restrictions — You may not apply legal terms or technological measures that legally restrict   +")
print("+                                 others from doing anything the license permits.                                 +")
print("+                                                                                                                 +")
print("+  Notices: You do not have to comply with the license for elements of the material in the public domain or where +")
print("+  your use is permitted by an applicable exception or limitation. No warranties are given. The license may not   +")
print("+  give you all of the permissions necessary for your intended use. For example, other rights such as publicity,  +")
print("+  privacy, or moral rights may limit how you use the material.                                                   +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
