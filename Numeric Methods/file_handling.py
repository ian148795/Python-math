filename='tmp.dat'
infile= open(filename, 'r')
line= infile.readline()

x=[]
y=[]
for line in infile:
    words = line.split()
    x.append(float(words[0]))
    y.append(float(words[1]))
infile.close()
from math import log
def f(y):
    return log(y)
for i in range (len(y)):
    y[i] = f(y[i])

filename = 'temp_out.dat'
outfile = open(filename, 'w')
outfile.write('# x and y coordinates\n')
for xi, yi in zip(x,y):
    outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()
