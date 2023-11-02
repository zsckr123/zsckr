''' a(1)=1
 a(n+1) = a(n) +n
 a(2) =2
 a(3) = a(2) +2'''

def ciag(n):
    # if n == 1:
    #     return 1
    if n > 1:
        return ciag(n-1) + (n-1)
    return 1


print(ciag(2))
