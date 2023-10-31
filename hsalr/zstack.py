import numpy as np
import os
import tifffile
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

#make stacks from images
dir = 'D:\Science\images\stellarvision_processing\AcqData'
os.chdir(dir)
with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackDAPI.tif') as stack:
   for img_files in os.listdir(dir):
    if img_files.endswith("DAPI.tif"):
        stack.save(
            tifffile.imread(img_files), 
            photometric='minisblack', 
            contiguous=True
        )
with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackCy3.tif') as stack:
   for img_files in os.listdir(dir):
    if img_files.endswith("Cy3S.tif"):
        stack.save(
            tifffile.imread(img_files), 
            photometric='minisblack', 
            contiguous=True
        )
with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackFAM.tif') as stack:
   for img_files in os.listdir(dir):
    if img_files.endswith("FAMS.tif"):
        stack.save(
            tifffile.imread(img_files), 
            photometric='minisblack', 
            contiguous=True
        )
with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackCy5.tif') as stack:
   for img_files in os.listdir(dir):
    if img_files.endswith("Cy5S.tif"):
        stack.save(
            tifffile.imread(img_files), 
            photometric='minisblack', 
            contiguous=True
        )

#make max-projection
path = "D:\Science\images\stellarvision_processing\StackDAPI.tif"
IM = io.imread(path)
IM_MAX= np.max(IM, axis=2)
im = Image.fromarray(IM_MAX)
im.save("D:\Science\images\stellarvision_processing\DAPI_max.tif")

path = "D:\Science\images\stellarvision_processing\StackFAM.tif"
IM = io.imread(path)
IM_MAX= np.max(IM, axis=2)
im = Image.fromarray(IM_MAX)
im.save("D:\Science\images\stellarvision_processing\FAM_max.tif")

path = "D:\Science\images\stellarvision_processing\StackCy5.tif"
IM = io.imread(path)
IM_MAX= np.max(IM, axis=2)
im = Image.fromarray(IM_MAX)
im.save("D:\Science\images\stellarvision_processing\Cy5_max.tif")

path = "D:\Science\images\stellarvision_processing\StackCy3.tif"
IM = io.imread(path)
IM_MAX= np.max(IM, axis=2)
im = Image.fromarray(IM_MAX)
im.save("D:\Science\images\stellarvision_processing\Cy3_max.tif")

#crop dapi max projection
image = Image.open("D:\Science\images\stellarvision_processing\DAPI_max.tif")
cropped_image = image.crop((512,512,1536,1536))
cropped_image.save("D:\Science\images\stellarvision_processing\DAPI_max_cropped.tif")
