from Domain.vanzare import get_price, get_id
from Logic.crud import delete


def ordonare_pret(lista_vanzari: list) -> list:
    """
    Ordoneaza lista dupa pretul cartilor
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: lista ordonata
    """
    result = []
    i = 0
    while lista_vanzari:
        cmm_pret = get_price(lista_vanzari[i])
        vanzare = lista_vanzari[i]
        for j in range(i+1, len(lista_vanzari)):
            if get_price(lista_vanzari[j]) < cmm_pret and not lista_vanzari[j] in result:
                vanzare = lista_vanzari[j]
                cmm_pret = get_price(lista_vanzari[j])
        result.append(vanzare)
        lista_vanzari = delete(lista_vanzari, get_id(vanzare))
    return result

