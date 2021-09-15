"""
UMAP on the Galaxy10SDSS dataset
---------------------------------------------------------

This is an example of using UMAP on the Galaxy10SDSS
dataset. The goal of this example is largely to
demonstrate the use of supervised learning as an
effective tool for visualizing and reducing complex data.
In addition, hdbscan is used to classify the processed
data.
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt
from PIL import Image

import umap
import os

# from sklearn.model_selection import train_test_split
import math
import requests

# libraries for clustering
# import hdbscan
import sklearn.cluster as cluster
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

if not os.path.isfile("Galaxy10.h5"):
    url = "http://astro.utoronto.ca/~bovy/Galaxy10/Galaxy10.h5"
    print('downloading data from astro.utoronto.ca/~bovy')
    r = requests.get(url, allow_redirects=True)
    open("Galaxy10.h5", "wb").write(r.content)

# To get the images and labels from file
with h5py.File("Galaxy10.h5", "r") as F:
    images = np.array(F["images"])
    labels = np.array(F["ans"])

print('data loaded..')
n_train = 1000
n_test = 10000
n_offset = 1000
flat_size = 69 * 69 * 3

X_train = np.empty([n_train, flat_size], dtype=np.float64)  # 69 * 69 * 3
y_train = np.empty([n_train], dtype=np.float64)
X_test = np.empty([n_test, flat_size], dtype=np.float64)
y_test = np.empty([n_test], dtype=np.float64)

# Get a subset of the data

for i in range(n_train):
    X_train[i, :] = np.array(np.ndarray.flatten(images[i, :, :, :]), dtype=np.float64)
    y_train[i] = labels[i]

for i in range(n_test):
    X_test[i, :] = np.array(np.ndarray.flatten(images[n_offset + i, :, :, :]), dtype=np.float64)
    y_test[i] = labels[n_offset + i]


def show_image(imgdata):
    print(imgdata.shape)
    img = Image.fromarray(imgdata, 'RGB')
    # img.save('gg.png')
    img.show()


for i in range(5):
    show_image(images[i])
    print(labels[i])


# Plot distribution - as bar plot
classes, frequency = np.unique(y_train, return_counts=True)
fig = plt.figure(1, figsize=(4, 4))  # factory method
plt.clf()
plt.bar(classes, frequency)
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.title("Data Subset")
plt.savefig("galaxy10_subset.svg")

# 2D Embedding
# UMAP
reducer = umap.UMAP(n_components=2, n_neighbors=40, random_state=42, transform_seed=42, verbose=False)
reducer.reducer(X_train)

print(f'X_train shape: {X_train.shape}')  # (217, 14283)
galaxy10_umap = reducer.transform(X_train)  # umap-reduced dataset

fig = plt.figure(1, figsize=(4, 4))
plt.clf()
plt.scatter(
    galaxy10_umap[:, 0],
    galaxy10_umap[:, 1],
    c=y_train,
    cmap=plt.cm.nipy_spectral,
    edgecolor="k",
    label=y_train,
)
plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap.svg")

#
# ### UMAP - Supervised

# get a UMAP reducer first..
reducer = umap.UMAP(n_components=2, n_neighbors=15, random_state=42, transform_seed=42, verbose=False)
reducer.reducer(X_train, y_train)

galaxy10_umap_supervised = reducer.transform(X_train)

fig = plt.figure(1, figsize=(8, 8))
plt.clf()
plt.scatter(
    galaxy10_umap_supervised[:, 0],
    galaxy10_umap_supervised[:, 1],
    c=y_train,
    cmap=plt.cm.nipy_spectral,
    edgecolor="k",
    label=y_train,
)
plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap_supervised.svg")

#
#
# ### UMAP - Supervised prediction
print(f'X_test shape: {X_test.shape}')  # (500, 14283)
galaxy10_umap_supervised_prediction = reducer.transform(X_test)

fig = plt.figure(1, figsize=(8, 8))
plt.clf()
plt.scatter(
    galaxy10_umap_supervised_prediction[:, 0],
    galaxy10_umap_supervised_prediction[:, 1],
    c=y_test,
    cmap=plt.cm.nipy_spectral,
    edgecolor='none',
    s=2,
    label=y_test
)
plt.colorbar(boundaries=np.arange(11) - 0.5).set_ticks(np.arange(10))
plt.savefig("galaxy10_2D_umap_supervised_prediction.svg")

# cluster the data
