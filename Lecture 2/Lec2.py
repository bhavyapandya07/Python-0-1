# Lecture 2: Strings, Input/Output, and Branching

b = ":"
c = ")"
a = b * 2
s1 = b + 2 * c
h = "3"
s2 = (b + c) * int(h)

# ----

s = 'abc'
print(s[0])
print(s[-1])

# ----

w = "adjbwuibaui"
print(w[4:7])
print(w[4:7:2])
print(w[:])
print(w[::-1])
print(w[::3])
print(w[-1:-4:-1])
print(w[9:4:-2])
print(w[3:len(w)-1])
print(w[4:0:-1])
print(w[6:3])
print(w)

# ----

a = input("Type a verb: ")
print(5*a)
print(' '.join([a] * 5))
print("I can", a, "better than you")

# ----

s = 5
g = int(input("guess a number: "))
print(g == s)

# ----

x = int(input("enter num1: "))
y = int(input("enter num1: "))
if x == y:
    print(good)
else:
    print(bad)

# ----

    x = int(input("enter num1: "))
y = int(input("enter num1: "))
if x == y:
    print(x, "is same as", y)
else:
    print(x, "is not same as", y)

# ----

    s = 5
g = int(input("guess a num: "))
if g < s:
    print(g, "is too low then", s)
elif g == s:
    print(g, "is same as", s)
else: 
    g >= s
    print(g, "is too high", s)