# Lecture 3: Iteration

where = input("go left or right?")
while where == "right":
    where = input("go left or right?")
print("you got out!")

# ----

# while True:
#     print("nooo")

# ----

a = 0
where = input("go left or right?")
while where == "right":
    a = a + 1
    if a > 2:
        print("please type left :()")
    where = input("go left or right?")
print("you got it!")

# ----

a = 0
for i in range (10):
    a += i
    print(a)

# ----

a = 0
s = 3
e = 5
for i in range(s, e+1):
    a += i
    print(a)