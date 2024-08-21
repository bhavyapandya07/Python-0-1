# Lecture 5: Floats and Approximation Methods

x = int(input("Type any Number: "))
e = 0.01
ng = 0
g = 0.0
i = 0.01
while abs(g**2 - x) >= e and g**2 <= x:
    g += i
    ng += 1
print(f"ng = {ng}")
print(f"{g} is close to square root of {x}")