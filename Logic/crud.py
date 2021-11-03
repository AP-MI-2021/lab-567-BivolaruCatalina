from Domain.vanzare import *


def create(lista_vanzari: list, _id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
    carte = getNewSell(_id, _titlu, _gen, _pret, _reducere)
    """
    lista_carti.append(carte)
"""
    return lista_vanzari + [carte]


def read(lista_vanzari: list, id_carte: int = None):
    carte_gasita = None

    if id_carte is None:
        return lista_vanzari

    for carte in lista_vanzari:
        if get_id(carte) == id_carte:
            carte_gasita = carte

    return carte_gasita


def update(lista_vanzari, new_book):
    result_list = []

    for carte in lista_vanzari:
        if get_id(carte) == get_id(new_book):
            result_list.append(new_book)
        else:
            result_list.append(carte)

    return result_list


def delete(lista_vanzari: list, id_carte: int):
    result = []

    for carte in lista_vanzari:
        if not get_id(carte) == id_carte:
            result.append(carte)

    return result