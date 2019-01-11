import numpy as np
from matplotlib import cm
from matplotlib import rcParams
import matplotlib.pyplot as plt
#rcParams['text.latex.unicode']=True
plt.rc('font', family='serif')
plt.rc('font',size=11)
plt.rc('axes',labelsize=11)
# Data
x       =   np.linspace(1 , 5  , 50)
y       =   np.logspace(5 , 10 , 50)
z       =   np.linspace(5 , 10 , 50)
size    =   np.geomspace(20 , 400 , len(x))

# Create a figure
fig     =   plt.figure(figsize = (8,4)) # Figure size
# Add subplots
ax     =   fig.add_subplot(121)
ax1    =   fig.add_subplot(122) 
# Plot a line with markers
ax.plot(x , y , 'k-',label = 'Curva 1') #, markevery = 2 ,linewidth = 1.5,
                                        #marker = 's', markersize = 6, markeredgewidth = 1.25,
                                         #markeredgecolor = 'k', markerfacecolor = '1', label = 'Curva 1')
ax1.plot(x , y , 'k-', markevery = 2 ,
         linewidth = 1.5, marker = 's',
         markersize = 6, markeredgewidth = 1.25,
         markeredgecolor = 'k', markerfacecolor = '1',
         label = 'Curva 1')
# Scatter plot with different size and different color
s = ax.scatter(x , y , s = size, marker = 'o' , c = z, cmap = cm.jet,
               linewidths = 1.25, edgecolors = 'k')
### Title
ax.set_title    ('Plot - example')
### Label X axis
ax.set_xlabel   ('Label X axis')
### Label Y axis
ax.set_ylabel   ('Label Y axis')
### Legend 
ax.legend       (numpoints = 1,
                 loc = 'upper left',
                 fontsize = 9,
                 frameon = False)
### Position of thicks
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
c_bar = fig.colorbar(s, ax = ax)
c_bar.set_ticks     (np.linspace(min(z),max(z),3))
c_bar.set_ticklabels(['min', 'med', 'max'])
c_bar.set_label     ('$T_{grafica}$', labelpad = 10, y = 0.5)
### Remove right spine 
ax.spines['right'].set_visible(False)
### Remove top spine
ax.spines['top'].set_visible(False)
### 
ax.set_xticks(np.linspace(min(x),max(x),3))
ax.set_yticks(np.linspace(min(y),max(y),3))
ax.set_xticklabels(['A','B','C'])
ax.set_yticklabels(np.linspace(10,20,3))
#ax.grid()
ay = ax.twinx()
ay.semilogy(x , y , 'k-', markevery = 2 ,
         marker = 's', markersize = 6, markeredgewidth = 1.25,
         markeredgecolor = 'k', markerfacecolor = '1', label = 'Curva 2')
ay.legend       (numpoints = 1,
                 loc = 'center',
                 fontsize = 9,
                 frameon = False)
fig.tight_layout()
plt.savefig('figura.svg')
plt.show()

