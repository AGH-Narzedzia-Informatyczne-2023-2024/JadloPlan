#funckja do wypisywania planu dnia 
def wypiszPlan(dzienTygodnia,posilek,userId)
    try:
        data = getDocs(db,'users/{userId}/posilki/{dzienTygodnia}/{posilek}')
    except: 
        print("Error")
    return data.data()

dzienTygodnia = input("Podaj dzien tygodnia")
posilek = input("Podaj rodzaj posiłku")

print(wypiszPlan(dzienTygodnia,posilek))
