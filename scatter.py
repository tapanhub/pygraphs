import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[ 34, 45,1,23,67,98,0, ]

plt.scatter(x, y, label='test', color='r', marker='x', s=30)
plt.title(' scatter plot')
plt.legend()
plt.show()
