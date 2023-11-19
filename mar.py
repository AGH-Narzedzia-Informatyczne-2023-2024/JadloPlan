# Funkcja do pobierania liczby porcji
def pobierz_liczbe_porcji():
    while True:
        try:
            liczba_porcji = int(input("Podaj liczbę porcji: "))
            return liczba_porcji
        except ValueError:
            print("Błąd! Podaj liczbę całkowitą.")

# Pobieranie informacji od użytkownika
nazwa_przepisu = input("Podaj nazwę przepisu: ")
skladniki = input("Podaj składniki, oddzielając je przecinkiem: ").split(',')
przygotowanie = input("Podaj sposób przygotowywania: ")
liczba_porcji = pobierz_liczbe_porcji()

# Wyświetlanie informacji
print("\nPrzepis: {}".format(nazwa_przepisu))
print("\nSkładniki:")
for skladnik in skladniki:
    print("- {}".format(skladnik.strip()))  # Usunięcie zbędnych białych znaków
print("\nSposób przygotowywania: {}".format(przygotowanie))
print("\nLiczba porcji: {}".format(liczba_porcji))
