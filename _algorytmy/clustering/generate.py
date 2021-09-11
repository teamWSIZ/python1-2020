from sklearn import datasets

n_samples = 20
dataset = datasets.make_blobs(n_samples=n_samples, n_features=10, centers=4, random_state=2,
                              cluster_std=[0.2,0.2,0.5,0.7])

X, y = dataset
print(X)
print(y)