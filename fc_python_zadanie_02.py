# FC – PYTHON – ZADANIE 2 – Pętle i argumenty w konsoli
#
# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać,
# a następnie wymaga podania wagi dla każdej z nich.
#
# Na koniec działania program powinien wyświetlić w podsumowaniu:
# 1. Liczbę paczek wysłanych.
# 2. Liczbę kilogramów wysłanych.
# 3. Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych.
# 4. Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik.
#
# Restrykcje:
# – Waga elementów musi być z przedziału od 1 do 10 kg.
# – Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# – W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# – W przypadku podania wagi elementu mniejszej od 1 kg lub większej od 10 kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.
#
# ###### Przykład 1:
# – Ilość elementów: 2
# – Wagi elementów: 7, 9
#
# Podsumowanie:
# – Wysłano 1 paczkę (7+9)
# – Wysłano 16 kg
# – Suma pustych kilogramów: 4 kg
# – Najwięcej pustych kilogramów ma paczka 1 (4 kg)
#
# ###### Przykład 2:
# – Ilość elementów: 6
# – Wagi elementów: 3, 6, 5, 8, 2, 3
#
# Podsumowanie:
# – Wysłano 2 paczki (3+6+5, 8+2+3)
# – Wysłano 27 kg
# – Suma pustych kilogramów: 13 kg
# – Najwięcej pustych kilogramów ma paczka 2 (7 kg)
#
# ###### Przykład 3:
# – Ilość elementów: 8
# – Wagi elementów: 7, 14
#
# Podsumowanie:
# – Wysłano 1 paczkę (7)
# – Wysłano 7 kg
# – Suma pustych kilogramów: 13 kg
# – Najwięcej pustych kilogramów ma paczka 1


# liczba_wyslanych_kilogramow = 0
# liczba_wyslanych_paczek = 1
# maksymalna_wielkosc_paczki = 20
# aktualna_wielkosc_paczki = 0
# najlzejsza_paczka = 1
# waga_najlzejszej_paczki = 0
# najciezsz_paczka = 1

# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(0, ilosc_elementow): # Zapis range(0, ilosc_paczek) jest tym samym co range(ilosc_paczek)
#     waga_elementu = float(input('Podaj wagę elementu: '))
#     if 1 > rozmiar_paczki > 20:
#         print('Paczka może ważyć od 1 do 10 kg.')
#         break
#     liczba_wyslanych_kilogramow += rozmiar_paczki
#     if rozmiar_paczki + aktualna_wielkosc_paczki <= 20:
#         aktualna_wielkosc_paczki += rozmiar_paczki
#     else:
#         if aktualna_wielkosc_paczki < waga_najlzejszej_paczki:
#             najlzejsza_paczka = liczba_wyslanych_paczek # Oznacza też, na której paczce aktualnie jesteśmy.
#             waga_najlzejszej_paczki = aktualna_wielkosc_paczki
#         aktualna_wielkosc_paczki = rozmiar_paczki
#         liczba_wyslanych_paczek += 1

# if 0 > rozmiar_elementu > 10:
#     break
# liczba_wyslanych_kilogramow += rozmiar_paczki
# if rozmiar_paczki + aktualna_wielkosc_paczki <= 20:
#     aktualna_wielkosc_paczki += rozmiar_paczki

# print(f'Wysłane PACZKI ważyły {liczba_wyslanych_kilogramow } kg.')
#
# print(f'Wysłano {liczba_wyslanych_paczek} PACZEK.')
# print(f'Suma pustych kilogramów: {liczba_wyslanych_paczek * 20 - liczba_wyslanych_kilogramow} kg.')
# print(f'Najwięcej pustych kilogramów na PACZKA {najlzejsza_paczka} ({waga_najlzejszej_paczki} kg).')




#########
#
# Etap 1
# 1. Pytamy o liczbę ELEMENTÓW, które mają zostać dodane do PACZEK.
# 1. Pytamy o wagę każdego z ELEMENTÓW.

# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(0, ilosc_elementow): # Zapis range(0, ilosc_paczek) jest tym samym co range(ilosc_paczek)
#     waga_elementu = float(input('Podaj wagę elementu: '))


#########
#
# Etap 2
# – Sprawdzam, ile kilogramów wysłano (wagę wszystkich ELEMENTÓW).

