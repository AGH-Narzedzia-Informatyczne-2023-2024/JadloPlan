

class User:
    def __init__(self, first_name, last_name, gender, birth_date, location, email, profile_picture=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.location = location
        self.email = email
        self.profile_picture = profile_picture

    def display_info(self):
        print(f"Imię: {self.first_name}")
        print(f"Nazwisko: {self.last_name}")
        print(f"Płeć: {self.gender}")
        print(f"Data urodzenia: {self.birth_date}")
        print(f"Miejsce zamieszkania: {self.location}")
        print(f"Adres email: {self.email}")
        if self.profile_picture:
            print("Zdjęcie załączone")
        else:
            print("Brak załączonego zdjęcia")

def create_account():
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    gender = input("Podaj płeć: ")
    birth_date_str = input("Podaj datę urodzenia (RRRR-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    location = input("Podaj miejsce zamieszkania: ")
    email = input("Podaj adres email: ")
    
    attach_picture = input("Czy chcesz załączyć zdjęcie? (tak/nie): ")
    if attach_picture.lower() == 'tak':
        picture_path = input("Podaj ścieżkę do pliku JPEG ze zdjęciem: ")
        try:
            img = Image.open(picture_path)
            profile_picture = img.tobytes()
        except Exception as e:
            print(f"Błąd przy otwieraniu pliku: {e}")
            profile_picture = None
    else:
        profile_picture = None

    user = User(first_name, last_name, gender, birth_date, location, email, profile_picture)
    return user

if __name__ == "__main__":
    new_user = create_account()
    print("\nUtworzone konto:")
    new_user.display_info()