import numpy as np
import pandas as pd
from skimage.io import imread, imsave
from sklearn.cluster import MiniBatchKMeans
import os, urllib.request


IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Seawall_Vancouver.jpg/320px-Seawall_Vancouver.jpg"
IMAGE_FILENAME = 'cluster-input.jpg'
OUTPUT_FILENAME = 'cluster-output.png'
N_COLOURS = 32


# get image and read pixel data
if not os.path.isfile(IMAGE_FILENAME):
    with urllib.request.urlopen(IMAGE_URL) as imgdata, open(IMAGE_FILENAME, 'wb') as imgfile:
        imgfile.write(imgdata.read())

imgdata = imread(IMAGE_FILENAME)
shape = imgdata.shape
imgdata = imgdata.reshape(-1, 3)

# find clusters of colours (MiniBatchKMeans instead of KMeans because of data size & computation time)
clusterer = MiniBatchKMeans(N_COLOURS, batch_size=10000)
clusterer.fit(imgdata)
pixel_cluster = clusterer.predict(imgdata)

# map each pixel back to the cluster centre (an RGB value)
colours = clusterer.cluster_centers_.astype(np.uint8)
imgdata = colours[pixel_cluster, :].reshape(shape)
imsave(OUTPUT_FILENAME, imgdata)