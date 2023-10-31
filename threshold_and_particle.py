import numpy as np
import glob
import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage.color
import skimage.filters
from scipy import ndimage
from PIL import Image
from scipy import ndimage as nd
import os
import pandas as pd
from scipy.spatial.distance import cdist

imagedir='D:\\Science\\images\\stellarvision_processing\\A871'
outputdir='D:\\Science\\images\\stellarvision_processing\\output\\A871'

imagefiles=os.listdir(imagedir)
for x in imagefiles:
    DAPI_file=x
    if DAPI_file.startswith("DAPI_max_cropped"):
        imagedapi = iio.imread(imagedir+'\\'+DAPI_file)
        blurred_image = skimage.filters.gaussian(imagedapi, sigma=1.0)
        # perform automatic thresholding
        t = skimage.filters.threshold_otsu(blurred_image)
        print("Found automatic threshold t = {}.".format(t))
        # create a binary mask with the threshold found by Otsu's method
        binary_mask = blurred_image > t
        if np.count_nonzero(binary_mask)>50000:
            imagedapi = iio.imread(imagedir+'\\'+DAPI_file)
            blurred_image = skimage.filters.gaussian(imagedapi, sigma=1.0)
            # perform automatic thresholding
            t = skimage.filters.threshold_yen(blurred_image)
            print("Found automatic threshold t = {}.".format(t))
            # create a binary mask with the threshold found by yen method
            binary_mask = blurred_image > t
        if np.count_nonzero(binary_mask)<50000:

            for x in imagefiles:
                FAM_file=x
                if FAM_file.startswith("FAM_max_Fiber"):
                    if FAM_file.endswith(DAPI_file[-10:]):
                        imageFAM = iio.imread(imagedir+'\\'+FAM_file)


                        selection = imageFAM
                        selection[~binary_mask] = 0


                        nuclei = []

                        def analyze(x):
                            xmin = x.min()
                            xmax = x.max()
                            xmean = x.mean()
                            xcount = x.sum()/x.mean()
                            nuclei.append({'min': xmin,
                                        'max': xmax,
                                        'mean': xmean,
                                        'pixel_count': xcount})
                            return 1

                        a=np.asarray(selection)
                        lbl, nlbl = nd.label(a)
                        lbls = np.arange(1, nlbl + 1)
                        nd.labeled_comprehension(a, lbl, lbls, analyze, float, -1)

                        df = pd.DataFrame(nuclei)
                        df.to_csv(outputdir+"\\"+FAM_file+"_nuclei"+".txt")

                        labeled_array,numpatches = ndimage.label(selection)

                        def feature_dist(input):
                            I, J = np.nonzero(labeled_array)
                            labels = labeled_array[I,J]
                            coords = np.column_stack((I,J))
                            sorter = np.argsort(labels)
                            labels = labels[sorter]
                            coords = coords[sorter]

                            nonzero_vs_feat = np.zeros(shape=(len(coords), numpatches))
                            b=-1
                            print(len(coords))

                            for x in coords:
                                b=b+1
                                x=np.array(x)
                                x=x.reshape(1,-1)
                                sq_dists = cdist(x, coords, 'sqeuclidean')
                                start_idx = np.flatnonzero(np.r_[1, np.diff(labels)])
                                nonzero_vs_feat_entry = np.minimum.reduceat(sq_dists, start_idx, axis=1)
                                nonzero_vs_feat[b]=nonzero_vs_feat_entry

                            feat_vs_feat = np.minimum.reduceat(nonzero_vs_feat, start_idx, axis=0)
                            return np.sqrt(feat_vs_feat)

                        distancearray= feature_dist(labeled_array)
                        df = pd.DataFrame(distancearray)
                        df.to_csv(outputdir+"\\"+FAM_file+"_Distances"+".txt")

            for x in imagefiles:
                Cy5_file=x
                if Cy5_file.startswith("Cy5_max_Fiber"):
                    if Cy5_file.endswith(DAPI_file[-10:]):
                        imageCy5 = iio.imread(imagedir+'\\'+Cy5_file)


                        selection = imageCy5
                        selection[~binary_mask] = 0


                        nuclei = []

                        def analyze(x):
                            xmin = x.min()
                            xmax = x.max()
                            xmean = x.mean()
                            xcount = x.sum()/x.mean()
                            nuclei.append({'min': xmin,
                                        'max': xmax,
                                        'mean': xmean,
                                        'pixel_count': xcount})
                            return 1

                        a=np.asarray(selection)
                        lbl, nlbl = nd.label(a)
                        lbls = np.arange(1, nlbl + 1)
                        nd.labeled_comprehension(a, lbl, lbls, analyze, float, -1)

                        df = pd.DataFrame(nuclei)
                        df.to_csv(outputdir+"\\"+Cy5_file+"_nuclei"+".txt")