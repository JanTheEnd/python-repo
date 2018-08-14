""" # ZMIANA WIELKOŚCI LITER
name = 'jan kowalski' # pierwsze litery duże
print(name.title())

name = "Jan Kowalski"
print(name.upper()) # wszystkie litery duże
print(name.lower()) # wszystkie litery małe

# ŁĄCZENIE CIAGÓW TEKSTOWYCH

first_name = "jan"
last_name = "kowalski"
full_name = first_name + " " + last_name
#print(full_name)
#print("Witaj, " + full_name.title() + "!")
massage = "Witaj, " + full_name.title() + "!" 
print(massage)
"""
# Dodawanie białych znaków do ciągów tekstowych za pomocą tabulatora i znaku nowego wiersza

""" print("Python")
print("\tPython")# \t tabulator

print("Jezyki: \nPython\nC\nJavaScript") # \n znak nowego wiersza
print("Jezyki: \n\tPython\n\tC\n\tJavaScript")
"""
# Usuwanie białych znków

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip() # metoda usuwająca białe znaki po prawej stronie ciagu tekstowego
print(favorite_language)
favorite_language = favorite_language.rstrip() # sposób na usunięcie na trwałe białego znaku
print(favorite_language)

favorite_language = ' python'
favorite_language.lstrip() # metoda usuwająca białe znaki po lewej stronie ciagu tekstowego
print(favorite_language)





