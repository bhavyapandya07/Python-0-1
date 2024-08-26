# Lecture 19: Inheritance

class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def setname(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}"

def abc(l1, l2):
    l3 = []
    for i in range(len(l1)):
        age = l1[i]
        name = l2[i]
        a = Animal(age)
        a.setname(name)
        l3.append(a)
    return l3
        
l1 = [2, 5, 1]
l2 = ['fish', 'cat', 'dog']
animal = abc(l1, l2)
for i in animal:
    print(i)

# -----

