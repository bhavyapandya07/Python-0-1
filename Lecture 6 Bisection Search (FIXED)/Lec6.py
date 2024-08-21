# Lecture 6: Bisection Search (FIXED)

x = 36
e = 1
l = 0
h = x
g = (h + l)/2
while abs(g**2 - x) >= e:
    if g**2 < x:
        l = g
    else:
        h = g
    g = (h + l)/2.0
print(g, "is close to square root of", x)

# ----

x = 0.5
e = 0.01
if x >= 1:
    l = 1
    h = x
else:
    l = x
    h = 1
g = (h + l) / 2
while abs(g**2 - x) >= e:
    print(l, h, g)
    if g**2 < x:
        l = g
    else:
        h = g
    g = (h + l) / 2
print(g, "is close to the square root of", x)

# ----

c = 27
e = 0.01
l = 0
h = c
g = (h + l)/2
while abs(g**3 - c) >= e:
    if g**3 < c:
        l = g
    else:
        h = g
    g = (h + l)/2.0
print(g, "is close to cube root of", c)

