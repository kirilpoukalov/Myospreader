import numpy as np
import glob
import matplotlib.pyplot as plt
import ipympl
import imageio.v3 as iio
import skimage.color
import skimage.filters
%matplotlib ipympl

shapes01 = iio.imread('D:\Science\images\stellarvision_processing\A860\DAPI_max_cropped_Fiber 1_1_1.tif')

fig, ax = plt.subplots()
plt.imshow(shapes01)
