def ciag(n):
    if n == 1:
        return -10
    if n>1:
        return ciag(n-1) +9

print(ciag(5))