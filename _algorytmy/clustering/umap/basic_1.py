from itertools import islice, cycle

import numpy as np
import matplotlib.pyplot as plt
from _algorytmy.clustering.utils import ts
import joblib

import seaborn as sns  # statistical data visualization
import umap
from sklearn import datasets, cluster

sns.set(style='dark', context='poster', rc={'figure.figsize': (14, 10)})

"""
Przykład pokazujący jak dla pewnego zbioru danych wielowymiarowych (tu stworzonych przez make_blobs)
uruchomić na tych danych analizę UMAP tak, by zmapować te dane do dwóch (lub innej, ale małej liczby) wymiarów, 
i jak wyniki potem odzyskać i wykorzystywać. 

Uwaga: UMAP to wykorzystywany jest w formie "unsupervised", czyli kompletnie nic nie wie
a priori o asociacjach między danymi. 

"""


def save_umap(red):
    """Pozwala zapisać sformowany/dofitowany UMAP"""
    joblib.dump(red, 'umap_reducer.sav')


def load_umap():
    """Pozwala wczytać sformowany/dofitowany UMAP"""
    return joblib.load('umap_reducer.sav')


# tworzenie danych
np.random.seed(42)
n_samples = 200
dataset = datasets.make_blobs(n_samples=n_samples, n_features=10, centers=2, cluster_std=[4.5, 4.8])
X, y = dataset
data = X  # [[0,0,1,2],[0.2,0.3,1,0],[..],.....]

# tworzenie reducera UMAP
# Uwaga: po tym kroku instancja jest ciągle "raw" -- "niesformatowana".
reducer = umap.UMAP(n_neighbors=45, min_dist=0.1)  # random_state gives same resutls for every run


# uruchomienie formatowania/fit-owania UMAP na danych `data`
# po tym kroku

# print('umap fitting to given data')
# reducer.fit(data)


# ↓↓ by ten krok działał, wcześniej musi powstać obiekt "reducer", i być wykonane "reducer.fit(data)"
# save_umap(reducer)
reducer = load_umap()  # wczytanie pełnego obiektu UMAP z pliku
u = reducer.transform(data)

colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                     '#f781bf', '#a65628', '#984ea3',
                                     '#999999', '#e41a1c', '#dede00']), int(max(y) + 1))))
colors = np.append(colors, ["#000000"])  # nieprzypisane do cluster-ów

# Rysowanie obrazu/projekcji z UMAP
plt.scatter(u[:, 0], u[:, 1], c=colors[y], s=4)
plt.title('Projekcja UMAP na dwa wymiary')
plt.savefig("blobs_umap.svg")
# plt.show()

# Rysowanie czystych danych w projekcji na wymiary 0,1
algo = cluster.MiniBatchKMeans(n_clusters=3)
algo.fit(X)
y_pred = algo.labels_.astype(int)

plt.clf()
plt.scatter(X[:, 0], X[:, 1], s=6, color=colors[y_pred])
plt.title('Czyste dane w projekcji na wymiary {0,1} + lekka analiza cluster-ów')
plt.savefig("blobs_raw.svg")
# plt.show()
