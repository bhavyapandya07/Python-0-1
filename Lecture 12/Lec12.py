# Lecture 12: List Comprehension, Functions as Objects, Testing, and Debugging (FIXED)

print([len (x) for x in ['xy', 'abcd', 7, '4.0'] if type(x) == str])

# ----

def ip(x):
    t = x[:]
    print(t, x)
    t.reverse()
    print(t, x)
    if t == x:
        return True
    else:
        return False

print(ip(list('abcba')))
print(ip(list('ab')))