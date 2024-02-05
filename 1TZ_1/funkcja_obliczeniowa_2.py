'''
y=a x + b
'''

a = float(input('Podaj współcznnik a:'))
b = float(input('Podaj współcznnik b:'))

def liniowa_1(x):
    return x, a * x + b

print(f' Wartość funkcji dla argumentu '
      f'{liniowa_1(-2)[0]}: {liniowa_1(-2)[1]}')
