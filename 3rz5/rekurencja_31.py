def ciag(n):
    if n > 1:
        return ciag(n - 1) - (n - 1) ** 2 + 3
    return 3

print(ciag(5))
