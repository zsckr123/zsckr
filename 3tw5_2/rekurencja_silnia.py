def silnia(n):
    # if n == 1:
    #     return 1
    if n > 1:
        return silnia(n-1) * n
    return 1

''' silnia(5) = 5 * silnia(4)
ale silnia(4) = 4 * silnia(3)
ale silnia(3) = 3 * silnia(2)
ale silnia(2) = 2 * silnia(1)
zatem zbieramy silnia(1) = 1'''

print(silnia(5))