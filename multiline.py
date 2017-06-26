import numpy as np
import matplotlib.pyplot as plt

#Create a figure and axes with room for the table
fig = plt.figure()
ax = plt.axes([0.2, 0.2, 0.7, 0.6])

#Create labels for the rows and columns as tuples
colLabels = ('36', '40', '44', '48', '149', '153', '157', '161', '165')
rowLabels = ('UDL DL', 'UDP UL', 'TCP DL', 'TCP UL')

#Table data as a numpy array
tableData = np.array([[  36.7128,  37.684,   38.283,  48.425,   32.839, 36.424, 34.440, 31.642, 35.710],
        [  36.7128,  37.684,   38.283,  48.425,   32.839, 36.424, 34.440, 31.642, 35.710],
        [  36.7128,  37.684,   38.283,  48.425,   32.839, 36.424, 34.440, 31.642, 35.710],
        [  36.7128,  37.684,   38.283,  48.425,   32.839, 36.424, 34.440, 31.642, 35.710]])

#Get the current color cycle as a list, then reset the cycle to be at the beginning
colors = []     
while True:
    colors.append(ax._get_lines.color_cycle.next())
    if colors[0] == colors[-1] and len(colors)>1:
        colors.pop(-1)
        break

for i in xrange(len(colors)-1):
    ax._get_lines.color_cycle.next()

#Show the table
table = plt.table(cellText=tableData,
                  rowLabels=rowLabels, rowColours=colors,
                  colLabels=colLabels,
                  loc='bottom')

#Make some line plots
x = np.linspace(0,10,100)                  
ax.plot(x,np.sin(x))
ax.plot(x,-1*np.sin(x))
ax.plot(x,np.cos(x))
ax.plot(x,-1*np.cos(x))

#Turn off x-axis ticks and show the plot              
plt.xticks([])
plt.show()
