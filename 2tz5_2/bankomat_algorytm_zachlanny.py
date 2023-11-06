def ile_moneta(kwota, banknot):
    licznik = 0
    if kwota >= banknot:
        licznik = kwota // banknot
        kwota = kwota - banknot * licznik
    return licznik, kwota


def rozmien_kwota(kwota, lista):
    # kwota =102
    # lista = [5,2]
    bankomat = {}
    for el in lista:
        bankomat[str(el)] = ile_moneta(kwota, el)[0]
        kwota = ile_moneta(kwota, el)[1]
    return bankomat

print(rozmien_kwota(110,[100,50,20,10]))
