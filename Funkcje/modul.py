########## moduł funkcji
def make_pizza(size, *toppings):
    """Podsumowanie informacjie o przygotowanej pizzy"""
    print("\nPrzygotowuje pizze o wielkości " + str(size) + "cm, z nastepującymi dodatkami:")
    for topping in toppings:
        print("- " + topping)
