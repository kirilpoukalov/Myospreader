import numpy as np
import os
import tifffile
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

mousedir='E:\\stellarvision\\Kiril\\A871'
savedir='D:\Science\images\stellarvision_processing\A871'
fibers=next(os.walk(mousedir))[1]
for x in fibers:
    fiber=x
    dir= mousedir + '\\' + fiber
    tiles=next(os.walk(dir))[1]
    for x in tiles:
        tile=x
        dir=mousedir + '\\' + fiber + '\\' + tile + '\\' +'AcqData'
        #make stacks from images
        os.chdir(dir)
        with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackDAPI'+'_'+fiber+'_'+tile+'.tif') as stack:
            for img_files in os.listdir(dir):
                if img_files.endswith("]_DAPI.tif"):
                    stack.save(
                        tifffile.imread(img_files), 
                        photometric='minisblack', 
                        contiguous=True
                    )
        with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackCy3'+'_'+fiber+'_'+tile+'.tif') as stack:
            for img_files in os.listdir(dir):
                if img_files.endswith("]_Cy3S.tif"):
                    stack.save(
                        tifffile.imread(img_files), 
                        photometric='minisblack', 
                        contiguous=True
                    )
        with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackFAM'+'_'+fiber+'_'+tile+'.tif') as stack:
            for img_files in os.listdir(dir):
                if img_files.endswith("]_FAMS.tif"):
                    stack.save(
                        tifffile.imread(img_files), 
                        photometric='minisblack', 
                        contiguous=True
                    )
        with tifffile.TiffWriter('D:\Science\images\stellarvision_processing\StackCy5'+'_'+fiber+'_'+tile+'.tif') as stack:
            for img_files in os.listdir(dir):
                if img_files.endswith("]_Cy5S.tif"):
                    stack.save(
                        tifffile.imread(img_files), 
                        photometric='minisblack', 
                        contiguous=True
                    )
        #make max-projection
        path = 'D:\Science\images\stellarvision_processing\StackDAPI'+'_'+fiber+'_'+tile+'.tif'
        IM = io.imread(path)
        IM_MAX= np.max(IM, axis=2)
        im = Image.fromarray(IM_MAX)
        im.save(savedir+ '\\' + 'DAPI_max'+'_'+fiber+'_'+tile+'.tif')

        path = 'D:\Science\images\stellarvision_processing\StackCy3'+'_'+fiber+'_'+tile+'.tif'
        IM = io.imread(path)
        IM_MAX= np.max(IM, axis=2)
        im = Image.fromarray(IM_MAX)
        im.save(savedir+ '\\' + 'Cy3_max'+'_'+fiber+'_'+tile+'.tif')

        path = 'D:\Science\images\stellarvision_processing\StackFAM'+'_'+fiber+'_'+tile+'.tif'
        IM = io.imread(path)
        IM_MAX= np.max(IM, axis=2)
        im = Image.fromarray(IM_MAX)
        im.save(savedir+ '\\' + 'FAM_max'+'_'+fiber+'_'+tile+'.tif')

        path = 'D:\Science\images\stellarvision_processing\StackCy5'+'_'+fiber+'_'+tile+'.tif'
        IM = io.imread(path)
        IM_MAX= np.max(IM, axis=2)
        im = Image.fromarray(IM_MAX)
        im.save(savedir+ '\\' + 'Cy5_max'+'_'+fiber+'_'+tile+'.tif')

        #crop dapi max projection
        image = Image.open(savedir+ '\\' + 'DAPI_max'+'_'+fiber+'_'+tile+'.tif')
        cropped_image = image.crop((512,512,1536,1536))
        cropped_image.save(savedir+ '\\' + 'DAPI_max_cropped'+'_'+fiber+'_'+tile+'.tif')

        os.remove('D:\Science\images\stellarvision_processing\StackDAPI'+'_'+fiber+'_'+tile+'.tif')
        os.remove('D:\Science\images\stellarvision_processing\StackFAM'+'_'+fiber+'_'+tile+'.tif')
        os.remove('D:\Science\images\stellarvision_processing\StackCy3'+'_'+fiber+'_'+tile+'.tif')
        os.remove('D:\Science\images\stellarvision_processing\StackCy5'+'_'+fiber+'_'+tile+'.tif')
