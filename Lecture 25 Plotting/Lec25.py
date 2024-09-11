import matplotlib.pyplot as plt

nv = []
lin = []
quad = []
cub = []
expo = []

for n in range(0, 30):
    nv.append(n)
    lin.append(n)
    quad.append(n**2)
    cub.append(n**3)
    expo.append(1.5**n)

plt.plot(nv, lin)
plt.plot(nv, quad)
plt.plot(nv, cub)
# plt.plot(nv, expo)
# plt.scatter(nv, expo)
# plt.bar(nv, expo)
plt.show()

#----

import matplotlib.pyplot as plt

test = list(range(112))

testv = [x**2 for x in test]

# plt.plot(test, testv)
plt.scatter(test, testv)
plt.xlabel('Test Values')
plt.ylabel('Squared Values')
plt.title('Test Values vs. Their Squares')
plt.show()

#----

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