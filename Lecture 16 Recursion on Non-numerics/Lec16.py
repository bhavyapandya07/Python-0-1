# Lecture 16: Recursion on Non-numerics

def tr(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + tr(l[1:])

test = [30, 40, 50]
print(tr(test))

# ----

def tlr(l):
    if len(l) == 1:
        return len(l[0])
    else:
        return tlr(l[1:]) + len(l[0])
    
t = ['ab', 'c', 'defgh']
print(tlr(t))

# ----

def ll(l, e):
    if len(l) == 1:
        return e in l[0]
    else:
        f = l[0]
        if e in f:
            return True
        else:
            return ll(l[1:], e)

t = [[1,2], [3,4], [5,6]]
print(ll(t, 6))
