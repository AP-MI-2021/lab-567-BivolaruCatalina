from Domain.vanzare import *
from Logic.crud import create, read, update, delete


def get_data():
    return [
    getNewSell(1, "Carte 1", "psihologic", 63.70, "silver"),
    getNewSell(2, "Carte 2", "thriller", 52.50, "gold"),
    getNewSell(3, "Carte 3", "informativ", 49, "none"),
    getNewSell(4, "Carte 4", "romantic", 45.90, "gold"),
    getNewSell(5, "Carte 5", "comedie", 53.80, "none")
    ]


def test_create():
    lista = get_data()
    lista_noua = get_data()
    new_book = getNewSell(6, "Carte 6", "psihologic", 24.40, "silver")
    lista = create(lista, 6, "Carte 6", "psihologic", 24.40, "silver")

    assert len(lista) == len(lista_noua) + 1
    assert new_book in lista


def test_read():
    lista = get_data()
    carte_cautata = lista[4]
    carte_gasita = read(lista, 5)

    assert carte_gasita == carte_cautata
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    lista_aux = get_data()
    new_book = getNewSell(5, "Carte 6", "psihologic", 24.40, "silver")
    lista = update(lista, new_book)

    assert len(lista) == len(lista_aux)
    assert new_book in lista


def test_delete():
    lista = get_data()
    lista_noua = get_data()
    carte_eliminata = getNewSell(3, "Carte 3", "informativ", 49, "none")
    lista_noua = delete(lista_noua, 3)

    assert len(lista) == len(lista_noua) + 1
    assert not carte_eliminata in lista_noua


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


test_crud()
