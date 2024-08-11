# Lecture 4: Loops over Strings, Guess-and-Check, and Binary

n = 0
for i in range(10):
    if i&2==0:
        n += 1
print(n)   

# ----

s ="shajfkghuwgacbh"
s2 = ""
for char in s:
    if char not in s2:
        s2 = s2 + char
print(len(s2))

# ----

s = 7
for i in range(1, 11):
    if i == s:
        print("you got the number")
        break
    else:
        print("you failed to guess the number")

# ----

x = 0
for i in range(10):
    x += 0.1
    print(x == 1)
    print(x, "==", 10*0.1)

# ----

n = int(input("type a num: "))
r = ''
if n == 0:
    r = '0'
else:
    while n > 0:
        r = str(n%2) + r
        n = n//2
print(r)