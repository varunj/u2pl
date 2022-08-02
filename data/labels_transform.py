import glob
from os.path import exists
import cv2
import numpy as np


def find_masks_that_have_images():
     masks = []
     for filename in glob.iglob('SegmentationClassAug/480p/*/*.png', recursive=True):
          filename = filename.replace('\\', '/')
          filename = filename.replace('SegmentationClassAug/', '')
          masks.append(filename)

     masks_new = []
     for x in masks:
          imagename = x.replace('png', 'jpg')
          imagename = 'JPEGImages/' + imagename
          if exists(imagename):
               print(x.replace('.png', ''))



def change_label_class():
     for filename in glob.iglob('SegmentationClassAug/480p/*/*.png', recursive=True):
          mask = cv2.imread(filename)
          b, g, r = mask[:,:,0], mask[:,:,1], mask[:,:,2]
          b[r==128] = 15
          g[r==128] = 15
          r[r==128] = 15
          cv2.imwrite(filename, mask)


change_label_class()