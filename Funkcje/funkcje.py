########## definiowanie funkcji
# def greet_user():
#     """Wyświetla proste powitanie"""
#     print("Witaj!")

# greet_user()

########## przekazywanie informacji do funkcji
# def greet_user(username):
#     """Wyświetla proste powitanie"""
#     print("Witaj! " + username.title() + "!")

# greet_user('janek')
# greet_user('sara')

########## przekazywanie argumentów - argumenty pozycyjne
# def describe_pet(animal_pet, pet_name):
#     """ Wyświetla informacje o zwierzęciu """
#     print("\nMoje zwierze to " + animal_pet + ".")
#     print("Mój " + animal_pet + " ma na imię " + pet_name.title() + ".")

# describe_pet('chomik', 'harry')
# describe_pet('pies', 'willie')

########## argumanty w postaci słow kluczowych
# def describe_pet(animal_type, pet_name):
#     """ Wyświetla informacje o zwierzęciu """
#     print("\nMoje zwierze to " + animal_type + ".")
#     print("Mój " + animal_type + " ma na imię " + pet_name.title() + ".")
# describe_pet(animal_type='chomik', pet_name='harry')

########## wartości domyślne
# def describe_pet(pet_name, animal_type='pies'):
#     """ Wyświetla informacje o zwierzęciu """
#     print("\nMoje zwierze to " + animal_type + ".")
#     print("Mój " + animal_type + " ma na imię " + pet_name.title() + ".")

# describe_pet(pet_name='willie')

########## unikanie błędów związanych z argumentami
# def descirbe_pet(animal_type, pet_name):
#     """Wyswietla informację o zwierzęciu"""
#     print("\nMoje zwierzę to " + animal_type + ".")
#     print("Mój " + animal_type + "ma na imię " + pet_name + ".")
# descirbe_pet() ### brak argumentów funkcji błąd kompilacji

########## wartość zwrotna  -  zwrot prostej wartości
def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko_Andrzej J."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
