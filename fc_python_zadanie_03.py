# FC – PYTHON – ZADANIE 3 – Kółko i krzyżyk (zadanie dodatkowe)
#
# Napisz program do gry w kółko i krzyżyk z przeciwnikiem komputerowym. Główne założenia:
# 1. Gracz komputerowy rozpoczyna grę.
# 2. Gracz komputerowy jest reprezentowany przez krzyżyk.
# 3. Użytkownik programu jest reprezentowany przez kółko.
# 4. Przeciwnik komputerowy gra optymalnie, tzn. zawsze wybiera najlepszy możliwy ruch. W połączeniu z pkt 1 oznacza to, że gracz komputerowy nigdy nie przegra.
# 5. Identyfikatory pól na tablicy są rozmieszczone następująco:
#    1 2 3
#    4 5 6
#    7 8 9
#
# Przebieg gry (działanie programu):
# 1. Przeciwnik komputerowy wykonuje ruch. Jeśli komputer wygrał, wyświetla komunikat "Przegrana".
#    Jeśli ostatnie pole zostało wypełnione, wyświetla komunikat "Remis" i kończy działanie.
# 2. Program zaczyna działanie od wyświetlenia tablicy jako trzech linii w terminalu. Minus "-" symbolizuje pole jeszcze nie wypełnione.
# ---
# -X-
# ---
# 3. Program pobiera od użytkownika identyfikator pola, które ma być wypełnione kółkiem i oczekuje naciśnięcia <Enter>.
# 4. Jeśli identyfikator pola jest nieprawidłowy (zły identyfikator lub pole jest już zajęte), program wyświetla napis "Błąd", i wraca do punktu 4.
# 5. Program wraca do punktu 1.
