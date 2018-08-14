########### iteracja przez cała listę ##########

# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician)

# magicians = ['alicja', 'dawid', 'karolina']
# for magician in magicians:
#     print(magician.title() + ", to byla doskonala sztuczka!")
#     print()

# magicians = ['alicja', "dawiad", 'karolina']
# for magician in magicians:
#     print( magician.title() + ", to byla doskonala sztuczka!")
#     print("Nie moge doczekac sie Twojej kolejnej sztuczki, " + magician.title() + ".\n")

########## tworzenie list liczbowych ########
# użycie funkcji range()

# for value in range(1,6):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

# forma bardziej zwięzła
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
#     print(squares)

########### proste dane statystyczne #########
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

######### lista składana ###########
# squares = [value**2 for value in range(1,11)]
# print(squares)

######### praca z fargmentami listy #########
# players = ['karol', 'martyna', 'michal', 'florian', 'ela']
# print(players[0:3])
# print(players[1:4])
# print(players[2:])
# print(players[-3:])

########## iteracja przez wycinek ##########
# players = ['karol', 'martyna', 'michal', 'florian', 'ela']
# print("Oto trzech pierwszych graczy naszej druzyny:")
# for player in players[:3]:
#     print(player.title())

########## kopiowanie listy ###########
# my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
# friend_foods = my_foods[:]
# my_foods.append('cannolo')
# friend_foods.append('lody')
# print("Moje ulubione potrawy to:")
# print(my_foods)
# print("\nUlubione potrawy mojego przyjaciela to:")
# print(friend_foods)

########### krotka ##########
# dimensions = (200, 50)
# #dimensions[0] = 250 błąd !!!!!!!!!!! nie można zmienić wertości elementu krotki
# print(dimensions[0])
# print(dimensions[1])

########### iteracja przez wszystkie wartości krotki
# dimensions = (200, 50,12, 1123, 22, 125)
# for dimension in dimensions:
#     print(dimension)

########### nadpisanie krotki
# dimensions = (200, 50)
# print("Wymiary poczatkowe:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nWymiary po modyfikacji:")
# for dimension in dimensions:
#     print(dimension)
