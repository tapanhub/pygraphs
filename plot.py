from __future__ import division
import matplotlib.pyplot as plt

x=[0, 1, 2, 3]
y=[2, 7, 8, 20]
x2=[0, 1, 2, 3]
y2=[1, 8, 3, 2]

plt.plot(x,y, label='tcp')
plt.plot(x2,y2, label='udp')
plt.title('time throughput graph')
plt.xlabel('time (s)')
plt.ylabel('bytes transmitted from server')
plt.grid(True)
plt.legend()

plt.show()
