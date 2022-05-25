import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#45 seconds

resolution = width, height = 2*(3000,)

xmin, xmax = -2.25, 1
xwidth = xmax - xmin

ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

x,y = np.ogrid[xmin:xmax:1j*width, ymin:ymax:1j*height]

complex_plane = (x + 1j*y).T

def f(z, c):
    return z**2 + c

N = 1000
max_m = 10

ns = np.zeros((height,width))
counter = 0

z = np.zeros(shape = (height, width), dtype = 'complex')

for i in range(N):
    T = abs(z) <= max_m
    z[T] = f(z[T], complex_plane[T])
    ns[T] += 1
    counter += 1
    print(f'{counter}/{N}')

julia = 1-np.sqrt(ns/N)

fig = plt.figure()

ax = fig.add_subplot(111)
im = ax.pcolormesh(julia, cmap = cm.jet)

cbar = fig.colorbar(ax=ax, mappable=im, orientation='vertical')

xtick_labels = np.linspace(xmin, xmax, int((xwidth)*2), endpoint=True)
ax.set_xticks([(x-xmin)*(width)/(xwidth) for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

ytick_labels = np.linspace(ymin, ymax, int((yheight)*2), endpoint=True)
ax.set_yticks([(y-ymin)*(height)/(yheight) for y in ytick_labels])
ax.set_yticklabels(['{:.1f}i'.format(ytick) for ytick in ytick_labels])

ax.set_xlabel('Re')
ax.set_ylabel('Im')

plt.subplots_adjust(left=0.23, right=0.843, top=0.967, bottom=0.06)

plt.show()