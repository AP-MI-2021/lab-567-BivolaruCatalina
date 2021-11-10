from Domain.vanzare import getNewSell, get_sell_string, get_price, get_genre, get_discount, get_title
from Logic.crud import create, read, update, delete
from Logic.discount import reducere_carte
from Logic.ordonare_vanzari import ordonare_pret
from Logic.modificare_gen import schimbare_gen
from  Logic.pret_min_per_gen import pret_min
from Logic.titlu_diferit import titlu_diferit
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print(
        """
        1. CRUD
        2. Aplicarea unui discount: 5% pentru reducere silver si 10% pentru reducere gold.
        3. Modificarea genului pentru un titlu dat.
        4. Determinarea pretului minim la fiecare gen.
        5. Ordonarea vanzarilor crescator dupa pret.
        6. Afisarea numarului de titluri distincte pentru fiecare gen.
        7. Undo
        8. Redo
        x. Iesire
        """
    )


def handle_add(lista_vanzari: list, list_versions: list, current_version: int):
    """
    Adauga elemente in lista_vanzari cu ajutorul functiei create din crud
    :param lista_vanzari: lista in cate va fi adaugat elementul
    :param list_versions: lista in care va fi salvata ultima versiuna a parametrului lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :return: lista_vanzari in urma apelarii functiei create, lista list_versions si contorul current_version
    """
    try:
        list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        reducere = input('Dati noul tip de reducere al cartii: ')
        return create(lista_vanzari, id_carte, titlu, gen, pret, reducere), list_versions, current_version
    except ValueError:
        print("Cel putin una dintre valorile introduse nu corespunde tipului de date declarat!!")


def handle_update(lista_vanzari: list, list_versions: list, current_version: int):
    """
    Mofica elemente in lista_vanzari cu ajutorul functiei create din crud
    :param lista_vanzari: lista in cate va fi modificat elementul
    :param list_versions: lista in care va fi salvata ultima versiuna a listei lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :return: lista_vanzari in urma apelarii functiei update, lista list_versions si contorul current_version
    """
    try:
        list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        reducere = input('Dati noul tip de reducere al cartii: ')
        return update(lista_vanzari, getNewSell(id_carte, titlu, gen,  pret, reducere)), list_versions, current_version
    except ValueError:
        print("Cel putin una dintre valorile introduse nu corespunde tipului de date declarat!!")


def handle_delete(lista_vanzari: list, list_versions: list, current_version: int):
    """
    Sterge elemente in lista_vanzari cu ajutorul functiei delete din crud
    :param lista_vanzari: lista din cate va fi sters elementul
    :param list_versions: lista in care va fi salvata ultima versiuna a listei lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :return: lista_vanzari in urma apelarii functiei delete, lista list_versions si contorul current_version
    """
    try:
        list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        id_carte = int(input('Dati id-ul cartii care se va sterge: '))
        lista_vanzari = delete(lista_vanzari, id_carte)
        print('Stergerea a fost efectuata cu succes.')
        return lista_vanzari, list_versions, current_version
    except ValueError:
        print("Id-ul introdus nu este de tipul int!!")


def handle_show_all(lista_vanzari: list):
    """
    Afisarea intregii liste de vanzari
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: nu returneaza nimic
    """
    for carte in lista_vanzari:
        print(get_sell_string(carte))


def handle_show_details(lista_vanzari: list):
    """
    Afiseaza detalii despre o anumita carte.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: nu returneaza nimic
    """
    try:
        id_carte = int(input('Dati id-ul cartii pentru care doriti detalii: '))
        vanzare = read(lista_vanzari, id_carte)
        print(f'Titlu: {get_title(vanzare)}')
        print(f'Gen: {get_genre(vanzare)}')
        print(f'Pret: {get_price(vanzare)}')
        print(f'Tip reducere: {get_discount(vanzare)}')
    except ValueError:
        print("Id-ul introdus nu este de tipul int!!")


def handle_reducere(lista_vanzari: list) -> list:
    """
    Apeleaza functia oentru aplicarea discountului fiecarei carti.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: lista dupa modificarea acesteia
    """
    lista_vanzari = reducere_carte(lista_vanzari)
    return lista_vanzari


def handle_schimbare_gen(lista_vanzari: list) -> list:
    """
    Apeleaza functia pentru sichimbarea genului unei cartii a carei titlu si gen nou sunt date.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: lista dupa modificarea acesteia
    """
    titlu = input('Introduceti titlul carti ce va fi schimbata: ')
    gen_nou = input('Introduceti noul gen al cartii: ')
    lista_vanzari = schimbare_gen(lista_vanzari, titlu, gen_nou)
    return lista_vanzari


