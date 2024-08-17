def rall(l, e):
    lcopy = l[:]
    l.clear()
    for i in lcopy:
        if e != i:
            l.append(i)
    
lin = [1,2,2,3]
rall(lin, 2)
print(lin)