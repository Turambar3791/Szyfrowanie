def sortowanie(tab):
    for i in range(len(tab)):
        for j in range(i):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
    return tab

plik = "abracadabra" #open("wiadomosc.txt").read()
plikIlosc = open("wynik1.txt", "w")
plikKody = open("wynik2.txt", "w")

alfabet = "qwertyuiopasdfghjklzxcvbnm"
tab = []

for i in alfabet:
    if i in plik:
        plikIlosc.write(f'{i} {str(plik.count(i))}\n')
        tab.append([plik.count(i), i, None])

tab.sort()
print(tab)

for i in range(len(tab)-1):
    tab = sortowanie(tab)
    lewy = tab[-2]
    prawy = tab[-1]
    temp = [lewy, prawy]
    suma = lewy[0] + prawy[0]
    tab.remove(lewy)
    tab.remove(prawy)
    tab.append([suma, 'polaczenie', temp])

print(tab)

stos = [(tab[0], "")]
kody = []

while stos:
    aktualnyStos = stos[-1][0]
    prefiks = stos[-1][1]
    del stos[-1]
    if aktualnyStos[2] is None:
        kody.append([aktualnyStos[1], prefiks])
    else:
        lewy = aktualnyStos[2][0]
        prawy = aktualnyStos[2][1]
        stos.append((lewy, prefiks + '0'))
        stos.append((prawy, prefiks + '1'))
print(kody)





