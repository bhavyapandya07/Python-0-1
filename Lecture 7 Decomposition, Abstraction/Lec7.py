# Lecture 7: Decomposition, Abstraction, and Functions

def is_e(i):
    if i%2 == 0:
        return True
    else:
        return False

# ----

def is_e(i):
    if i%2 == 0:
        return True
    else:
        return False
print(is_e(3))
print(is_e(4))

# ----

def div_by(n, d):
    if d%n == 0:
        return True
    else:
        return False
print(div_by(10, 3))
print(div_by(195, 13))