import matplotlib.pyplot as plt

x=[20,30,40,34]
y=[45,55,66,77]
x2=[24,34,44,38]
y2=[35,25,86,27]

plt.bar(x,y, label='first', color='r')
plt.bar(x2,y2, label='second', color='b')

plt.legend()
plt.show()
