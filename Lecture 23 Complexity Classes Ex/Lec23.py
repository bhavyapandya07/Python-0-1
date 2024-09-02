# Lecture 23: Complexity Classes Examples

l = [1, 2, 3, 4]

def gs(l):
    if len(l) == 0:
        return [[]]
    extra = l[-1:]
    small = gs(l[:-1]) 
    new = []
    for smaller in small:
        new.append(smaller + extra)
    return small + new
subsets = gs(l)
subsets = [[0] if s == [] else s for s in subsets]
subsets.sort(key=lambda x: (len(x), x))

print(subsets)

# ----

n = 83
n = 4271
def da(n):
    ans = 0
    s = str(n)
    for c in s[::-1]:
        ans += int(c)
    return ans