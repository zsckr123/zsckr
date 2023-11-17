# def ciag(n):
#     if n==1:
#         return 2
#     if n>1:
#         return ciag(n-1)+1

def ciag(n):
    if n == 1:
        return 1
    if n > 1:
        return ciag(n-1)+(-2)**(n-1)
print(ciag(5))
        