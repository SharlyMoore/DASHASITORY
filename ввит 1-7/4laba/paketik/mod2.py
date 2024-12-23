def F(n, k):
    c = 0
    for i in range(n, k+1):
        c += 1
    if c >= n + k:
        return c
    else:
        return n + k