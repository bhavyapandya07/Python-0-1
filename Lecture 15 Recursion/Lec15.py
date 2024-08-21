# Lecture 15: Recursion

def m(a, b):
    return a*b

print(m(2, 5))

# ----

def mr(a, b):
    if b == 1:
        return a
    else:
        return a + mr(a, b-1)
    
print(mr(5, 4))

# ----

def pr(n, p):
    if p == 0:
        return 1
    else:
        return n*pr(n, p-1)
    
print(pr(2, 4))