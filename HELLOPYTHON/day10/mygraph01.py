import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D  


fig = plt.figure()

ax = fig.gca(projection='3d')  

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

plt.title('my 3D')

x = [0,0,0,0,0]
y = [0,1,2,3,4]
z = [1,2,1,2,1]

ax.plot(x, y, z) 


plt.show()
