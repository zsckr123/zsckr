'''
d(1) = -10
d(n+1) = d(n) +9
'''

def ciag(n):
    # if n == 1:
    #     return -10
    if n >1:
        return ciag(n-1) + 9
    return 1