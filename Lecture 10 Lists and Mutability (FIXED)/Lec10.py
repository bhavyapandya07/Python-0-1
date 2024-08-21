# Lecture 10: Lists and Mutability

l1 = ['ab']
l2 = ['cd']
l3 = ['ef']
l4 = l1 + l2
l3.append(l4)
l = l1.append(l3)
print(l4)
print(l3)
print(l1)
print(l)

# ----

def list(n):
    list1 =  []
    for i in range(n+1):
        list1.append(i)
    return list1
print(list(10))

# ----

def elem(L, e):
    list = []
    for i in L:
        if i != e:
            list.append(i)
    return list

L = [1,2,3,3]
print(elem(L, 3))

# ----

def cw(s):
    l1 = s.split(' ')
    return len(l1)

s = "Hello world is the first code"
print(cw(s))

# ----

def cw(s):
    l1 = s.split(' ')
    l1.sort()
    return l1

def cw1(s):
    l2 = s.split(' ')
    l2.reverse()
    return l2

def cw2(s):
    l3 = s.split(' ')
    l4 = sorted(l3)
    return l3

s = "b c d a"
print(cw(s))
s = "b c d a"
print(cw1(s))
s = "b c d a"
print(cw2(s))

# ----

def sw(s):
    l = s.split(" ")
    return sorted(l)

l = [4,5,6]
print(l)
print(id(l))
l.append(8)
print(l)
l.clear()
print(l)
l = [4,5,6,7]
print(l)
l=[]
print(l)