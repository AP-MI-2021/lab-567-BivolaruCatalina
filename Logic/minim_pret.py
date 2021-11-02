from Domain.carte import get_price, get_discount


def pret_mini(lista_carti):
    mini1 = get_price(lista_carti[0])
    mini2 = get_price(lista_carti[0])
    mini3 = get_price(lista_carti[0])
    for carte in lista_carti:
        if get_price(carte) < mini1 and get_discount(carte) == "gold":
            mini1 = get_price(carte)
        elif get_price(carte) < mini2 and get_discount(carte) == "silver":
            mini2 = get_discount(carte)
        elif get_price(carte) < mini3 and get_discount(carte) == "none":
