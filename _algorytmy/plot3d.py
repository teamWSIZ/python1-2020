import math
from dataclasses import dataclass
from typing import List

import matplotlib.cm as cm
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


@dataclass
class MData:
    x: float
    y: float
    z: float


def plotdata(data: List[MData]):
    xxx, yyy, zzz = [], [], []
    mx = 0
    for c in data:
        xxx.append(c.x)
        yyy.append(c.y)
        zzz.append(c.z)
        mx = max(mx, c.z)

    ####
    fig, ax = plt.subplots(1, 1)
    fig.set_dpi(250)
    fig.set_size_inches(7, 8)
    plt.tight_layout(pad=0.09)

    cmap = cm.get_cmap(name='jet', lut=None)

    im2 = ax.tricontourf(xxx, yyy, zzz, 150, cmap=cmap, norm=plt.Normalize(vmin=0, vmax=mx), alpha=0.9)

    plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)

    cbar = plt.colorbar(im2)
    cbar.ax.set_ylabel(f'Czas wykonania')

    xspect = 1.0
    ax.set_aspect(xspect)

    plt.show()
    # plt.savefig(filename)
    # print(f'saved as {filename}')

# data = []
# for i in range(10):
#     for j in range(10):
#         data.append(MData(i * 0.1, j * 0.1, i * j))
#
# plotdata(data)
