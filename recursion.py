def rec(n):
    print(n)
    if n<=1:
        return 1
    else:
        return n*rec(n-1)
rec(3)