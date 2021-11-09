"""
from Domain.carte import getNewBook, get_book_string

carte1 = getNewBook(1, "Sherlock Holmes", "thriller", 49.60, "silver")
carte2 = getNewBook(2, "Pride and prejudice", "romance", 74.50, "gold")
carte3 = getNewBook(3, "Interpretarea viselor", "psihologic", 60, "none")

print(get_book_string(carte1))
print(get_book_string(carte2))
print(get_book_string(carte3))
"""

from Logic.crud import create, update, delete
from UserInterface.console import run_ui

lista = []

lista = create(lista, 1, "Sherlock Holmes", "thriller", 49.60, "silver")
lista = create(lista, 2, "Pride and prejudice", "romance", 74.50, "gold")
lista = create(lista, 3, "Interpretarea viselor", "psihologic", 60, "none")
lista = create(lista, 4, "Razboi si Pace", "psihologic", 78, "silver")
lista = create(lista, 5, "Pride and prejudice", "romance", 63.90, "gold")
lista = create(lista, 6, "Disparuti", "thriller", 60, "none")



run_ui(lista)
"""
print(lista)
carte = read(lista)

new_book = getNewBook(3, "Peace and War", "-", 60, "silver")
lista = update(lista, new_book)
print(lista)lista = delete(lista, 1)print(lista)
print(carte)
"""




