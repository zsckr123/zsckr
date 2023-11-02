''' a(1) = 7
a(n+1) = a(n) -3
a(2) = a(1)-3'''

def ciag(n):
    if n == 1:
        return 7
    if n > 1:
        return ciag(n-1) -3
    # return 7
print(ciag(2))