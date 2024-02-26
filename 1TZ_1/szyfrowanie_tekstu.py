# lista = [1,'s']
# print(lista)
# print(ord('a'))
lista_zaszyfrowana =[]
wyraz = input('Podaj wyraz do zaszyfrowania')
for znak in wyraz:
    lista_zaszyfrowana.append(ord(znak))
print(lista_zaszyfrowana)
