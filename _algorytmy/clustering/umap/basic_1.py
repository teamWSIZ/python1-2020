from itertools import islice, cycle

import numpy as np
import matplotlib.pyplot as plt
from _algorytmy.clustering.utils import ts
import joblib

import seaborn as sns  # statistical data visualization
import umap
from sklearn import datasets, cluster

sns.set(style='dark', context='poster', rc={'figure.figsize': (14, 10)})

np.random.seed(42)

n_samples = 2000
dataset = datasets.make_blobs(n_samples=n_samples, n_features=10, centers=3, cluster_std=[0.8, 0.3, 9.8])
X, y = dataset
data = X

# fit = umap.UMAP(n_neighbors=48, min_dist=0.1, random_state=3)  # random_state gives same resutls for every run
fit = umap.UMAP(n_neighbors=148, min_dist=0.1)  # random_state gives same resutls for every run

# print('umap fit')
# t_start = ts()
# fit.fit(data)
# t_end = ts()
# print(f'umap fit (construction) took {t_end - t_start:.3f}s')
#
# t_start = ts()
# print('umap (projection) started..')
# u = fit.transform(data)
# t_end = ts()
# print(f'umap projection took {t_end - t_start:.3f}s')  # very fast


def save_umap(reducer):
    joblib.dump(reducer, 'umap_reducer.sav')


def load_umap():
    return joblib.load('umap_reducer.sav')


# save_umap(fit)
reducer = load_umap()
u = reducer.transform(data)


colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                     '#f781bf', '#a65628', '#984ea3',
                                     '#999999', '#e41a1c', '#dede00']), int(max(y) + 1))))
colors = np.append(colors, ["#000000"])  # nieprzypisane do cluster-ów

# algo = cluster.MiniBatchKMeans(n_clusters=3)
# algo.fit(X)
# y_pred = algo.labels_.astype(int)
# plt.scatter(X[:, 0], X[:, 1], s=6, color=colors[y_pred])

plt.scatter(u[:, 0], u[:, 1], c=colors[y], s=4)

plt.title('UMAP projection')
plt.show()
