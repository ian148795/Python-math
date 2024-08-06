from numpy import linspace
v0 = 4.5
g = 9.81
t = linspace (0, 1, 1000)
y = v0*t - 0.5*g*t**2
#find where the ball hits y=0
i=0

while y[i] >=0:
    i +=1
#now, y[i-1]>0 and y[i]<0 so lets take the middle point
#in time as the aproximation for when the ball hits h=0
print( "y=0 at", 0.5*(t[i-1] + t[i]))
#we plot  the path again just for comparison
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.plot(t, 0*t, 'g--')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()
