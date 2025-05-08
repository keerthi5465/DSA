def counts(n):
    f = [1,2,3,4,5,4,3,2]
    p = 0
    if n > 8:
        p = (n % 8) - 1
    else:
        return f[n - 1]
    return f[p]

k = 26
c = counts(k)
print(c)

     