import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin
 
fig, ax = plt.subplots()
line, = plt.plot([], [], 'o', color='g', label='line')

edge = 20
v0=10
g=9.8
a=30

tp=v0/g
lmax=v0**2*0.85/g
hmax=v0**2*sin(a)**2/2*g

print ('Время:', tp)
print ('Расстояние:', lmax)
print ('Высота:', hmax)
 
plt.axis('equal')

ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
 
x, y = [], []

def animate(frame):
    t = frame
    xn=v0*t
    yn=v0*t-g*t**2/2
    x.append(xn)
    y.append(yn)
    line.set_data(x, y)

ani = animation.FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 10, 0.1),
                        interval=30)


ani.save('my_anim.gif')