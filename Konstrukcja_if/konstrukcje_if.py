# ########## prosty przykład
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# ######### test warunkowy
# car = 'bmw'
# car == 'bmw'
# print(car)

# car = 'audi'
# car == 'bmw'
# print(car)

# ######## ignorowanie wielkości liter podczas sprawdzania równości
# car = 'Audi'
# car == 'audi'
# print(car)

# car = 'Audi'
# car.lower() == 'audi'
# print(car)

# ######### sprawdzenie nierówności
# requested_topping = 'pieczarki'
# if requested_topping != 'anchois':
#     print("Prosze o anchois!")

# ######### porównania liczbowe
# answer = 17
# if answer != 42:
#     print("To nie jest prawidlowa odpowiedz. Prosze sprobuj ponownie")

# ######### sprawdzenie wielu warunków 
# ######### uzycie słowa kluczowego and do sprawdzenie wielu warunków
# age_0 = 22
# age_1 = 18
# if (age_0 >= 21) and (age_1 >= 21):
#     print(age_0, age_1)
# else:
#     print("Warunek jest nie prawdziwy FALSE")

# age_1 = 22
# if age_0 >= 21 and age_1 >= 21:
#     print(age_0, age_1, "\nWarunek spelniony")

# ######### sprawdzenie czy wartość znajduje się na liscie
# requested_toppings = ['pieczarki', 'cebula', 'ananas']
# if 'pieczarki' in requested_toppings:
#     print("Prawda")
# else:
#     print("Fałsz")

# ######### sprawdzenie, czy wartość nie znajduje się na liście
# banned_users = ['andrzej', 'karolina', 'dawid']
# user = 'maria'
# if user not in banned_users:
#     print(user.title() + ", mozesz opublikowac odpowiedz, jesli chcesz.")

# ######### proste polecenia if
# age = 19
# if age >= 18:
#     print("Mozesz wziac udzial w glosowaniu")
#     print("Czy zarejstrowales sie juz, aby moc glosowac??")

# ######### polecenie if-else
# age = 17
# if age >= 18:
#     print("Mozesz wziac udzial w glosowaniu")
#     print("Czy zarejstrowales sie juz, aby moc glosowac??")
# else:
#     print("Przykro nam, ale jestes zbyt mlody, aby glosowac")
#     print("Mozesz sie zarejestrowac po ukonczeniu 18 lat!")

# ######### lancuch if-elif-else
# age = 30
# if age < 4:
#     price = 0
#     #print("Cena biletu wstepu wynosi 0 zl") <-------- alternatywny zapis
# elif age < 18:
#     price = 5 # <------- zapis uproszcony
#     #print("Cena biletu wstepu wynosi 5 zl ")
# else:
#     price = 10
#     #print("Cena biletu wstepu wynosi 10 zl")
# print("Cena biletu wstepu wynosi " + str(price) + " zl.") # tylko jedna funkcja print()

# ######### uzycie wielu bloków elif
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else: 
#     price = 7
# print("Cena biletu wstepu wynosi " + str(price) + " zl.")

# ######### sprawdzenie wielu warunków
# requested_toppings = ['pieczarki', 'podwojny ser']
# if 'pieczarki' in requested_toppings:
#     print("Dodaj pieczarki")
# if 'pepperoni' in requested_toppings:
#     print("Dodaj pepperoni.")
# if 'podwojny ser' in requested_toppings:
#     print("Dodaj podwojny ser")
# print("\n Twoja pizza jest juz gotowa")

# ######### uzywanie polecen if z listami
# requseted_toppings = ['pieczarki', 'boczek', 'podwojny seer']
# for requseted_topping in requseted_toppings:
#     print("Dodaj " + requseted_topping + ".")
# print("Twoja pizza jest juz gotowa!")

# requested_toppings = ['pieczarki', 'boczek', 'podwojny seer']
# for requested_topping in requested_toppings:
#     if requested_topping == 'boczek': # <----------TRUE warunek spełniony
#         print("Przepraszamy, ale obecnie nie mamy boczku.")
#     else:
#         print("Dodaj " + requested_topping + ".")
# print("Twoja pizza jest juz gotowa!")

########## sprawdzenie czy lista nie jest pusta
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Dodaj " + requested_topping + ".") 
#     print("\nTwoja pizza jest juz gotowa!")
# else:
#     print("Czy jestes pewien, ze chcesz pizze bez dodatkow??")

########## uzycie wielu list
# available_toppings = ['pieczarki', 'oliwki', 'boczek', 'pepproni', 'ananas', 'podwojny ser']
# requested_toppings = ['pieczarki', 'frytki', 'podwojny ser']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Dodaje " + requested_topping + ".")
#     else:
#         print("Przepraszam, ale obecnie nie mamy dodatku " + requested_topping + '.')