# waga_wszystkich_elementow = 0
# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(0, ilosc_elementow): # Zapis range(0, ilosc_paczek) jest tym samym co range(ilosc_paczek)
#     waga_elementu = float(input('Podaj wagę elementu: '))
#     waga_wszystkich_elementow += waga_elementu # Dodaje wagę kolejnych, dodanych ELEMENTÓW
#
# print(f'Wysłano: {waga_wszystkich_elementow} kg.')


#########
#
# Etap 3
# – Sprawdzam, ile PACZEK wysłano (każda paczka zawiera pewną sumę ELEMENTÓW).

# waga_wszystkich_elementow = 0
# ilosc_paczek = 1
# maksymalna_waga_paczki = 20
# aktualna_waga_paczki = 0
#
# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(ilosc_elementow):
#     waga_elementu = float(input('Podaj wagę elementu: '))
#     waga_wszystkich_elementow += waga_elementu
#     if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki: # Jeżeli mam miejsce w PACZCE
#         aktualna_waga_paczki += waga_elementu # to dodaję kolejny ELEMENT
#     else:
#         aktualna_waga_paczki = waga_elementu # Zamykam PACZKĘ
#         ilosc_paczek += 1 # zwiększam liczbę PACZEK o kolejną
#
# print(f'Wysłano: {waga_wszystkich_elementow} kg.')
# print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
# print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')


#########
#
# Etap 4
# – Sprawdzam, która PACZKA miała najwięcej "pustych" kilogramów, i ile to było kilogramów.

# waga_wszystkich_elementow = 0
# ilosc_paczek = 1
# maksymalna_waga_paczki = 20
# aktualna_waga_paczki = 0
# najlzejsza_paczka = 0
# waga_najlzejszej_paczki = maksymalna_waga_paczki # Wagę tej paczki trzeba porównać w maksymalnym, a nie minimalną wagą PACZKI (dlatego NIE wpisuje tutaj 0)
#
# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(ilosc_elementow):
#     waga_elementu = float(input('Podaj wagę elementu: '))
#     waga_wszystkich_elementow += waga_elementu
#     if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki:
#         aktualna_waga_paczki += waga_elementu
#     else: # Muszę sprawdzić, która PACZKA jest najlżejsza w momencie, kiedy kończę ją ładować (zanim załaduje nową PACZKĘ)
#         if aktualna_waga_paczki < waga_najlzejszej_paczki: # Sprawdzam, czy obecna PACZKA była najlżejsza
#             najlzejsza_paczka = ilosc_paczek  # liczba PACZEK mówi też, w której PACZCE aktualnie jesteśmy.
#             waga_najlzejszej_paczki = aktualna_waga_paczki  # Po to, aby wiedzieć, jaki jest aktualny rozmiar PACZKI
#         aktualna_waga_paczki = waga_elementu
#         ilosc_paczek += 1
#
# print(f'Wysłano: {waga_wszystkich_elementow} kg.')
# print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
# print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')
# print(f'Najwięcej pustych kilogramów na PACZKA: {najlzejsza_paczka} ({maksymalna_waga_paczki - waga_najlzejszej_paczki} kg).')


#########
#
# Etap 5
# – Dodaje ograniczenie dotyczące rozmiaru ELEMENTÓW

# waga_wszystkich_elementow = 0
# ilosc_paczek = 0
# maksymalna_waga_paczki = 20
# aktualna_waga_paczki = 0
# najlzejsza_paczka = 0
# waga_najlzejszej_paczki = maksymalna_waga_paczki # Wagę tej paczki trzeba porównać w maksymalnym, a nie minimalną wagą PACZKI (dlatego NIE wpisuje tutaj 0)
#
# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# for numer_elementu in range(ilosc_elementow):
#     waga_elementu = float(input('Podaj wagę elementu: '))
#     if 1 < waga_elementu > 10: # Ograniczenie dotyczące rozmiaru ELEMENTÓW
#         print('Waga każdego elementów musi być z przedziału od 1 do 10 kg.')
#         break
#     waga_wszystkich_elementow += waga_elementu
#     if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki:
#         aktualna_waga_paczki += waga_elementu
#     else:
#         if aktualna_waga_paczki < waga_najlzejszej_paczki:
#             ilosc_paczek = 1 # Jeśli jest choć jeden ELEMENT zmieścił się w PACZCE
#             najlzejsza_paczka = ilosc_paczek
#             waga_najlzejszej_paczki = aktualna_waga_paczki
#         aktualna_waga_paczki = waga_elementu
#         ilosc_paczek += 1
#
# print()
# print(f'Wysłano: {waga_wszystkich_elementow} kg.')
# print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
# print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')
# print(f'Najwięcej pustych kilogramów na PACZKA: {najlzejsza_paczka} ({maksymalna_waga_paczki - waga_najlzejszej_paczki} kg).')
# print()



