########## DANE WEJŚCIOWE UŻYTKOWNIKA I PĘTLA WHILE rozdział 7
########## jak działa funkcja " input "
# message = input("Powiedz mi coś o sobie, a wyświetlę to na ekranie: ")
# print(message)

########## przygotowanie jasnych i zrozumiałych komunikatów
# name = input("Podaj swoje imię: ")
# print("Witaj, " + name + "!")

# prompt = "Jeżeli powiesz nam, kim jesteś, spersonalizujemy wyświetlany komunikat."
# prompt += "\nJak masz na imię? "
# name = input(prompt)
# print("\nWitaj, " + name + "!")

# age = input("Ile masz lat?")
# print(age)

# height = input("Ile masz wzrostu (w centymetrach)? ")
# height = int(height)
# if height >= 90:
#     print("\nJesteś wystarczająco wysoki na przejażdżkę!")
# else:
#     print("\nBędziesz mógł się przejechać, gdy nieco urośniesz.")

########## operator modulo
# modulo_0 = 4 % 3
# modulo_1 = 5 % 3
# modulo_2 = 6 % 3
# modulo_3 = 7 % 3
# print("Wynik działania modulo = ",modulo_0, modulo_1, modulo_2, modulo_3)

# number = input("Podaj liczbę, aby dowiedzieć się, czy jest parzysta czy nieparzysta: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nLiczba " + str(number) + " jest parzysta.")
# else:
#     print("\nLiczba " + str(number) + " jest nieparzysta.")

########## wprowadzenie do petli " while "
########## petla "while" w działaniu
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

########## umozliwienie użytkownikowi podjęcia decyzji o zakoczeniu działania programu
# prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "
# message = ""
# while message != 'koniec':
#     message = input(prompt)
#     print(message)

# prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "
# message = ""
# while message != 'koniec':
#     message = input(prompt)

#     if message != 'koniec':
#         print(message)

########## użycie flagi
# prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'koniec':
#         active = False
#     else:
#         print(message)

########## użycie polecenia " break " do opuszczenia pętli
# prompt = "\nPodaj nazwy miast, które chciałbyś odwiedzić:"
# prompt += "\n(Gdy zakończysz podawanie miast, napisz 'koniec'.) "
# while True:
#     city = input(prompt)

#     if city == 'koniec':
#         break
#     else:
#         print("Chciałbym odwiedzić " + city.title() + "!")

########## użycie polecenia " continue " w pętli
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

########## unikanie pętli działającej w nieskoczoność
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# TA PĘTLA DZIAŁA W NIESKOŃCZONOŚĆ !!! !!! !!!
# x = 1
# while x <= 5:
#     print(x)

########## użycie pętli while wraz z listami i słownikami
########## przenoszenie elementów z jednej listy na drugą
# Rozpoczynamy od użytkowników, którzy mają być zweryfikowani.
# Tworzymy też pustą listę przeznaczoną do przechowywania zweryfikowanych
# użytkowników.
unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []
# Weryfikujemy poszczególnych użytkowników, dopóki lista nie będzie pusta.
# Każdego zweryfikowanego użytkownika przenosimy na oddzielną listę.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Weryfikacja użytkownika: " + current_user.title())
#     confirmed_users.append(current_user)
# # Wyświetlenie wszystkich zweryfikowanych użytkowników.
# print("\nZweryfikowano wymienionych poniżej użytkowników:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

########## usuwanie z listy wszystkich egzemplarzy okreslonej wartości
# pets = ['pies', 'kot', 'pies', 'złota rybka', 'kot', 'królik', 'kot']
# print(pets)
# while 'kot' in pets:
#     pets.remove('kot')

# print(pets)

########## Umieszczenie w słowniku danych wejściowych wprowadzonych przez użytkownika
# responses = {}
# # Ustawienie flagi wskazującej, czy ankieta jest aktywna.
# polling_active = True
# while polling_active:
#     # Prośba o podanie imienia uczestnika ankiety oraz odpowiedzi na pytanie.
#     name = input("\nJak masz na imię? ")
#     response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia? ")

#     # Umieszczenie odpowiedzi w słowniku:
#     responses[name] = response

#     # Ustalenie, czy ktokolwiek jeszcze chce wziąć udział w ankiecie.
#     repeat = input(
#         "Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie) ")
#     if repeat == 'nie':
#         polling_active = False

# # Ankieta została zakończona i wyświetlamy jej wyniki.
# print("\n--- Wyniki ankiety ---")
# for name, response in responses.items():
#     print(name + " chciałby się wspiąć na " + response + ".")

####################################### ZRÓB TO SAM ##########################################
