import matplotlib.pyplot as plt

slices = [ 29, 10, 20, 80 ]
activities = [ 'sleeping', 'eating', 'working', 'playing' ]
c= ['k', 'm', 'w', 'g' ]


plt.pie(slices, 
	labels=activities, 
	colors=c, 
	shadow=True,
	explode=(0,0.1, 0.2,0),
	autopct=('%1.1f%%'))
#plt.pie(slices, labels=activities, colors=c, startangle=0)

plt.title('pie chart')

plt.show()

