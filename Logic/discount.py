from Domain.carte import get_discount, get_price, getNewBook, get_id, get_title, get_genre


def reducere_carte(lista_carti):
    result_list = []
    for carte in lista_carti:
        if not get_discount(carte) == "none":
            if get_discount(carte) == "silver":
                pret = get_price(carte) - get_price(carte)/20
            """
            carte_aux = getNewBook(get_id(carte), get_title(carte), get_genre(carte), pret, get_discount(carte))
            """
            else:
                pret = get_price(carte) - get_price(carte)/ 10
            result_list.append(getNewBook(get_id(carte),
                               get_title(carte),
                               get_genre(carte),
                               pret,
                               get_discount(carte)))
        else:
            result_list.append(carte)
    return result_list
