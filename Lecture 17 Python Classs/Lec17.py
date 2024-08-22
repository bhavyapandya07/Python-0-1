# Lecture 17: Python Classes

class Coordinate:
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

c = Coordinate(3, 4)
o = Coordinate(0, 0)

print(c.x)
print(o.x)

# ----

class code:
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def d(self, other):
        xdiff = (self.x - other.x)**2
        ydiff = (self.y - other.y)**2
        return (xdiff + ydiff)**0.5

c = code(3, 4)
o = code(0, 0)

print(c.d(o))