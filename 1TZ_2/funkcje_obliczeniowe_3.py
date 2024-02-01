'''
Czy liczba jest parzysta
'''

def parzystosc(x):
    if x % 2 ==0:
        return f'Liczba {x} jest parzysta'
    else:
        return f'Liczba {x} jest nieparzysta'

print(parzystosc(5))