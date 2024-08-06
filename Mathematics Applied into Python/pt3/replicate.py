def replicate(n,x):
    if n>=0:
        a=[]
        for i in x:
            for b in range(0,n):
                a.append(i)

    return a

print(replicate(7, []))
print(replicate(0, ['a', 'b', 'c']))
print(replicate(3, ['a']))
print(replicate(3, ['a', 'b', 'c']))
print(replicate(4, [1, 2, 3, 4]))
