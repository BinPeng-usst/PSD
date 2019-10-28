import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm

##读入数据
#file=open('c:/users/2013-fwq/onedrive - usst.edu.cn/桌面/publication/pywork/3/0－通道 0.dat')
Temp=pd.read_table('c:/users/2013-fwq/onedrive - usst.edu.cn/桌面/publication/pywork/3/0－通道 0.dat',header=None,skiprows=1,sep='\+')
Y=Temp.values
X=np.linspace(0,Y.size*(1/200),Y.size)

##分析计算


##曲线图
#pl.figure(1,figsize=(6,6), dpi= 100, facecolor='w', edgecolor='k')
#aix=pl.subplot(111)
#pl.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9,hspace=0,wspace=0)
#pl.title("Acceleration",fontdict={'family': 'Times New Roman', 'size' : 16})
#aix.tick_params(axis='both',direction='in')

#pl.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size' : 16})
#pl.xlim=(0,Y.size*(1/200))
#pl.xticks(fontproperties='Times New Roman', size = 16)

#pl.ylabel('ACC',fontdict={'family' : 'Times New Roman', 'size' : 16})
#pl.ylim=(0,Y.size*(1/200))
#pl.yticks(fontproperties='Times New Roman', size = 16)

#pl.plot(X,Y,'g--^',linewidth=2,markersize=1)

#pl.savefig('./1.pdf',dpi=300)
#pl.show()
###

##曲面图
fig = pl.figure(1,figsize=(6,6), dpi= 100, facecolor='w', edgecolor='k')
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)

# Customize the x,y z axis.
pl.xlabel('Time',fontdict={'family' : 'Times New Roman', 'size' : 16})
pl.xlim=(0,Y.size*(1/200))
pl.xticks(fontproperties='Times New Roman', size = 16)

pl.ylabel('ACC',fontdict={'family' : 'Times New Roman', 'size' : 16})
pl.ylim=(0,Y.size*(1/200))
pl.yticks(fontproperties='Times New Roman', size = 16)

ax.set_zlabel('ACC',fontdict={'family' : 'Times New Roman', 'size' : 16})
ax.set_zlim(-1.01, 1.01)
ax.set_zticklabels([],fontdict={'family' : 'Times New Roman', 'size' : 16})

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

pl.show()



