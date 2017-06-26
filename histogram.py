import matplotlib.pyplot as plt

population_ages=[2, 6, 9, 20, 30, 25, 34, 90, 200, 100, 45, 53, 76, 83, 23, 74, 19, 5, 7, 18, 21, 29, 33, 36, 76, 67, 100]
ids=[x for x in range(len(population_ages))]
bins=[10, 20, 30, 40, 50, 60, 70, 80, 90,100]
#plt.bar(ids, population_ages )
plt.hist(population_ages, bins, histtype='bar', rwidth=.2)
#plt.xlable('index')
#plt.ylable('age')
plt.legend()
plt.show()

