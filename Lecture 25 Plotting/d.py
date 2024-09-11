import matplotlib.pyplot as plt

mon = range(1, 13, 1)
bost = [28, 32, 39, 48, 59, 68, 75, 73, 66, 54, 45, 34]
plt.plot(mon, bost, label = 'boston')
phoe = [54, 57, 61, 68, 77, 86, 91, 90, 84, 73, 61, 54]
plt.plot(mon, phoe, label = 'phoenix')
plt.title('avg. temp')
plt.xlabel('months')
plt.ylabel('degrees F')
plt.legend(loc = 'best')
plt.grid()
plt.show()