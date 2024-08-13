# Lecture 9: Lambda Functions, Tuples, and Lists

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

print("apply with is_f: ", apply(is_f, 10))
print("apply with anon fn: ", apply(lambda x: x==5, 100))

# ----

def dt(n , fn):
    return fn(fn(n))

print(dt(3, lambda x: x**2))

# ----

def cc(s):
    vow = "aeiou"
    (c, v) = (0, 0)
    for char in s:
        if char in vow:
            v += 1
        else:
            c += 1
    return (v, c)

print(cc("asfho"))
print(cc("znren"))

# ----

def snp(l):
    ts= sum(l)
    tp = 1
    for num in l:
        tp *= num
    return (ts, tp)

num = [1, 2, 3, 4]
r = snp(num)
print(r)