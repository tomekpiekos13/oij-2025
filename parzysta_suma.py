linia = input()
(liczba1, liczba2, liczba3) = [int(n) for n in linia.split()]
if (liczba1 + liczba2)% 2 == 0:
    print('TAK')
    print(f'{liczba1} {liczba2}')
elif (liczba2 + liczba3)%2 == 0:
    print('TAK')
    print(f'{liczba3} {liczba2}')
elif (liczba1 + liczba3)%2 == 0:
    print('TAK')
    print(f'{liczba3} {liczba1}')