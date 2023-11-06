def ile_moneta(kwota, banknot):
    licznik = 0
    if kwota >= banknot:
        licznik = kwota // banknot
        # kwota = kwota - banknot * licznik
        kwota = kwota % banknot
    return licznik, kwota

def rozmien_kwota(kwota, lista):
    bankomat = {}
    for el in lista:
        bankomat[str(el)] = ile_moneta(kwota, el)[0]
        kwota = ile_moneta(kwota, el)[1]
    return bankomat
# print(ile_moneta(120,30))
# print(ile_moneta(120,30)[1])
print(rozmien_kwota(1240,[100,50,20]))