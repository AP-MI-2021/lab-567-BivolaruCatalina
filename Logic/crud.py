from Domain.carte import getNewBook, get_id


def create(lista_carti: list, _id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
    carte = getNewBook(_id, _titlu, _gen, _pret, _reducere)
    """
    lista_carti.append(carte)
"""
    return lista_carti + [carte]


def read(lista_carti: list, id_carte: int = None):
    carte_gasita = None

    if id_carte is None:
        return lista_carti

    for carte in lista_carti:
        if get_id(carte) == id_carte:
            carte_gasita = carte

    return carte_gasita


def update(lista_carti, new_book):
    result_list = []

    for carte in lista_carti:
        if get_id(carte) == get_id(new_book):
            result_list.append(new_book)
        else:
            result_list.append(carte)

    return result_list


def delete(lista_carti: list, id_carte: int):
    result = []

    for carte in lista_carti:
        if not get_id(carte) == id_carte:
            result.append(carte)

    return result