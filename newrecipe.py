# Funkcja do pobierania liczby porcji wraz z jednostką miary
def pobierz_liczbe_porcji():
    while True:
        try:
            input_liczba_porcji = input("Podaj liczbę porcji wraz z jednostką miary (np. '4 porcje'): ")
            # Rozdzielanie liczby i jednostki miary
            liczba_porcji, jednostka_miary = input_liczba_porcji.split()
            liczba_porcji = int(liczba_porcji)
            return liczba_porcji, jednostka_miary
        except ValueError:
            print("Błąd! Podaj liczbę porcji wraz z jednostką miary (np. '4 porcje').")

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
