'''
def ciag(n):
    if n == 1:
        oblicz -10
    if n >1 :
        oblicz
'''

def ciag(n):
    # if n == 1:
    #     return -10
    if n >1:
        return ciag(n-1) + 9
    return 1