
def getNewBook(_id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
    book = {
        'id': _id,
        'titlu': _titlu,
        'gen': _gen,
        'pret': _pret,
        'reducere': _reducere
    }
    return book
"""
    def __init__(self, _id: int, _titlu: str, _gen: str, _pret: float, _reducere: str):
        self.id = _id
        self.titlu = _titlu
        self.gen = _gen
        self.pret = _pret
        self.reducere = _reducere
        print("S-a creat o carte.")
"""


def get_id(carte):
    return carte['id']


def get_title(carte):
    return carte['titlu']


def get_genre(carte):
    return carte['gen']


def get_price(carte):
    return carte['pret']


def get_discount(carte):
    return carte['reducere']


def get_book_string(carte):
    return f'Cartea cu id-iul {get_id(carte)}, cu numele {get_title(carte)}, de gen {get_genre(carte)}, are pretul {get_price(carte)} si i se aplica reducerea de tip {get_discount(carte)}'
