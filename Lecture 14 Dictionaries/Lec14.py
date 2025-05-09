# Lecture 14: Dictionaries

def fg(g, s):
    ln = []
    for e in s:
        g = g[e]
        ln.append(g)
    return ln

d = {'ana':'b', 'john':'a'}
print(fg(d, ['john']))

# ----

def f(ld, k):
    for d in ld:
        if k in d:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(f([d1, d2, d3], 2))
print(f([d1, d2, d3], 25))

# ----

def cm(d):
    count = 0
    for v,k in d.items():
        if v==k:
            count = count +1
    return count

d = {1:2, 3:4, 5:6}
print(cm(d))
d = {1:2, 'a':'a', 5:5}
print(cm(d))