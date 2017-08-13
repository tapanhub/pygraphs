import matplotlib.pyplot as plt

x = range(10)
y = range(10)

'''
for row in ax:
    for col in row:
        col.plot(x, y)

plt.show()
'''

fig, ax = plt.subplots(nrows=2,ncols=2)

for i in range ( 2*2 ):
	plt.subplot(2,2,i)
	plt.plot(x, y, label="plot(%d)" % (i))
	plt.xlabel("index_x=%d" % (i))
	plt.ylabel("index_y=%d" % (i))
	plt.grid(True)
	plt.legend()

plt.show()
