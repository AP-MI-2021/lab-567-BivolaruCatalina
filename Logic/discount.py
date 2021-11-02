from Domain.carte import get_discount, get_price, getNewBook, get_id, get_title, get_genre
from Logic.crud import delete


def reducere_carte(lista_carti):
    result_list = []
    for carte in lista_carti:
            if get_discount(carte) == "silver":
                delete(lista_carti, get_id(carte))
                pret = get_price(carte) - get_price(carte)/20
            elif get_discount(carte) == "gold":
                pret = get_price(carte) - get_price(carte)/10
            result_list.append(getNewBook(get_id(carte),
                               get_title(carte),
                               get_genre(carte),
                               pret,
                               get_discount(carte)))
            if get_discount(carte) == "none":
                result_list.append(carte)
    return result_list
