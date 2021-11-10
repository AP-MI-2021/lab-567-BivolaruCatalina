from Logic.discount import reducere_carte
from Logic.modificare_gen import schimbare_gen
from Logic.ordonare_vanzari import ordonare_pret
from Logic.pret_min_per_gen import pret_min
from Logic.titlu_diferit import titlu_diferit


def test_reducere_carte():
    assert reducere_carte([(1, "Lama", "animals", 67.50, "silver")]) == [(1, "Lama", "animals", 64.125, "silver")]
    assert reducere_carte([(1, "Lama", "animals", 67.50, "gold")]) == [(1, "Lama", "animals", 60.75, "gold")]
    assert reducere_carte([(1, "Lama", "animals", 67.50, "none")]) == [(1, "Lama", "animals", 67.50, "none")]


def test_schimbare_gen():
    assert schimbare_gen([(1, "Lama", "animals", 67.50, "silver")], "Lama", "drama") == [(1, "Lama", "drama", 67.50, "silver")]
    assert schimbare_gen([(1, "Lama", "animals", 67.50, "silver"), (2, "Mana", "thriller", 67.50, "silver")], "Lama", "drama") == [(1, "Lama", "drama", 67.50, "silver")]


def test_ordonare_pret():
    assert ordonare_pret([(1, "Carte 1", "psihologic", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")]) == [(3, "Carte 3", "informativ", 49, "none"), (2, "Carte 2", "thriller", 52.50, "gold"), (1, "Carte 1", "psihologic", 63.70, "silver")]
    assert ordonare_pret([(1, "Carte 1", "psihologic", 52.50, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")]) == [(3, "Carte 3", "informativ", 49, "none"), (2, "Carte 2", "thriller", 52.50, "gold"), (1, "Carte 1", "psihologic", 63.70, "silver")]


def test_pret_min():
    assert pret_min([(1, "Carte 1", "psihologic", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")])) == [("psihologic", 63.70), ("thriller", 52.50), ("informativ", 49)]
    assert pret_min([(1, "Carte 1", "thriller", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")])) == [("thriller", 52.50), ("informativ", 49)]


def test_titlu_diferit():
    assert titlu_diferit([(1, "Carte 1", "psihologic", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")])) == [("psihologic", 1), ("thriller", 1), ("informativ", 1)]
    assert titlu_diferit([(1, "Carte 2", "thriller", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")])) == [("thriller", 1), ("informativ", 1)]
    assert pret_min([(1, "Carte 1", "thriller", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 3", "informativ", 49, "none")])) == [("thriller", 2), ("informativ", 1)]
    assert pret_min([(1, "Carte 2", "thriller", 63.70, "silver"), (2, "Carte 2", "thriller", 52.50, "gold"), (3, "Carte 2", "thriller", 49, "none")])) == [("thriller", 1)]


def test_functionalitati():
        test_reducere_carte()
        test_schimbare_gen()
        test_ordonare_pret()
        test_pret_min()
        test_titlu_diferit()
test_functionalitati()