def handle_ordonare_pret(lista_vanzari: list) -> list:
    """
    Apeleaza functia pentru ordonarea crescatoare a vanzarilor in functie de pret.
    :param lista_vanzari:  lista in care se afla toate vanzarile
    :return: lista dupa modificarea acesteia
    """
    lista_vanzari = ordonare_pret(lista_vanzari)
    return lista_vanzari


def handle_pret_minim(lista_vanzari: list) -> list:
    """
     Apeleaza functia pentru obtinerea pretului minim pentru fiecare gen.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: lista in care se afla fiecare gen si pretul cel mai mic intalnit la o carte cu genul respectiv
    """
    result = pret_min(lista_vanzari)
    return result


def handle_titlu_diferit(lista_vanzati: list) -> list:
    """
    Apeleaza functia pentru obtinerea numarului de carti diferite pentru fiecare gen.
    :param lista_vanzati:
    :return: lista in care se afla fiecare gen si numarul de carti cu genul respectiv
    """
    result = titlu_diferit(lista_vanzati)
    return result


def handle_undo(lista_vanzari: list, list_versions: list, current_version: int):
    """
    Apeleaza functia de undo.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param list_versions: lista in care va fi salvata ultima versiuna a listei lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :return: lista_vanzari in urma apelarii functiei do_undo si contorul current_version
    """
    lista_vanzari, current_version = do_undo(list_versions, current_version)
    return lista_vanzari, current_version


def handle_redo(lista_vanzari, list_versions, current_version):
    """
    Apeleaza functia de redo.
    :param lista_vanzari: lista in care se afla toate vanzarile
    :param list_versions: lista in care va fi salvata ultima versiuna a listei lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :return: lista_vanzari in urma apelarii functiei do_redo si contorul current_version
    """
    lista_vanzari, current_version = do_redo(list_versions, current_version)
    return lista_vanzari, current_version


def handle_new_list(list_versions: list, current_version: int, lista_vanzari: list):
    """
    Reduce versiunile listei lista_vanzari prin parametrul list_versions la acelasi numar cu current_version.
    :param list_versions: lista in care va fi salvata ultima versiuna a listei lista_vanzari
    :param current_version: contor care salveaza numarul de pasi efectuati
    :param lista_vanzari: lista in care se afla toate vanzarile
    :return: lista list_versions si contorul current_version
    """
    while current_version < len(list_versions) - 1:
        list_versions.pop()

    list_versions.append(lista_vanzari)
    current_version += 1

    return list_versions, current_version


def handle_crud(lista_vanzari: list, list_versions: list, current_version:int):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('u. Undo')
        print('r. Redo')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_vanzari, list_versions, current_version = handle_add(lista_vanzari, list_versions, current_version)
        elif optiune == '2':
            lista_vanzari, list_versions, current_version = handle_update(lista_vanzari, list_versions, current_version)
        elif optiune == '3':
            lista_vanzari, list_versions, current_version = handle_delete(lista_vanzari, list_versions, current_version)
        elif optiune == 'a':
            handle_show_all(lista_vanzari)
        elif optiune == 'u':
            lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
        elif optiune == 'r':
            lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
        elif optiune == 'd':
            handle_show_details(lista_vanzari)

        elif optiune == 'b':
           break
        else:
            print('Optiune invalida.')

    return lista_vanzari, list_versions, current_version


def run_ui(lista_vanzari: list):
    list_versions = [lista_vanzari]
    current_version = 0

    stop = True
    while stop:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_vanzari, list_versions, current_version = handle_crud(lista_vanzari, list_versions, current_version)
        elif optiune == '2':
            lista_vanzari = handle_reducere(lista_vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        elif optiune == '3':
            lista_vanzari = handle_schimbare_gen(lista_vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        elif optiune == '4':
            print(handle_pret_minim(lista_vanzari))
        elif optiune == '5':
            lista_vanzari = handle_ordonare_pret(lista_vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, lista_vanzari)
        elif optiune == '6':
            print(handle_titlu_diferit(lista_vanzari))
        elif optiune == '7':
            lista_vanzari, current_version = handle_undo(lista_vanzari, list_versions, current_version)
        elif optiune == '8':
            lista_vanzari, current_version = handle_redo(lista_vanzari, list_versions, current_version)
        elif optiune == 'x':
            stop = False
        else:
            print('Optiune invalida!')

    return lista_vanzari
