# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# new a figure and set it into 3d

fig = plt.figure()
plt.rcParams["figure.figsize"] = (20, 10)
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("18×12")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
# ax.set_xlim(-50, 50, 10)
# ax.set_ylim(-50, 50, 10)
ax.set_zlim(0, 50)
ax.set_xticks(np.arange(-50, 60, 10))
ax.set_yticks(np.arange(-50, 60, 50))
# draw the figure, the color is r = read
xx = []
yy = []
zz = []
for i in range(len(order1)):
    xx.append(x[order1[i]])
    yy.append(y[order1[i]])
    zz.append(z[order1[i]])
ax.plot(xx, yy, zz, 'r-')
xx = []
yy = []
zz = []
for i in range(len(order2)):
    xx.append(x[order2[i]])
    yy.append(y[order2[i]])
    zz.append(z[order2[i]])
ax.plot(xx, yy, zz, 'g-')
xx = []
yy = []
zz = []
for i in range(len(order3)):
    xx.append(x[order3[i]])
    yy.append(y[order3[i]])
    zz.append(z[order3[i]])
ax.plot(xx, yy, zz, 'm-')
ax.scatter(x, y, z, 'o', linewidths = 5)
ax.scatter([x[start[0]], x[start[1]], x[start[2]]], [y[start[0]], y[start[1]], y[start[2]]], [z[start[0]], z[start[1]], z[start[2]]], 'yp', linewidths = 15)

elev = 65
azim = 75
ax.view_init(elev, azim)
 
# Show the figure, adjust it with the mouse
plt.show()