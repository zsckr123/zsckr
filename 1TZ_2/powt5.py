def tekst():
    wyraz = input('Podaj dowolny ciąg znakowy')
    lista = []
    for i in wyraz[1::2]:
        print(i)
        lista.append(ord(i))
    return lista
print(tekst())