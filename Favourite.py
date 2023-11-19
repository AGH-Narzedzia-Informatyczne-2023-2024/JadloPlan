
ulubione_przepisy = []

# Funkcja do dodawania przepisu do listy
def dodaj_przepis():
    przepis = input("Podaj swój ulubiony przepis: ")
    ulubione_przepisy.append(przepis)
    print("Przepis dodany do ulubionych!")

# Pytanie użytkownika, czy chce dodać przepis do ulubionych
czy_dodac_przepis = input("Czy chcesz dodać swój ulubiony przepis? (tak/nie): ").lower()

if czy_dodac_przepis == 'tak':
    dodaj_przepis()
else:
    print("Możesz dodać przepis później.")

# Wyświetlenie listy ulubionych przepisów
print("\nTwoje ulubione przepisy:")
for idx, przepis in enumerate(ulubione_przepisy, start=1):
    print(f"{idx}. {przepis}")
}
