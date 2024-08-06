import matplotlib.pyplot as plt
v0=5
g=9.81
t = linspace(0, 1, 1000)
y= v0*t - 0.5*g*t**2

largest_height = y[0]
for i in range(1, 1000):
    if [i] > largest_height:
        largest_height[i]
print ("the largest height achieved was %f m" % (largest_height))
plt.plot(x,y)
plt,xlabel('time (s)')
plt,ylabel('height (m)')
plt.show()
