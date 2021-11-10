from Domain.vanzare import *


def create(lista_vanzari: list, _id: int, _titlu: str, _gen: str, _pret: float, _reducere: str) -> list:
    """
    Crearea unei noi carti care va fi adaugata in lista de vanzari.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param _id:
    :param _titlu:
    :param _gen:
    :param _pret:
    :param _reducere:
    :return: returneaza lista lista_vanzari in urma adaugarii cartii create
    """
    carte = getNewSell(_id, _titlu, _gen, _pret, _reducere)
    return lista_vanzari + [carte]


def read(lista_vanzari: list, id_carte: int = None):
    """
    Gasirea unei carti in lista lista_vanzari.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param id_carte:
    :return: intreaga lista cu vanzari daca id-ul cartii nu este valabil si cartea cautata in cazul opus
    """
    carte_gasita = None

    if id_carte is None:
        return lista_vanzari

    for carte in lista_vanzari:
        if get_id(carte) == id_carte:
            carte_gasita = carte

    return carte_gasita


def update(lista_vanzari, new_book) -> list:
    """
    Modifica o carte prin inlocuirerea acesteia cu una noua.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param new_book: cartea noua
    :return: lista dupa modificarea cartii
    """
    result_list = []

    for carte in lista_vanzari:
        if get_id(carte) == get_id(new_book):
            result_list.append(new_book)
        else:
            result_list.append(carte)

    return result_list


def delete(lista_vanzari: list, id_carte: int) -> list:
    """
    Sterge o carte, a carei id este dat, din lista de vaznari
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param id_carte:
    :return: lista dupa stergerea cartii
    """
    result = []

    for carte in lista_vanzari:
        if not get_id(carte) == id_carte:
            result.append(carte)

    return result
