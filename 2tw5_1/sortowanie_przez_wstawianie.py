import time
def sort_insert(A):
    start = time.time()
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    stop = time.time()
    delta = stop - start
    print(f'Czas sortowania {delta}')
    return A

lista = [-2,3,4,5,-100, 200, -10000, -2000]
lista1 = [x for x in range(1,10000)]
print(sort_insert(lista1))