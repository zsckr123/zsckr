def ciag(n):
    if n == 2:
        return 2
    if n >= 3:
        return ciag(n - 2) / ciag(n - 1)
    return 1

for i in range(1,6):
    print(ciag(i))
