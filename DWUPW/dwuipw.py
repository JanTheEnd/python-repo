# message = input("Powiedz mi cos o sobie:")
# print(message)

# name = input("Podaj swoje imie:")
# print("Witaj " + name + "!")
# surneme = input("Podaj swoje nazwisko: ")
# print(surneme)

########## uzycie funkcji int() do akceptowania liczbowych danych wejściowych
# height = input("Ile masz wzrostu (w centymetrach)?")
# height = int(height)
# if height >= 90:
#     print("\nJesteś wystarczająco wysoki na przejażdżkę!")
# else:
#     print("\nBędziesz mógł sie przejechać gdy nieco urośniesz.")

########## operator modulo
# number = input("Podaj liczbę, aby dowiedzieć się czy jest parzysta czy nieparzysta:")
# number = int(number)
# if number % 2 == 0:
#     print("\nLiczba " + str(number) + " jest parzysta.")
# else:
#    print("\nLiczba " + str(number) + " jest nieparzysta.")

########### wprowadzenie do petli !!!while!!!
# current_number = 10
# while current_number >= 1:
#     print(current_number)
#     current_number -= 1

# while current_number <= 10:
#     print(current_number)
#     current_number += 1

########## umozliwienie uzytkownikowi podjęcie decyzji o zakonczeniu działania
# prompt = "\nPowiedz mi coś o sobie, a wyswietlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakoczyć działanie programu."
# message = ""
# while message != 'koniec':
#     message = input(prompt)
#     print(message)
# print("koniec dzialania programu")

# prompt = "\nPowiedz mi coś o sobie, a wyswietlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakoczyć działanie programu."
# message = ""
# while message != 'koniec':
#     message = input(prompt)
#     if message != 'koniec':
#         print(message)

########## użycie flagi
# prompt = "\nPowiedz mi coś o sobie, a wyswietlę to na ekranie:"
# prompt += "\nNapisz 'koniec', aby zakoczyć działanie programu."
# active = True
# while active:
#     message = input(prompt)

#     if message == 'koniec':
#         active = False
#     else:
#         print(message)

########## uzycie polecenia << breake >> do opuszczenie pętli
# prompt = "\nPodaj nazwy miest, które chciałbys odwiedzić:"
# prompt += "\n(Gdy zakoczysz podawanie miast, napisz 'koniec.)"
# while True:
#     city = input(prompt)

#     if city == 'koniec':
#         break
#     else:
#         print("Chciałbym odzwiedzić " + city.title() + '!')

########## uzycie polecenie << continue >> w pętli  
# current_number = 0     
# while current_number < 10:
#     current_number +=1
#     if current_number % 2 ==0:
#         continue

#     print(current_number)

########## unikanie pętli działającej w nieskoczoność
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

########## uzycie petli while wraz z listami i słownikami
########## przenoszenie elementówz jednej listy na drugą
# rozpoczynamy od użytkowników, którzy mają byc zweryfikowani
# tworzymy tez pusta liste do przechowywania zweryfikowanych uzytkowników

# uncofirmed_users = ['alicja', 'bartek', 'katarzyna'] 
# confirmed_users = []
# # weryfikujemy poszczególnych uzytkowników, dopuki lista nie bedzie pusta.
# # kazdego zweryfikowanego użytkownika przenosimy na oddzielną listę
# while uncofirmed_users:
#     current_user = uncofirmed_users.pop()

#     print("Weryfikacja użytkownika:" + current_user.title())
#     confirmed_users.append(current_user)
# # wyswietlenie wszystkich zweryfikowanych uzytkowników
# print("\nZweryfikowano wymienionych poniżej uzytkowników:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

########## usuwanie z listy wszystkich egzemplarzy okreslonej wartości
# pets = ['pies', 'kot', 'pies', 'zlota rybka', 'kot', 'krolik', 'kot']
# print(pets)
# while 'kot' in pets:
#     pets.remove('kot')
# print(pets)

########## umiesczenie w słowniku danych wejściowych wprowadzonych prze uzytkownika
responses = {}
# ustawienie flagi czy ankieta jest aktywna.
polling_active = True
while polling_active:
    # prośba o podanie imienia uczetsnika ankiety oraz odpowiedzi na pytanie
    name = input("\n Jak masz na imię?")
    response = input("Na który szczyt chcialbyś się wspiąć pewnego dnia? ")

    # umieszczenie odpowiedzi w słowniku:
    responses[name] = response

    # ustalenie, czy ktokolwiek chce jescze wziąć udział w ankiecie.
    repeat = input("Czy ktokolwiek inny chce jeszcze wziąć udział w ankiecie? (tak/nie)")
    if repeat == 'nie':
        polling_active = False

# ankieta została zakoczona i wyswietlamy jej wyniki
print("\n---Wyniki ankiety---")
for name, response in responses.items():
    print(name.title() + " chciałby się wspiąć na " + response.title() + ".")
