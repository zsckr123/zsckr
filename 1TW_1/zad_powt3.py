def tekst():
    wyraz = input('Podaj dowolny ciąg znakowy')
    lista = []
    for i in wyraz[::-1]:
        # print(ord(i))
        lista.append(ord(i))
    return lista
print(tekst())