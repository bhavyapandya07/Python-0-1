# Lecture 18: More Python Class Methods

class circle(object):
    def __init__(self, center, radius):
        if type(center) != circle:
            raise ValueError
        if type(radius) != int:
            raise ValueError
        self.center = center
        self.radius = radius

center = circle(2, 2)
mycircle = circle(center, 2)
mycricle = circle(2, 2)
mycricle = circle(center, 'two')

# ----

class simple(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def getinverse(self):
        return self.denom/self.num
    def getinvert(self):
        newd = self.num
        newn = self.denom
        self.num = newn
        self.denom = newd
    def plus(self):
        return self.denom + self.num
    def times(self):
        return self.denom * self.num 

f1 = simple(3, 4)
print(f1.getinverse())

f1.getinvert()
print(f1.num, f1.denom)

print(f1.plus())

print(f1.times())