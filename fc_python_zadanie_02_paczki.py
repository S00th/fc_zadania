# FC – PYTHON – ZADANIE 2 – Pętle i argumenty w konsoli – PROGRAM do obsługi ładowarki PACZEK
#
# UWAGA! Oryginalny opis ZADANIA (dodany niżej) zawiera błędy uniemożliwiające przygotowanie poprawnie działającego programu.
# Już na początku powinniśmy zapytać "Ile ELEMENTÓW (a nie PACZEK) chcesz wysłać?".
# ELEMENTY są ładowane do PACZEK. Wiemy, ile ELEMENTÓW chcemy wysłać, ale nie wiemy, do ilu PACZEK je zmieścimy i ile PACZEK wyślemy.
# Liczbę wysłanych PACZEK ma nam obliczyć program. Wyraz TOWAR jest niepotrzebny. Wprowadza jedynie zamieszanie.
# Treść poprawiłem i dodałem tutaj: https://docs.google.com/document/d/1AvPNBNYynIBkpQsADBwLX33gFWA72HnSqIW5A20Gjqk/edit?usp=sharing
#
# Napisz program do obsługi ładowarki PACZEK. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać,
# a następnie wymaga podania wagi dla każdej z nich.
#
# Na koniec działania program powinien wyświetlić w podsumowaniu:
# 1. Liczbę paczek wysłanych.
# 2. Liczbę kilogramów wysłanych.
# 3. Suma "pustych" – kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych.
# 4. Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik.
#
# Restrykcje:
# – Waga elementów musi być z przedziału od 1 do 10 kg.
# – Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# – W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# – W przypadku podania wagi elementu mniejszej od 1 kg lub większej od 10 kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane.
# – Wyświetlane jest podsumowanie.
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



waga_wszystkich_elementow = 0
ilosc_paczek = 1
maksymalna_waga_paczki = 20
aktualna_waga_paczki = 0
najlzejsza_paczka = 0
waga_najlzejszej_paczki = maksymalna_waga_paczki  # Szukam najlżejszej paczki, więc muszę zacząć porównywać od najcięższej (wpisałbym 0, gdybym szukał NAJCIĘŻSZEJ)

ilosc_elementow = int(input('Ile elementów chcesz wysłać? '))

if ilosc_elementow <= 0: # Sprawdzam, czy w ogóle został dodany jakiś ELEMENT
    raise ValueError('Nie dodałeś nic do wysyłki')
for numer_elementu in range(ilosc_elementow): # Zapis range(ilosc_paczek) jest tym samym co range(0, ilosc_paczek)
    waga_elementu = float(input('Podaj wagę elementu: '))
    if waga_elementu > 10 or waga_elementu < 1: # Ograniczenie dotyczące rozmiaru ELEMENTÓW
        print(f'\nWpisałeś {waga_elementu} kg. Każdy z elementów musi ważyć od 1 do 10 kg.') # Dodałem akapit (\n) dla zwiększenia czytelności komunikatu.
        break
    waga_wszystkich_elementow += waga_elementu
    if waga_elementu + aktualna_waga_paczki <= maksymalna_waga_paczki: # Jeżeli w PACZCE jest jeszcze miejsce
        aktualna_waga_paczki += waga_elementu # to dodaję kolejny ELEMENT
    else: # Tu kończy się ładowanie aktualnej PACZKI
        if aktualna_waga_paczki <= waga_najlzejszej_paczki: # Sprawdzam, czy obecna PACZKA była najlżejsza
            najlzejsza_paczka = ilosc_paczek # "liczba_paczek" mówi też, w której PACZCE aktualnie jesteśmy.
            waga_najlzejszej_paczki = aktualna_waga_paczki # Chcę wiedzieć, jaki jest aktualny rozmiar PACZKI
        aktualna_waga_paczki = waga_elementu # Zamykam PACZKĘ
        ilosc_paczek += 1 # i zwiększam liczbę PACZEK o kolejną
if aktualna_waga_paczki > 0: # Sprawdzamy, czy coś włożyłem do ostatniej PACZKI
    if aktualna_waga_paczki <= waga_najlzejszej_paczki: # Ostatnia PACZKA zostanie wzięta pod uwagę (wcześniej nie mogła, bo nie była pod "else")
        najlzejsza_paczka = ilosc_paczek
        waga_najlzejszej_paczki = aktualna_waga_paczki

    print()
    print(f'Wysłano: {waga_wszystkich_elementow} kg.')
    print(f'Liczba wysłanych PACZEK: {ilosc_paczek}.')
    print(f'Suma pustych kilogramów: {ilosc_paczek * maksymalna_waga_paczki - waga_wszystkich_elementow} kg.')
    print(f'Najwięcej pustych kilogramów na PACZKA: {najlzejsza_paczka} ({maksymalna_waga_paczki - waga_najlzejszej_paczki} kg).')
    print()