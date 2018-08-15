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

############ Okreslenie wielkości listy
cars = ['bmw', 'audi', 'toyota', 'subaru' 'syrenka']
print(len(cars))