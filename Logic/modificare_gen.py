from Domain.vanzare import get_discount, get_price, get_id, get_title, getNewSell
from Logic.crud import update


def schimbare_gen(lista_carti, titlu):
    for carte in lista_carti:
        if get_title(carte) == titlu:
            gen = input('Introduceti noul gen al cartii: ')
            carte_noua = getNewSell(get_id(carte), get_title(carte), gen, get_price(carte), get_discount(carte))
            lista_carti = update(lista_carti, carte_noua)
    return lista_carti