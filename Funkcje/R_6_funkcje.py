########## FUNKCJE rozdział 8
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


# def get_formatted_name(first_name, last_name):
#     """Zwraca elegancko sformatowne pełne imie i nazwisko."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# # To jest petla działąca w nieksoczoność!
# while True:
#     print("\nProsze podac imie i nazwisko:")
#     print("(wpisz 'q', aby zakonczyć prace w dowolnym momencie)")

#     f_name = input("Imię: ")
#     if f_name == 'q':
#         break
    
#     l_name = input("Nazwisko:")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nWitaj, " + formatted_name + "!")

########## przekazywanie listy
# def greet_users(names):
#     """Wyswietla proste powitanie kazdemu użytkownikowi listy"""
#     for name in names:
#         msg = "Witaj, " + name.title() + "!"
#         print(msg)
# usernames = ['halina', 'tymek', 'marzena']
# greet_users(usernames)

########## modyfikowanie listy w funkcji
### Rozwiązanie bez uzycia funkcji ###
# rozpoczynamy od pewnych projektów które maja być wydrukowane.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecehedron']
# completed_models =[]
# # symulujemy wydruk posczególnych projektów, dopóki pozostał jakakolwiek projekt na liście.
# # każdy wydrukowany model zostaje przeniesiony na liste copleted_models.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # symulacja druku 3D na podstawie modelu.
#     print("Wydruk modelu: " + current_design)
#     completed_models.append(current_design)

# #Wyswietlenie wszystkich wydrukowanych modeli
# print("\nWydrukowane zostały następujące modele:") 
# for completed_model in completed_models:
#     print(completed_model)

### Rozwiązanie z użyciem 2 funkcji ###
# def print_models(unprinted_designs, completed_models):
#     """
#     Symuluje wydruk poszczególnych projektów, dopóki pozostał jakikolwiek
#     projekt na liście. Każdy wydrukowany model zostaje przeniesiony na
#     liste completed_models.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         # Symulacja wydruku 3D na podstawie modelu.
#         print("Wydruk modelu: " + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """ Wyświetla wszystkie modele, które zostały wydrukowane"""
#     print("\nWydrukowane zostały nastepujęce modele:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

########## uniemozliwienie modyfikowanie listy przez funkcję
# kopię listy można przekazac do funkcji w przedstawiony poniżej sposób:
# nazwa_funkcji(nazwa_listy[:])

########## przekazywanie dowolnej listy argumentów
# def make_pizza(*toppings):
#     """Wyświetla listy dodatków wybranych przez klienta."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('pieczarki', 'zielona papryka', 'podwójny ser')

# def make_pizza(*toppings):
#     """Podsumowanie informacji o przygotowywanej pizzy"""
#     print("\nPrzygotowuje pizzę z następującymi dodatkami")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('pieczarki', 'zileona papryka', 'podwójny ser')

########## argumenty pozycyjne i przekazywanie dowolnej liczby argumentów
# def make_pizza(size, *toppings):
#     """Podsumowanie informacjie o przygotowanej pizzy"""
#     print("\nPrzygotowuje pizze o wielkości " + str(size) + "cm, z nastepującymi dodatkami:")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza(40, 'pepperoni')
# make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

########## używanie dowolnej liczby argumentów w postaci słów kluczowych
# def build_profile(first, last, **user_info):
#     """Budowa słownika zawierającego wszelkie informacje o użytkowniku."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# user_profile = build_profile('albert', 'einstein',location='princeton',field='fizyka')
# print(user_profile)

########## przechowywanie funkcji w modułach
########## import całego modułu
import modul
modul.make_pizza(40, 'pepperoni')
modul.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

########## importowanie okreslonych funkcji
from modul import make_pizza
make_pizza(50, 'czosnek')
make_pizza(60, 'kurki', 'pomidor', 'feta')

########## użycie słowa kluczowego " as " w celu zdefinowania aliasu modułu
from modul import make_pizza as mp
mp( 20, 'szynka')
mp( 35, 'boczek', 'salami', "ser")

########## import wszystkich funkcji modułu za pomocą operatora " * "
from modul import *
make_pizza(40, 'pepproni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')

####################################### ZRÓB TO SAM #########################################
