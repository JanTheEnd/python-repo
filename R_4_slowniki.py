########## SŁOWNIKI rozdzial 6
########## prosty słownik
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

########## uzyskiwanie dostepu do wartości słownika
# alien_0 = {'color': 'zielony'}
# print(alien_0['color'])

# alien_0 = {'color': 'zielony', 'points': 5}
# new_points = alien_0['points']
# print("Zdobyłeś " + str(new_points) + " punktów!")

########## dodawanie nowej pary klucz wartość
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

########## rozpoczęcie pracy od pustego słownika
# alien_0 = {}
# alien_0['color'] = 'zielony'
# alien_0['points'] = 5
# print(alien_0)

########## modyfikowanie wartości słownika
# alien_0 = {'color': 'zielony'}
# print("Obcy ma kolor " + alien_0['color'] + ".")
# alien_0['color'] = 'żółty'
# print("Obcy ma teraz kolor " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio'}
# print("Początkowa wartość x-position: " + str(alien_0['x_position']))
# # Przesunięcie obcego w prawo.
# # Ustalenie odległości, jaką powinien pokonać obcy poruszający się z daną szybkością.
# if alien_0['speed'] == 'wolno':
#     x_increment = 1
# elif alien_0['speed'] == 'średnio':
#     x_increment = 2
# else:
#     # To musi być szybki obcy.
#     x_increment = 3
# # Nowe położenie to suma dotychczasowego położenia i wartości x_increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("Nowa wartość x-position: " + str(alien_0['x_position']))

########## usuwanie pary klucz wartość
# alien_0 = {'color': 'zielony', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

########## słownik podobnych obiektów
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# print("Ulubiony język programowania Sary to " +
#       favorite_languages['sara'].title() +
#       ".")

########## iteracja przez słownik
########## iteracja przez wszystkie pary klucz-wartość
# user_0 = {
#     'username': 'jkowalski',
#     'first': 'jan',
#     'last': 'kowalski',
# }
# for key, value in user_0.items():# zamiast 'key' i 'value' można użyc dowolnej nazwy np. 'k' i 'v'
#     print("\nKlucz: " + key)
#     print("Wartość: " + value)

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# for name, language in favorite_languages.items():
#     print("Ulubiony język programowania użytkownika " + name.title() + " to " +
#           language.title() + ".")

########## iteracja przez wszystkie klucze słownika
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# friends = ['paweł', 'sara']
# for name in favorite_languages.keys(): # użycie metody keys()
#     print(name.title())

#     if name in friends:
#         print("  Witaj, " + name.title() +
#               "! Widzę, że Twoim ulubionym językiem programowania jest " +
#               favorite_languages[name].title() + "!")

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# if 'elżbieta' not in favorite_languages.keys(): # uzycie metody kesy()
#     print("Elżbieta, proszę, weź udział w naszej ankiecie!")

########## iteracja przez uporządkowanie klucze słownika
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", dziękujemy za udział w ankiecie.")

########## iteracja przez wszystkie wartości słownika
# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# print("W ankiecie zostały wymienione następujące języki programowania:")
# for language in favorite_languages.values():
#     print(language.title())

# favorite_languages = {
#     'janek': 'python',
#     'sara': 'c',
#     'edward': 'ruby',
#     'paweł': 'python',
# }
# print("W ankiecie zostały wymienione następujące języki programowania:")
# for language in set(favorite_languages.values()):
#     print(language.title())

########## Zagnieżdżenia 
########## lista słowników
# alien_0 = {'color': 'zielony', 'points': 5}
# alien_1 = {'color': 'żółty', 'points': 10}
# alien_2 = {'color': 'czerwony', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# Utworzenie pustej listy przeznaczonej do przechowywania obcych.
# aliens = []
# # Utworzenie 30 zielonych obcych.
# for alien_number in range(30):
#     new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
#     aliens.append(new_alien)

# # Wyświetlenie pierwszych pięciu obcych.
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Wyświetlenie całkowitej liczby utworzonych obcych.
# print("Całkowita liczba obcych: " + str(len(aliens)))

# Utworzenie pustej listy przeznaczonej do przechowywania obcych.
aliens = []
# Utworzenie 30 zielonych obcych.
# for alien_number in range(30):
#     new_alien = {'color': 'żółty', 'points': 10, 'speed': 'średnio'}
#     aliens.append(new_alien)

# for alien in aliens[0:3]:
#     if alien['color'] == 'zielony':
#         alien['color'] = 'żółty'
#         alien['speed'] = 'średnio'
#         alien['points'] = 10
#     elif alien['color'] == 'żółty':
#         alien['color'] = 'czerwony'
#         alien['speed'] = 'szybko'
#         alien['points'] = 15

# # Wyświetlenie pierwszych pięciu obcych:
# for alien in aliens[:5]:
#     print(alien)
# print("...")

########## lista w słowniku
# Przechowywanie informacji o pizzy zamawianej przez klienta.
# pizza = {
#     'crust': 'grubym',
#     'toppings': ['pieczarki', 'podwójny ser'],
# }
# # Podsumowanie zamówienia.
# print("Zamówiłeś pizzę na " + pizza['crust'] + " cieście " +
#       "wraz z następującymi dodatkami:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'janek': ['python', 'ruby'],
#     'sara': ['c'],
#     'edward': ['ruby', 'go'],
#     'paweł': ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():
#     print("\n Ulubione języki programowania użytkownika " + name.title() + " to:")
#     for language in languages:
#         print("\t" + language.title())

########## słownik w słowniku
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'maria',
#         'last': 'skłodowska-curie',
#         'location': 'paryż',
#     },
# }
# for username, user_info in users.items():
#     print("\nNazwa użytkownika: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#     print("\tImię i nazwisko: " + full_name.title())
#     print("\tMiejscowość: " + location.title())

####################################### DO ZROBIENIA ########################################