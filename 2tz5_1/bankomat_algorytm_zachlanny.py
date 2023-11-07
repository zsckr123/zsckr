def ile_moneta(kwota, banknot):
    # kwota_oryg = kwota
    licznik = 0
    if kwota >= banknot:
        licznik = kwota // banknot
        # kwota = kwota - banknot * licznik
        kwota = kwota % banknot
        # print(f'{banknot} mieści się {licznik} razy w {kwota_oryg}')
    return licznik, kwota

def rozmien_kwota(kwota, lista):
    kwota_oryg = kwota
    kwota_spr = 0
    bankomat = {}
    for el in lista:
        bankomat[str(el)] = ile_moneta(kwota, el)[0]
        kwota = ile_moneta(kwota, el)[1]
    for el in bankomat.keys():
        kwota_spr += int(el) * bankomat[el]
    if kwota_spr == kwota_oryg:
        return bankomat
    return 'bledna kwota'
# print(ile_moneta(230,100))
# print(ile_moneta(120,30)[1])
print(rozmien_kwota(1240,sorted([50,100,20,10], reverse=True)))