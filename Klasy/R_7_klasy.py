########## KLASY rodział 9
# class Dog():
#     """Prosta próba modelowania psa. """
#     def __init__(self, name, age): #metoda " __init__ ""
#         """Inicjalizacja atrybutów 'name' i 'age' """
#         self.name = name
#         self.age = age

#     def sit(self):                                              # metoda " sit() "
#         """Symulacja, że pies siada po otrzymaniu polecenia."""
#         print(self.name.title() + " teraz siedzi.")
#     def roll_over(self):                                        # metoda " roll_over() ""
#         """Symulacja, że pies kładzie się na plecy po otrzrymaniu polecenia"""
#         print(self.name.title() + " teraz położył sie na plecy!")

# # utworzenie egzemplarza na podstawie klasy
# my_dog = Dog('willie', 6) #pierwszy egzemplarz klasy " Dog "
# print("Mój pies ma na imię " + my_dog.name.title() + '.') # uzyskanie dostępu do trybutu " my_dog.name "
# print("Mój pies ma " + str(my_dog.age) + " lat.")
# # wywołanie metod
# my_dog.sit()
# my_dog.roll_over()

# ########## utworzenie wielu egzemplarzy
# your_dog = Dog('lucy', 5)# drugi egzemplarz kalsy " Dog "
# print("Twój pies ma na imię " + your_dog.name.title() + ".")
# print("Twój pies ma " + str(your_dog.age) + " lat.")
# your_dog.sit()

########## praca z klasami i egzemplarzami
########## klasa Car
# class Car():
#     """Prosta próba do zaprezentowania samochodu"""
#     def __init__(self, make, model, year):
#         """Inicjalizaca atrybutów opisującychsamochód"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 #przypisanie atrybutowi wartości domyslnej
    
#     def get_descriptive_name(self):
#         """Zwrot elegancko sformatowanego opisu samochodu"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
    
#     def read_odometer(self):
#         """Wyświetla informację o przebiegu samochodu"""
#         print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")
    
#     def update_odometer(self, mileage):
#         """
#         Przypisanie podanej wartości licznikowi przebiegu samochodu.
#         Zmia zostanie odrzucona w przypadku próby cofnięcia licznika
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Nie można cofnąć licznika samochodu!")
#     def increment_odometer(self, kilometers):
#         """inkrementacja wartości licznika samochodu o podaną wartość"""
#         self.odometer_reading += kilometers

# my_new_car = Car('audi', 'a4', 2016)# egzamplarz nowego samochodu
# print(my_new_car.get_descriptive_name())
# #my_new_car.odometer_reading = 23  # bezposrednia modyfikacja wartości atrybutu
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

########## dziedziczenie
########## metoda " __init__ " w klasie potomnej


class Car():
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

class Battery():
    """Prosta próba modelowanie akumulatora samochodu elektrycznego."""
    def __init__(self, battery_size=70):
        """Inicjalizacja atrybutów akumulatora."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Wyswietlenie informacji o wielkości akumulatora"""
        print("Ten samochód ma akumulator o pojemności " + str(self.battery_size) + " kWh.")

class ElectrcCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzednej"""
        super().__init__(make, model, year)
        self.battery = Battery() # egzemplarz jako atrybut

########## definiowanie atrybutów i metod dla klasy potomnej
    # def describe_battery(self):
    #     """Wyświetlenie informacji o wielkości akumulatora"""
    #     print("Ten samochód ma akumulator o pojemności " + str(self.battery_size) + " kWh.")

my_tesla = ElectrcCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
