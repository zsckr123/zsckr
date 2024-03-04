def tekst():
    wyraz = input('Podaj dowolny ciąg znakowy')
    lista = []
    for i in wyraz[3:]:
        lista.append(ord(i))
    return lista
print(tekst())