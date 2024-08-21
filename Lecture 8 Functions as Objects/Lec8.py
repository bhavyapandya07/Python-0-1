# Lecture 8: Functions as Objects

def add(x, y):
    return x+y
def mult(x, y):
    print(x*y)

add(1, 2)
print(add(2, 3))
mult(2, 3)
print(mult(2, 2))

# ----

def is_tri(n):
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return (True)
    return (False)

print(is_tri(4))
print(is_tri(6))
print(is_tri(1))

# ----

def suma(a, b):
    sumo = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            sumo += i
    return sumo

# ----

def calc(op, x, y):
    return op(x ,y)
def div(a, b):
    if b != 0:
        return a/b
    print("Denom was 0.")
res = calc(div, 2, 0)
print(res)

# ----

def apply(crit, n):
    count = 0
    for i in range (n+1):
        if crit(i):
            count += 1
    return count

def is_e(x):
    return x%2==0
def is_f(x):
    return x==5

print(is_e)
print(is_f)
hm = apply(is_f, 10)
print(hm)