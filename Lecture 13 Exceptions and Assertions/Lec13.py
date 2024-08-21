# Lecture 13: Exceptions and Assertions

def sd(s):
    t = 0
    for char in s:
        if char in '0123456789':
            v = int(char)
            t += v
    return t
print(sd('123abc'))

# ----

def sd(s):
    t = 0
    for char in s:
        try:
            v = int(char)
            t += v
        except:
            print('error', char)
    return t
print(sd('123abc'))

# ----

def pd(ln, ld):
    l = []
    if 0 in ld:
        raise ValueError
    for i in range(len(ln)):
        try:
            l.append(ln[i]/ld[i])
        except:
            raise ValueError('ggs')
    return l

l1 = [4,5,6]
l2 = [1,2,3]
print(pd(l1, l2))

# ----

def pd(ln, ld):
    assert len(ln) == len(ld), 'Lists must have the same length'
    assert len(ln) != 0 and len(ld) != 0, 'Lists cannot be empty'
    
    l = []
    for i in range(len(ln)):
        try:
            l.append(ln[i] / ld[i])
        except ZeroDivisionError:
            raise ValueError('Division by zero encountered')
    return l

l1 = [4, 5, 6]
l2 = [1, 2, 3]

result = pd(l1, l2)
print(result)