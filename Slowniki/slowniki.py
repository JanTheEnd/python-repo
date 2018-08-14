########## prosty słownik
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

########## uzyskiwanie dostępy do wartości slownika
# alien_0 = {'color': 'zielony', 'points': 5}
# new_points = alien_0['points']
# print("Zdobyles " + str(new_points) + ' punktow')

########## dodanie nowej pary klucz-wartość
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

########## rozpoczęcie pracy od pustego slownika
# alien_0 = {}
# alien_0['color'] = 'zielony'
# alien_0['points'] = 5
# print(alien_0)

########## modyfikowanie wratości słownika
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'szybko'} 
# print("Poczatkowa wartosc x-position:" + str(alien_0['x_position']))
# #przesunięcie obcego w prawo
# #ustalenie odleglosci, jaka powinien pokonac obcy poruszajacy się z daną szybkością
# if alien_0['speed'] == 'wolno':
#     x_increment = 1
# elif alien_0['speed'] == 'srednio':
#     x_increment = 2
# elif alien_0['speed'] == 'szybko':
#     x_increment = 3
# else:
#     # to musi byc szybki obcy
#     x_increment = 4
# # nowe położenie to suma dotychczasowego położenia i wartości x_increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("Nowa wartosc x-position: " + str(alien_0['x_position']))
########## usuwanie pary klucz-wartość !!! należy pamietać że usunięcie jest NIEODWRACALNE!!!
# alien_0 = { 'color': 'zielony', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

########## słownik podobnych obiektów
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python'
#     }
# print("Ulubiony jezyk programowania Sary to " +
#     favorite_languages['sara'].title() +
#     '.')
########## iteracja przez słownik
########## iteracja przez wszystkie pary klucz wartość
# user_0 = {
#     'username': 'jkowalski',
#     'first': 'jan',
#     'last': 'kowalski',
# }
# for key, value in user_0.items(): # można zapisać tak for k, v in user_0.items()
#     print("\nKlucz: " + key)
#     print("Wartosc: " + value)

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
#     }
# for name, language in favorite_languages.items():
#     print("Ulubiony jezyk programowania uzytkownika " + name.title() +
#     " to " + language.title() + '.')

########## iteracja przez wszystkie klucz słoawnika metoda keys()
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
# }

# for name in favorite_languages.keys():  # alternatywnie for name in favorite_languages:
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
# }
# friends = ['pawel', 'sara']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(" Witaj, " + name.title() + 
#         " ! Widze, ze Twoim ulubionym jezykiem programowania jest " +
#         favorite_languages[name].title() + '!')

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
#     #'elzbieta': 'java',
# }
# if 'elzbieta' not in favorite_languages.keys():
#     print("Elzbieta, wez prosze udzial w naszej ankiecie!")
# else:
#     print("Elki jest juz na liscie")

########## iteracja poprzez uporządkowane klucze słownika funkcja sorted()
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
#     }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", dziekujemy za udzial w ankiecie.")

########## iteracja przez wszystkie wratości słownika
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
# }
# print("W ankiecie zostaly wymienieone nastepujace jezyki programowania:")
# for language in favorite_languages.values():
#     print(language.title())

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'rudy',
#     'pawel': 'python',
#     }
# print("W ankiecie zostaly wymienieone nastepujace jezyki programowania:")
# for language in set(favorite_languages.values()): # <-------- wywołanie set()
#     print(language.title())

########## zagieżdżenie lista słowników
# alien_0 = {'color': 'zielony', 'points': '5'}
# alien_1 = {'color': 'zolty', 'points': '10'}
# alien_2 = {'color': 'czerwony', 'points': '15'}
# aliens = [alien_0, alien_1, alien_2] 
# for alien in aliens:
#     print(alien)

#utworzenie pustej listy do przechowywania obcych
# aliens = [] 
# # utworzenie 30 zielonych obcych
# for alien_number in range(30):
#     new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
#     aliens.append(new_alien)
# # wyswietlenie pierwszysch pieciu obcych
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # wyświetlenie całkowitej liczby obcych
# print("Calkowita liczba obcych:" + str(len(aliens)))

# aliens = []
# # utworzenie 30 zielonych obcych
# for alien_number in range(0,30):
#     new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
#     aliens.append(new_alien)

# for alien in aliens[0:8]:
#     if alien['color'] == 'zielony':
#         alien['color'] = 'zolty'
#         alien['speed'] = 'srednio'
#         alien['points'] = 10
#     elif alien['color'] == 'zolty':
#         alien['color'] = 'czerwony'
#         alien['speed'] = 'szybko'
#         alien['points'] = 15

# #wyswietl pierwszych .... obcych
# for alien in aliens[0:15]:
#     print(alien)
# print("...")
# # wyświetlenie całkowitej liczby obcych
# print("Calkowita liczba obcych:" + str(len(aliens)))

########## lista w słowniku
# przechowywanie informacji o pizzy zamawianej przez klienta
# pizza = {
#     'crust': 'grubym',
#     'toppings': ['pieczarki', 'podwojny ser'],
#     }
# # posumowanie zamówienia
# print("Zamowiles pizze na " + pizza['crust'] + " ciescie " + "wraz z nastepujacymi dodatkami:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languanges = {
#     'janek': ['python' , 'ruby'],
#     'sara': ['c'],
#     'edward': ['ruby', 'go'],
#     'pawel': ['python', 'haskell'],
#     }
# for name, languages in favorite_languanges.items():
#     print("\n Ulubione jezyki programowania uzytkownika " + name.title() +
#     " to") 
#     for language in languages:
#         print("\t" + language.title())

########## słownik w słowniku
# users = {
#     'aeinstein':{
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'maria',
#         'last': 'sklodowska-curie',
#         'location': 'paryz',
#     }
# }
# for username, user_info in users.items():
#     print("\nNazwa uzytkownika:" + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#     print("\tImie i nazwisko: " + full_name.title())
#     print("\tMiejscowosc: " + location.title())
