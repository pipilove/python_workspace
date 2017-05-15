#!/usr/bin/env python
# coding=gbk
"""
__title__ = '绘制圆形和椭圆'
__author__ = 'pi'
__mtime__ = '2014.10.11'
"""
from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
cir1 = Circle(xy = (0.0, 0.0), radius=2, alpha=0.5)
ax.add_patch(ell1)
ax.add_patch(cir1)

x, y = 0, 0
ax.plot(x, y, 'ro')

plt.axis('scaled')
# ax.set_xlim(-4, 4)
# ax.set_ylim(-4, 4)
plt.axis('equal')   #changes limits of x_new or y axis so that equal increments of x_new and y have the same length

plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = y = np.arange(-4, 4, 0.1)
x, y = np.meshgrid(x,y)
plt.contour(x, y, x**2 + y**2, [9])     #x_new**2 + y**2 = 9 的圆形

plt.axis('scaled')
plt.show()
