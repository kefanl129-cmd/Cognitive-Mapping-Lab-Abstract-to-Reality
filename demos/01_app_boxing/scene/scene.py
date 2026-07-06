import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(10,8))

ax=fig.add_subplot(111,projection="3d")

ax.set_xlim(-2,2)

ax.set_ylim(-2,2)

ax.set_zlim(-2,2)