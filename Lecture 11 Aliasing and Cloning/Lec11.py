# Lecture 11: Aliasing and Cloning

def rall(l, e):
    lcopy = l[:]
    l.clear()
    for i in lcopy:
        if e != i:
            l.append(i)
    
lin = [1,2,2,3]
rall(lin, 2)
print(lin)

# ----

def rall(l, e):
    lcopy = l[:]
    l.clear()
    for i in lcopy:
        if i % 2 == 0:  
            l.append(i)

lin = [1, 2, 222, 3, 434, 5, 69, 75, 88, 9, 10]
rall(lin, 2)
print(lin)

# ----

def rall(l, e):
    for elem in l:
        if elem == e:
            l.remove(e)

l = [1,2,2,2]
rall(l, 2)
print(l)