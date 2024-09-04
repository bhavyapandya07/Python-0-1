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