import numpy as np
import matplotlib.pylab as plt


plt.style.use('seaborn-white')


plt.rc('font', family='serif')
plt.rc('font',size=10)
plt.rc('axes',labelsize=10)



# Funcion solo para generar datos
def T(theta):
    a = 1.5
    b = 2
    return a*np.sin(theta*b)   

# Funcion solo para generar datos 
def R(r):
    c = 2
    d = 1.6
    return c*np.cos(r*d)

def contourPlot(colormap,N):
    fig, ax = plt.subplots(figsize = (5,3),subplot_kw=dict(projection='polar'))
    s = ax.contourf(t, r, Parameter, levels=N, cmap=colormap,linewidth=0.8)
    ay = fig.add_axes([0.8, 0.1, 0.03, 0.8])
    c_bar = fig.colorbar(s, cax = ay)
    fig.tight_layout()
    return 
radius = np.arange(0,4.01,0.01)
theta = np.radians(np.arange(0,361,1))
r,t= np.meshgrid(radius, theta) # Datos en forma de grid
Parameter = T(t)*R(r) # tercera variable, en tu caso la presion.



contourPlot('viridis',100)
contourPlot('magma',100)
contourPlot('jet',100)
contourPlot('coolwarm',100)
contourPlot('gist_rainbow',100)
plt.show()




