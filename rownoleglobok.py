szerokosc_wysokosc = input()
(wysokosc, szerokosc) = [int(s) for s in szerokosc_wysokosc.split()]

for rzad in range(1, wysokosc+1):
    print((rzad-1) * ' ' + szerokosc * '*')