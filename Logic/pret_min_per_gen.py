from Domain.vanzare import get_price, get_genre
from Logic.ordonare_vanzari import ordonare_pret


def fiecare_gen(lista_vanzari):
    genuri = []
    for carte in lista_vanzari:
        if not get_genre(carte) in genuri:
            genuri.append(get_genre(carte))
    return genuri


def pret_min(lista_vanzari):
    lista_vanzari = ordonare_pret(lista_vanzari)
    genuri = fiecare_gen(lista_vanzari)
    result1 = []
    for gen in genuri:
        min1 = get_price(lista_vanzari[len(lista_vanzari) - 1])
        for carte in lista_vanzari:
            if gen == get_genre(carte) and get_price(carte) < min1:
                min1 = get_price(carte)
        result1.append(tuple((gen, min1)))

    return result1
