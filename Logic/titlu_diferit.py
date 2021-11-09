from Domain.vanzare import get_genre, get_title
from Logic.pret_min_per_gen import fiecare_gen


def titlu_diferit(lista_vanzari):
    genuri = fiecare_gen(lista_vanzari)
    carti_unice = []
    titlu_unic = []
    result = []

    for carte in lista_vanzari:
        if not get_title(carte) in titlu_unic:
            carti_unice.append(carte)
            titlu_unic.append(get_title(carte))

    for gen in genuri:
        contor = 0
        for carte in carti_unice:
            if get_genre(carte) == gen:
                contor = contor + 1
        result.append(tuple((gen, contor)))

    return result