#########
#
# Etap 6
# – Sprawdzenie, czy cokolwiek zostało dodane do wysyłki

# waga_wszystkich_elementow = 0
# ilosc_paczek = 0
# maksymalna_waga_paczki = 20
# aktualna_waga_paczki = 0
# najlzejsza_paczka = 0
# waga_najlzejszej_paczki = maksymalna_waga_paczki # Wagę tej paczki trzeba porównać w maksymalnym, a nie minimalną wagą PACZKI (dlatego NIE wpisuje tutaj 0)
#
# ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))
#
# if ilosc_elementow > 0:
#     for numer_elementu in range(ilosc_elementow):
#         waga_elementu = float(input('Podaj wagę elementu: '))
#         if waga_elementu > 10 or waga_elementu < 1:
#             print(f'\nWpisałeś {waga_elementu} kg. Każdy z elementów musi warzyć od 1 do 10 kg.')
#             break
#         waga_wszystkich_elementow += waga_elementu
#         if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki:
#             aktualna_waga_paczki += waga_elementu
#         else:
#             if aktualna_waga_paczki < waga_najlzejszej_paczki:
#                 ilosc_paczek = 1 # Jeśli jest choć jeden ELEMENT zmieścił się w PACZCE
#                 najlzejsza_paczka = ilosc_paczek
#                 waga_najlzejszej_paczki = aktualna_waga_paczki
#             aktualna_waga_paczki = waga_elementu
#             ilosc_paczek += 1
#
#     print()
#     print(f'Wysłano: {waga_wszystkich_elementow} kg.')
#     print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
#     print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')
#     print(f'Najwięcej pustych kilogramów na PACZKA: {najlzejsza_paczka} ({maksymalna_waga_paczki - waga_najlzejszej_paczki} kg).')
#     print()
#
# else:
#     print()
#     print('Nie dodałeś nic do wysyłki.')



#########
#
# Etap 7
# – Zamknięcie ostatniej PACZKI

waga_wszystkich_elementow = 0
ilosc_paczek = 0 # Co zrobić, kiedy nie wysłałem żadnego ELEMENTU, żeby nie wyświetliło 1 tylko ZERO?
maksymalna_waga_paczki = 20
aktualna_waga_paczki = 0
najlzejsza_paczka = 0
waga_najlzejszej_paczki = maksymalna_waga_paczki # Wagę tej paczki trzeba porównać w maksymalnym, a nie minimalną wagą PACZKI (dlatego NIE wpisuje tutaj 0)

ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))

if ilosc_elementow > 0:
    for numer_elementu in range(ilosc_elementow):
        waga_elementu = float(input('Podaj wagę elementu: '))
        if waga_elementu > 10 or waga_elementu < 1:
            print(f'\nWpisałeś {waga_elementu} kg. Każdy z elementów musi warzyć od 1 do 10 kg.')
            break
        waga_wszystkich_elementow += waga_elementu
        if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki:
            aktualna_waga_paczki += waga_elementu
        else: # Tu kończy się ładowanie aktualnej PACZKI
            if aktualna_waga_paczki < waga_najlzejszej_paczki:
                ilosc_paczek = 1
                najlzejsza_paczka = ilosc_paczek
                waga_najlzejszej_paczki = aktualna_waga_paczki
            aktualna_waga_paczki = waga_elementu
            ilosc_paczek += 1
    if aktualna_waga_paczki > 0: # Sprawdzamy, czy coś włożyłem do ostatniej PACZKI
        if aktualna_waga_paczki < waga_najlzejszej_paczki: # Dzięki temu ostatnia PACZKA sostanie wzięta pod uwagę (wcześniej nie mogła, bo nie była pod "else")
            najlzejsza_paczka = ilosc_paczek
            waga_najlzejszej_paczki = aktualna_waga_paczki


    print()
    print(f'Wysłano: {waga_wszystkich_elementow} kg.')
    print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
    print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')
    print(f'Najwięcej pustych kilogramów na PACZKA: {najlzejsza_paczka} ({maksymalna_waga_paczki - waga_najlzejszej_paczki} kg).')
    print()

else:
    print()
    print('Nie dodałeś nic do wysyłki.')
