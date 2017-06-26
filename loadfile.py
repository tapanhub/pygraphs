import matplotlib.pyplot as plt
import numpy as np

# part 1
'''
import csv

x = []
y = []

with open('example.txt') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
'''
#part 2
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='plot from file')
plt.xlabel('x')
plt.xlabel('y')
plt.title('plot from file')
plt.legend()
plt.show()
