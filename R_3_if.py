############# KONSTRUKCJA IF rozdział 5
########## prosty przykład
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

########## test warunkowy sprawdzenie równości
# car = 'bmw'
# print(car)
# car == 'bmw'
# print(car)

# car = 'audi'
# print(car)
# car == 'bmw'
# if car == 'bmw':
#     print(car)
# else:
#     print('FALSE')

########## sprawdzenie nierówności
# requested_topping = 'pieczarki'
# if requested_topping != 'anchois':
#     print("Proszę o anchois!")

########## porównania liczbowe
# answer = 17
# if answer != 42:
#     print("To nie jest prawidłowa odpowiedź. Proszę spróbuj ponownie!")

########## sprawdenie wielu warunków
# age_0 = 22
# age_1 = 18
# print("Przypadek pierwszy")
# print(age_0 >= 21 and age_1 >= 21)

# age_1 = 22
# print("\nPrzypadek drugi")
# print(age_0 >= 21 and age_1 >= 21)

#użycie słowa kluczowego "or" do sprawdzania wielu warunków
# age_0 = 22
# age_1 = 18
# print("\nPrzypadek I")
# print(age_0 >= 21 or age_1 >= 21)

# age_0 = 18
# print("\nPrzypadek II")
# print(age_0 >= 21 or age_1 >= 21)

########## sprawdzenie czy wartość znajduje sie na liscie
# requested_toppings = ['pieczarki', 'cebula', 'ananas']
# print("prawda")
# print('pieczarki' in requested_toppings)
# print("\nfałsz")
# print('pepperoni' in requested_toppings)

########## sprawdzenie czy wartość nie znajduje sie na liście
# banned_users = ['andrzej', 'karolina', 'dawid']
# user = 'maria'
# if user not in banned_users:
#     print(user.title() + ", możesz opublikować odpowiedź, jeśli chcesz.")

########## proste polecenia "if"
# age = 19
# if age >= 18:
#     print("Możesz wziąć udział w głosowaniu!")

# age = 19
# if age >= 18:
#     print("Możesz wziąć udział w głosowaniu!")
#     print("Czy zarejestrowałeś się już, aby móc głosować?")

########## poelcenia " if-else "
# age = 17
# if age >= 18:
#     print("Możesz wziąć udział w głosowaniu!")
#     print("Czy zarejestrowałeś się już, aby móc głosować?")
# else:
#     print("Przykro nam, ale jesteś zbyt młody, aby głosować.")
#     print("Możesz się zarejestrować po ukończeniu 18 lat!")

########## łancuch " if-elif-else "
# age = 12
# if age < 4:
#     print("Cena biletu wstępu wynosi 0 zł.")
# elif age < 18:
#     print("Cena biletu wstępu wynosi 5 zł.")
# else:
#     print("Cena biletu wstępu wynosi 10 zł.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print("Cena biletu wstępu wynosi " + str(price) + " zł.")

########## użycie wielu bloków " elif "
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
# print("Cena biletu wstępu wynosi " + str(price) + " zł.")

########## pominięcie bloku " else "
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print("Cena biletu wstępu wynosi " + str(price) + " zł.")

########## sprawdzenie wielu warunków
# requested_toppings = ['pieczarki', 'podwójny ser']
# if 'pieczarki' in requested_toppings:
#     print("Dodaję pieczarki.")
# if 'pepperoni' in requested_toppings:
#     print("Dodaję pepperoni.")
# if 'podwójny ser' in requested_toppings:
#     print("Dodaję podwójny ser.")

# print("\nTwoja pizza jest już gotowa!")

# requested_toppings = ['pieczarki', 'podwójny ser']  # kod nie działa prawidłowo " if-elif-else"
# if 'pieczarki' in requested_toppings:
#     print("Dodaję pieczarki.")
# elif 'pepperoni' in requested_toppings:
#     print("Dodaję pepperoni.")
# elif 'podwójny ser' in requested_toppings:
#     print("Dodaję podwójny ser.")
# print("\nTwoja pizza jest już gotowa!")

########## uzywanie polecen " if " z listami
########## sprawdzenie pod katem wartości specjalnych
# requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']
# for requested_topping in requested_toppings:
#     print("Dodaję " + requested_topping + ".")
# print("\nTwoja pizza jest już gotowa!")

# requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']
# for requested_topping in requested_toppings:
#     if requested_topping == 'boczek': # brak jednego składniak polecenie " if " obsłuży proble
#         print("Przepraszamy, ale obecnie nie mamy boczku.")
#     else:
#         print("Dodaję " + requested_topping + ".")
# print("\nTwoja pizza jest już gotowa!")

########## sprawdzenie czy lista nie jest pusta
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Dodaję " + requested_topping + ".")
#     print("\nTwoja pizza jest już gotowa!")
# else:
#     print("Czy jesteś pewien, że chcesz pizzę bez dodatków?")

########## użycie wielu list
# available_toppings = ['pieczarki', 'oliwki', 'boczek',
#                       'pepperoni', 'ananas', 'podwójny ser']
# requested_toppings = ['pieczarki', 'frytki', 'podwójny ser']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Dodaję " + requested_topping + ".")
#     else:
#         print("Przepraszamy, ale obecnie nie mamy dodatku " + requested_topping + ".")

# print("\nTwoja pizza jest już gotowa!")

############################### ZRÓB TO SAM #############################################