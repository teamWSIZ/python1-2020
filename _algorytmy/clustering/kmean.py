from itertools import islice, cycle

from sklearn import cluster, datasets, mixture
import matplotlib.pyplot as plt
from sklearn.neighbors import kneighbors_graph
import numpy as np
from sklearn.preprocessing import StandardScaler

from _algorytmy.clustering.utils import ts

np.random.seed(2)

n_samples = 10 ** 2

# n features == liczba "wymiarów" próbki

# ###### generowanie losowych próbek
# https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py


# dataset = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)    # dwa kółka
# dataset = datasets.make_blobs(n_samples=n_samples, n_features=8, random_state=1, cluster_std=1.1)  # populacje
# dataset = datasets.make_blobs(n_samples=n_samples, n_features=2, centers=3, random_state=2,cluster_std=0.2)
dataset = datasets.make_blobs(n_samples=n_samples, n_features=4, centers=4, random_state=1,
                              cluster_std=[0.2,0.2,0.5,0.7])
# dataset = datasets.make_swiss_roll(n_samples=n_samples, random_state=2)

print(dataset)

# [0.4, 0.3, 0.4, 0.4]
# print(dataset)
print(type(dataset[0]))

plt.figure(figsize=(9 * 2 + 3, 13))

default_base = {'quantile': .3,
                'eps': .3,
                'damping': .9,
                'preference': -200,
                'n_neighbors': 10,
                'n_clusters': 3,
                'min_samples': 20,
                'xi': 0.05,
                'min_cluster_size': 0.1}

X, y = dataset  # X : array-like of shape (n_samples, n_features)

# X = StandardScaler().fit_transform(X)  #computes mean&std and transforms data to (0,1)
# X[1] *= 10
# X = StandardScaler().fit_transform(X)  #computes mean&std and transforms data to (0,1)


st = ts()
connectivity = kneighbors_graph(X, n_neighbors=90, include_self=False)

# make connectivity symmetric
connectivity = 0.5 * (connectivity + connectivity.T)
en = ts()
print(f'connectivity done in {en - st:.3}s')
# wybór alogrytmu klasteryzacji

# algo = cluster.MiniBatchKMeans(n_clusters=12)
algo = cluster.AgglomerativeClustering(n_clusters=4, linkage='ward', connectivity=connectivity)
# algo = cluster.OPTICS(min_samples=20, xi=0.05, min_cluster_size=0.1)

st = ts()
algo.fit(X)
en = ts()
print(f'fit done in {en - st:.3}s')

if hasattr(algo, 'labels_'):
    y_pred = algo.labels_.astype(int)
else:
    y_pred = algo.predict(X)

colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                     '#f781bf', '#a65628', '#984ea3',
                                     '#999999', '#e41a1c', '#dede00']), int(max(y_pred) + 1))))
colors = np.append(colors, ["#000000"])  # nieprzypisane do cluster-ów

plt.subplot(1, 1, 1)  # rows, cols, plot position r * COLS + col

# print(X[:, 0])  # np; extract x[0]

plt.scatter(X[:, 0], X[:, 1], s=6, color=colors[y_pred])  # s=point size
plt.show()

# todo.. UMAP....