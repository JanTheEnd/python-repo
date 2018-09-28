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
