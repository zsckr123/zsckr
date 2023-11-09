def ciag(n):
    if n == 1:
        return 3
    if n>1:
        return ciag(n-1) - n**2 +3

print(ciag(5))