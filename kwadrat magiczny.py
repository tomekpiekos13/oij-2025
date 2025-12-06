kwadrat = []

slowo = input()
kwadrat.append(slowo)

for _ in range(1, len(slowo)):
    kwadrat.append(input())

def kwadrat_pionowo(kwadrat):
    k = [[] for _ in kwadrat]
    for i in range(len(kwadrat)):
        for j in range(len(kwadrat)):
            k[i] += kwadrat[j][i]
    return k
jest_magiczny = True
wyrazy_dobre = [[] for _ in kwadrat]
pionowo = kwadrat_pionowo(kwadrat)

for i in range(len(kwadrat)):
    for j in range(len(kwadrat[i])):
        litera_k = kwadrat[i][j]
        litera_p = pionowo[i][j]
        if litera_k == litera_p or litera_k == '?' or litera_p == '?':
            if litera_k == '?' and litera_p != '?':
                litera_k = litera_p
            if litera_p == '?' and litera_k != '?':
                litera_p = litera_k
            if litera_k == '?' and litera_p == '?':
                litera_k = 'Z'
                litera_p = 'Z' 
            wyrazy_dobre[i] += litera_k
        else:
            jest_magiczny = False


if jest_magiczny:
    for slowo in wyrazy_dobre:
        print("".join(slowo))
else:
    print('NIE')