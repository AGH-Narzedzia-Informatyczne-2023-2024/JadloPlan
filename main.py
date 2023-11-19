from collections import Counter

def dodaj_przepis(przepis, slownik_zakupow):
    slownik_zakupow.update(Counter(przepis))

def utworz_slownik_zakupow(przepisy):
    slownik_zakupow = Counter()
    for przepis in przepisy:
        dodaj_przepis(przepis, slownik_zakupow)
    return slownik_zakupow

def main():
    przepisy = [
        ["jajka", "mleko", "mąka"],
        ["pomidory", "cebula", "czosnek", "makaron"],
        ["kurczak", "ziemniaki", "marchew", "cebula"]
    ]

    slownik_zakupow = utworz_slownik_zakupow(przepisy)

    print("Lista zakupów:")
    for index, (skladnik, ilosc) in enumerate(slownik_zakupow.items(), start=1):
        print(f"{index}. {skladnik}: sztuk {ilosc}")

if __name__ == "__main__":
    main()