def dopelnij(napis, znak, liczba_znakow):
    wynik = napis
    for i in range(len(napis), liczba_znakow):
        wynik += znak
    return wynik


def liczba_znakow_z_dopelnieniem(napis, liczba_kolumn):
    dlugosc = len(napis)
    liczba_znakow_ostatni_wiersz = dlugosc % liczba_kolumn
    if liczba_znakow_ostatni_wiersz != 0:
        dlugosc += (liczba_kolumn - liczba_znakow_ostatni_wiersz)
    return dlugosc


def zaszyfruj(napis, liczba_kolumn):
    wynik = ""
    napis = dopelnij(napis, "_", liczba_znakow_z_dopelnieniem(napis, liczba_kolumn))
    dlugosc = len(napis)
    akt_pozycja = 0
    for i in range(dlugosc):
        wynik += napis[akt_pozycja]
        akt_pozycja += liczba_kolumn
        if akt_pozycja >= dlugosc:
            akt_pozycja -= (dlugosc - 1)
    return wynik


def deszyfruj(napis, liczba_kolumn):
    wynik = ""
    for i in range(liczba_kolumn):
        wynik = zaszyfruj(napis, liczba_kolumn)
        napis = wynik
    wynik = ""
    for i in napis:
        if i != "_":
            wynik += i
    return wynik


print(zaszyfruj("ALAMAKOTA", 4))
print(deszyfruj("AAALK_AO_MT_", 4))
