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
# def get_formatted_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

########## definiowanie argumentu jako opcjonalnego
# def get_formatted_name(first_name, middle_name, last_name):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Zwraca elegancko sformatowane pełne imię i nazwisko."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

########## zwrot słownika
# def build_person(first_name, last_name, age=''):
#     """Zwraca słownik informacji o danej osobie"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

########## używanie funkcji wraz petla while
# def get_formatted_name(first_name, last_name):
#     """Zwraca elegancko sformatowne pełne imie i nazwisko."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# To jest petla działąca w nieksoczoność!
# while True:
#     print("\nProsze podac imie i nazwisko:")
#     f_name = input("Imię: ")
#     l_name = input("Nazwisko: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nWitaj, " + formatted_name + "!")


def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowne pełne imie i nazwisko."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# To jest petla działąca w nieksoczoność!
while True:
    print("\nProsze podac imie i nazwisko:")
    print("(wpisz 'q', aby zakonczyć prace w dowolnym momencie)")

    f_name = input("Imię: ")
    if f_name == 'q':
        break
    
    l_name = input("Nazwisko:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nWitaj, " + formatted_name + "!")
