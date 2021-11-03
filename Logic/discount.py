from Domain.vanzare import get_discount, get_price, getNewSell, get_id, get_title, get_genre
from Logic.crud import update


def reducere_carte(lista_carti):
    for carte in lista_carti:
            if get_discount(carte) == "silver":
                pret = get_price(carte) - get_price(carte)/20
                carte_noua = getNewSell(get_id(carte), get_title(carte), get_genre(carte), pret, get_discount(carte))
                lista_carti = update(lista_carti, carte_noua)
            elif get_discount(carte) == "gold":
                pret = get_price(carte) - get_price(carte) / 10
                carte_noua = getNewSell(get_id(carte), get_title(carte), get_genre(carte), pret, get_discount(carte))
                lista_carti = update(lista_carti, carte_noua)
    return lista_carti
