########## WPROWADZENIE DO LIST rozdział 3

########## Uzyskanie dostepu,numerowanie indeksu, uzycie poszczegolnych wartosci listy
# bicycles = ['trekingowy','gorski','szosowy']
# print(bicycles) #wypisuje listę 
# print(bicycles[0]) #odwołuje się do indeksu zerowego tj. pierwszego elementu listy
# print(bicycles[1])
# print(bicycles[2])
# print(bicycles[0].title())
# print(bicycles[-1])
# print(bicycles[-2])

# message ="Moim pierwszym rowerem byl rower " + bicycles[0].upper() +"."
# print(message) 
# # zmienianie, dodawanie i usuwanie elementów
# # modyfikowanie elementów na liście
# motorcycles = ['honda','yamaha','suzuki',]
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles) 

########## dodawanie elementów do listy
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# motorcycles.insert(0,'ducati')
# print(motorcycles)

########## usuwanie elementu z listy za pomocą polecenia del
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[2]
# print(motorcycles)

########## usuwanie za pomocą metody pop()
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# last_owned = motorcycles.pop()
# print("Ostatnio zakupiony przeze mnie motocykl to " + last_owned.title() + ".")

############ Usunięcie elementu z dowolnego miejsca na liście
# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print('Moj pierwszy motocykl to ' + first_owned.title() + '.')
# print(motorcycles)

############ Usunięcie elementu na podstawie jego wartości metoda remove()
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nMotocykl " + too_expensive.title() + "jest zbyt drogi dla mnie.")

############ Organizacja listy - trwałe sortowanie listy za pomocą metody sort()
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.sort()
# print(cars)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

############ Tymczasowe sortowanie listy za pomocą funkcji sorted()
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Oto lista poczatkowa:")
# print(cars)
# print("\n Oto lista posortowana:")
# print(sorted(cars))
# print("\nOto ponownie lista poczatkowa:")
# print(cars)

########### Wświetlanie listy w odwrotnej kolejności
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.reverse()
# print(cars)

############ Określenie wielkości listy
# cars = ['bmw', 'audi', 'toyota', 'subaru' 'syrenka']
# print(len(cars))

########## PRACA Z LISTĄ rozdział 4
########## iteracja przez całą listę
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician)

########## wykonywanie wiekszej liczby zadan w pętli for
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician.title() + ", to była doskonała sztuczka!")

# magicians = ['alicja', 'dawid', 'karolina'] 
# for magician in magicians: 
#     print(magician.title() + ", to była doskonała sztuczka!")  
#     print("Nie mogę się doczekać Twojej kolejnej sztuczki, "
#           + magician.title() + ".\n")

########## wykonywanie operacji po petli for
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician.title() + ", to była doskonała sztuczka!")
#     print("Nie mogę się doczekać Twojej kolejnej sztuczki, " + magician.title() + ".\n")

# print("Dziękuję wszystkim. To był naprawdę wspaniały występ!")

########## brak wcięcia dodatkowych wierszy
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician.title() + ", to była doskonała sztuczka!")
# print("Nie mogę się doczekać Twojej kolejnej sztuczki, " + magician.title() + ".\n")

########## niepotrzebne wcięcie błąd 
# message = "Witaj, świecie Pythona!"
#     print(message) 

########## niepotrzebne wcięcie w pętli
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician.title() + ", to była doskonała sztuczka!")
#     print("Nie mogę się doczekać Twojej kolejnej sztuczki, " + magician.title() + ".\n")

#     print("Dziękuję wszystkim. To był naprawdę wspaniały występ!") # niepotrzebne wcięcie

########## brak dwukropka wygenerowanie błędu składni
# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians # brak dwukrpoka
#     print(magician)

########## tworzenie list liczbowych
# użycie funkcji range()
# for value in range(1, 5):
#     print(value)

# for value in range(1, 6):
#     print(value)

########## użycie funkcji range() do utworzenia listy liczb
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2)) #pominięcie liczb w podanym zakresie
# print(even_numbers)
# lista kwadratów pierwszych 10 liczb
# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
# print(squares)

# zwięzła forma
# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
# print(squares)

########## proste dane statystyczne dotyczace liczb
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

########## lista składana
# squares = [value**2 for value in range(1, 11)]
# print(squares)

########## praca z fragmentami list
# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print(players[0:3])

# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print(players[1:4])

# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print(players[:4])

# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print(players[2:])

# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print(players[-3:])

########## iteracja przez wycinek
# players = ['karol', 'martyna', 'michał', 'florian', 'ela']
# print("Oto trzech pierwszych graczy naszej drużyny:")
# for player in players[:3]:
#     print(player.title())

########## kopiowanie listy
# my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
# friend_foods = my_foods[:]
# print("Moje ulubione potrawy to:")
# print(my_foods)
# print("\nUlubione potrawy mojego przyjaciela to:")
# print(friend_foods)

# my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
# friend_foods = my_foods[:]
# my_foods.append('cannolo')
# friend_foods.append('lody')
# print("Moje ulubione potrawy to:")
# print(my_foods)
# print("\nUlubione potrawy mojego przyjaciela to:")
# print(friend_foods)

# my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
# # Poniższe rozwiązanie nie działa.
# friend_foods = my_foods
# my_foods.append('cannolo')
# friend_foods.append('lody')
# print("Moje ulubione potrawy to:")
# print(my_foods)
# print("\nUlubione potrawy mojego przyjaciela to:")
# print(friend_foods)

########## krotka
# definiowanie krotki
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200, 50) 
# dimensions[0] = 250 # zmiana wartości krotki wygeneruje błąd

########## iteracja przez wszystkie wartości krotki
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

########## nadpisanie krotki
# dimensions = (200, 50)
# print("Wymiary początkowe:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nWymiary po modyfikacji:")
# for dimension in dimensions:
#     print(dimension)
##################################### ZRÓB TO SAM ############################################