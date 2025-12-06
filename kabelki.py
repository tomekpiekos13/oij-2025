from collections import namedtuple

Gniazdo = namedtuple('Gniazdo', ['x', 'y'])
Kabelek = namedtuple('Kabelek', ['start', 'koniec'])

def czy_sie_przecinaja(kabelek_1: Kabelek, kabelek_2: Kabelek):
    if kabelek_1.start in kabelek_2 or kabelek_1.koniec in kabelek_2:
        return True
    
    def pdrwz(a, b, c):
        return (c.y-a.y) * (b.x-a.x) > (b.y-a.y) * (c.x-a.x)
    
    def przecinaja_sie(a, b, c, d):
        return pdrwz(a, c, d) != pdrwz(b, c, d) and pdrwz(a, b, c) != pdrwz(a, b, d)
    
    return przecinaja_sie(kabelek_1.start, kabelek_1.koniec, kabelek_2.start, kabelek_2.koniec)

def czy_sie_przecina_z_innymi(kabelek, kabelki):
    for k in kabelki:
        if czy_sie_przecinaja(kabelek, k):
            return True
    return False

def znajdz_kabelki_bez_przecinania(liczba_kabelkow, kombinacje):
    for i in range(len(kombinacje)):
        kabelki_bez_przecinania = []
        kabelki_bez_przecinania.append(kombinacje[i])
        for j in range(i, len(kombinacje)):
            kabelek = kombinacje[j]
            if not czy_sie_przecina_z_innymi(kabelek, kabelki_bez_przecinania):
                kabelki_bez_przecinania.append(kabelek)
            if len(kabelki_bez_przecinania) == liczba_kabelkow:
                return kabelki_bez_przecinania    
         

if __name__ == "__main__":
    liczba_kabelkow = int(input())
    dane = [input().strip() for _ in range(2 * liczba_kabelkow)] 

    gniazda = [g.split() for g in dane]

    gniazda = [Gniazdo(int(g[0]), int(g[1])) for g in gniazda]

    # przypadek najprostszy
    if  liczba_kabelkow == 1:
        print(f"{gniazda[0].x} {gniazda[0].y} {gniazda[1].x} {gniazda[1].y}")
    else:
        kombinacje = []
        for gniazdo_1 in gniazda:
            for gniazdo_2 in gniazda[1:]:
                if gniazdo_2 != gniazdo_1 and not (gniazdo_2, gniazdo_1) in kombinacje:
                    kombinacje.append(Kabelek(gniazdo_1, gniazdo_2))

        wynik = znajdz_kabelki_bez_przecinania(liczba_kabelkow, kombinacje)    

        for k in wynik:
            print(f"{k.start.x} {k.start.y} {k.koniec.x} {k.koniec.y}")