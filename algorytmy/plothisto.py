import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(12345)

mu = 23.7
sigma = 7.4
x = mu + sigma * np.random.randn(int(1e6))    # generate 20 numbers

print(x)

num_bins = 50
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins, density=1)

# (add a line)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
y1= ((1 / (np.sqrt(2 * np.pi) * sigma*2)) * np.exp(-0.5 * (1 / sigma*2 * (bins - mu)) ** 2))

ax.plot(bins, y, '--')
ax.plot(bins, y1, '--')

ax.set(xlabel='data', ylabel='value (MW)', title='Nice histogram')

fig.tight_layout()
plt.show()
