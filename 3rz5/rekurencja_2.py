def ciag(n):
    if n == 2:
        return 2
    if n > 2:
        return ciag(n - 1) / ciag(n - 2)
    return 1
for i in range(1,20):
    print(ciag(i))
