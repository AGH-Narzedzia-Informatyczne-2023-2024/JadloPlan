def pobierz_liste():
    print("Podaj składniki, każdy składnik oddziel spacja lub Enter. Wpisz 'koniec', aby zakończyć.")

    skladniki = []
    while True:
        skladnik = input("Składnik: ")
        if skladnik.lower() == 'koniec':
            break
        skladniki.append(skladnik)

    return skladniki

# Wyświetlanie listy składników
def wyswietl_liste(skladniki):
    print("\nTwoja lista składników:")
    for index, skladnik in enumerate(skladniki, start=1):
        print(f"{index}. {skladnik}")

# Główna część programu
if __name__ == "__main__":
    lista_skladnikow = pobierz_liste()
    wyswietl_liste(lista_skladnikow)
