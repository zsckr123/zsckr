''' 5 poczatkowych wyrazow ciagu
a(n+1) =a(n)+n, a(1)=1 '''
def ciag(n):
    if n>1:
        return ciag(n-1) + n
    return 1

print(ciag(6))