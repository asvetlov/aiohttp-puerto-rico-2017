from math import log
import numpy as np
import matplotlib.pyplot as plt

K = 500

x = np.arange(500, 10000, 1)
y2 = np.log(x) - log(x[0])
y1 = np.log(x)*0.9 - log(x[0])
y3 = x/K + y2[0] - x[0]/K/2


fig, ax = plt.subplots()
ax.plot(x, y1, label='WSGI')
ax.plot(x, y2, label='Async')


ax.legend(loc='upper left', fontsize='x-large')


ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

# plt.show()

plt.savefig('no_io.png')


fig, ax = plt.subplots()
ax.plot(x, y3, label='WSGI')
ax.plot(x, y2, label='Async')


ax.legend(loc='upper left', fontsize='x-large')

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

plt.savefig('io.png')
