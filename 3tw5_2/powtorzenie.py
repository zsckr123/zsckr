''' Instrukcja warunkowa'''
#
# liczba1 = float(input('Podaj liczbe pierwszą'))
# liczba2 = float(input('Podaj liczbe drugą'))
#
# if liczba1 > liczba2:
#     print(f'Liczba {liczba1} jest większa od {liczba2}')
# elif liczba1 < liczba2:
#     print(f'Liczba {liczba2} jest większa od {liczba1}')
# else:
#     print('Podane liczby są identyczne')

''' Instrukcja pętli'''

# for i in range(10,3,-1):
#     print(i)
''' Lista'''
lista = [1,2,3,4,'a','b','c']
# print(lista[2::-2])
# for el in lista:
#     print(el)
#
for i in range(0,len(lista),2):
     print(lista[i])