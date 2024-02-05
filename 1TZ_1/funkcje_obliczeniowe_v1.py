'''
y=ax+b
f(x) = ax +b
f(-1) = 2x+1 = 2 * (-1) +1
'''

def liniowa_1(x):
    return x, 2 * x + 1

print(f' Wartość funkcji dla argumentu '
      f'{liniowa_1(-2)[0]}: {liniowa_1(-2)[1]}')

