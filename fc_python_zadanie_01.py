# FC – PYTHON – ZADANIE 1 – Program do generowania życzeń urodzinowych
#
# Stwórz program, który generuje spersonalizowaną kartkę urodzinową. Program będzie prosił użytkownika o konkretne informacje,
# a następnie generował kartkę urodzinową na podstawie jego odpowiedzi.
# Wiek osoby powinien być obliczany na podstawie roku urodzenia podanego przez użytkownika.
#
# 1. Napisz program, który prosi użytkownika o podanie następujących informacji:
#  – Imię odbiorcy
#  – Rok urodzenia
#  – Spersonalizowaną wiadomość
#  – Imię nadawcy
#
# 2. Program powinien następnie obliczyć wiek odbiorcy na podstawie obecnego roku i roku urodzenia podanego przez użytkownika.
#
# 3. Wygeneruj spersonalizowaną kartkę urodzinową z następującą wiadomością:
# [Imię odbiorcy], wszystkiego najlepszego z okazji [Wiek] urodzin!
# [Spersonalizowana Wiadomość]
# [Imię Nadawcy]
#
# Wskazówki:
# – Upewnij się, że program jest łatwy w obsłudze
# – Podczas obliczania wieku odbiorcy, pamiętaj, aby konwertować dane wprowadzone przez użytkownika na odpowiedni typ zmiennej.
# – Możesz zodyfikować szablon według własnego uznania. Upewnij się, że wyświetlasz wszystkie niezbędne zmienne.

name = input('Podaj imię ODBIORCY wiadomości: ')
age = int(input('Podaj rok urodzenia ODBIORCY wiadomości: '))
message = input('Wpisz spersonalizowaną WIADOMOŚĆ: ')
sender = input('Podaj imię NADAWCY wiadomości: ')
print()

print(f'{name}, wszystkiego najlepszego z okazji {2026 - age} urodzin!')
print(message)
print(f'Życzy {sender}.')
print()

### NIŻEJ wersja zadania, w której dzięki modułowi datatime pobrałem bieżący rok systemowy.

from datetime import date
act_year = date.today().year

print(f'{name}, wszystkiego najlepszego z okazji {act_year - age} urodzin!')
print(message)
print(f'Życzy {sender}.')
print()