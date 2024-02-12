def dlugosc(tekst1, tekst2):
    if tekst1 > tekst2:
        return f'{tekst1} jest dłuższy {tekst2}'
    elif  tekst2 > tekst1:
        return f'{tekst2} jest dłuższy {tekst1}'
    return f'napisy są jednakowej dlugości'

print(dlugosc('komiks','komiks_'))