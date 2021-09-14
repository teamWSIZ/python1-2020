from sklearn import datasets
from sklearn.neighbors import kneighbors_graph

from _algorytmy.clustering.utils import ts

n_samples = 10 ** 5
dataset = datasets.make_blobs(n_samples=n_samples, n_features=10, centers=4, random_state=2,
                              cluster_std=[0.2, 0.2, 0.5, 0.7])

X, y = dataset
print('creating graph...')
st = ts()
A = kneighbors_graph(X, n_neighbors=2, mode='connectivity', include_self=False)
en = ts()
print(f'.. done in {en-st:.3f}s')

a_dok = A.todok()
print(len(a_dok.keys()))