def ciag(n):
    if n > 1:
        return ciag(n-1) + 9
    return -10

print(ciag(5))