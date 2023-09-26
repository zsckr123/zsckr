''' Dzielimy liczba1 przez liczba2 '''
while True:
    liczba1 = int(input('podaj pierwszą liczbę: '))
    liczba2 = int(input('podaj drugą liczbę: '))
    if liczba2 == 0:
          print("Brak nwd")
    else:
        while liczba2 > 0:
            reszta = liczba1 % liczba2  # %  dzielenie modulo; reszta z dzielenie
            liczba1 = liczba2
            liczba2 = reszta
    print("najwiekszy wspolny dzielnik to:",liczba1)
    key = input('Nacisnij x zeby zakończyć')
    if key == 'x':
        break