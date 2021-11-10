from Logic.crud import create
from UserInterface.console import handle_new_list, handle_undo, handle_redo


def test_undo_redo():
    lista_vanzari = []
    list_versions = [lista_vanzari]
    current_version = 0
    lista_vanzari = create(lista_vanzari, 1, "Carte 1", "psihologic", 63.70, "silver")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
    lista_vanzari = create(lista_vanzari, 2, "Carte 2", "thriller", 52.50, "gold")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
    lista_vanzari = create(lista_vanzari, 3, "Carte 3", "informativ", 49, "none")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
    lista_vanzari = create(lista_vanzari, 4, "Carte 4", "romantic", 45.90, "gold")
    list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
    lista_vanzari = create(lista_vanzari, 5, "Carte 5", "comedie", 53.80, "none")
    lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 4
    lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 5
    lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 4
    lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 3
    lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 2
    lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 3
    lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 4
    lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
    assert len(lista_vanzari) == 5


test_undo_redo()