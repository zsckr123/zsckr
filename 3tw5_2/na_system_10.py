liczba_w_innym_systemie = [1,1,0,0]
podstawa = int(input('Podaj podstawę'))
liczba_10 = 0
potega = 0
for i in liczba_w_innym_systemie[::-1]:
    liczba_10 += i * podstawa ** potega
    potega +=1
print(f'Liczba w systemie dziesiątkowym: {liczba_10}')