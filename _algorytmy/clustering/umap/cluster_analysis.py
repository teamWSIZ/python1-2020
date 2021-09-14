from itertools import islice, cycle

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns  # statistical data visualization
import umap
from sklearn import datasets, cluster

sns.set(style='dark', context='poster', rc={'figure.figsize': (14, 10)})

np.random.seed(42)

n_samples = 4000
# dataset = datasets.make_swiss_roll(n_samples=n_samples, random_state=2)
dataset = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.15)  # dwa kółka

# dataset = datasets.make_blobs(n_samples=n_samples, n_features=10, centers=3, random_state=2,
#                               cluster_std=[0.8, 0.7, 0.8])
X, y = dataset

# data = np.random.rand(10, 4)
data = X

# algo = cluster.MiniBatchKMeans(n_clusters=2)
# algo.fit(X)
# y_pred = algo.labels_.astype(int)


fit = umap.UMAP(n_neighbors=48, min_dist=0.1)
u = fit.fit_transform(data)

colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                     '#f781bf', '#a65628', '#984ea3',
                                     '#999999', '#e41a1c', '#dede00']), int(max(y) + 1))))

colors = np.append(colors, ["#000000"])  # nieprzypisane do cluster-ów

# plt.scatter(X[:, 0], X[:, 1], s=6, color=colors[y_pred])

plt.scatter(u[:, 0], u[:, 1], c=colors[y], s=4)

# plt.title('UMAP random')
plt.show()
