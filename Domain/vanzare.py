def getNewSell(_id: int, _titlu: str, _gen: str, _pret: float, _reducere: str) -> tuple:
    book = tuple((_id, _titlu, _gen, _pret, _reducere))
    return book


def get_id(carte):
    return carte[0]


def get_title(carte):
    return carte[1]


def get_genre(carte):
    return carte[2]


def get_price(carte):
    return carte[3]


def get_discount(carte):
    return carte[4]


def get_sell_string(carte):
    return f'Cartea cu id-iul {get_id(carte)}, cu numele {get_title(carte)}, de gen {get_genre(carte)}, are pretul {get_price(carte)} si i se aplica reducerea de tip {get_discount(carte)}'
