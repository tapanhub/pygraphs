import matplotlib.pyplot as plt

days = [ 1, 2, 3, 4, 5]
sleeping =[5, 6, 4, 8,6]
eating = [1, 1, 2, 2, 1]
working=[7,8, 7, 9, 10]
playing = [1, 1, 2, 3, 2]

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'b', 'g', 'r'])

plt.xlable('x')
plt.ylable('y')
plt.title('Stack plot')
plt.legend()
plt.show()

