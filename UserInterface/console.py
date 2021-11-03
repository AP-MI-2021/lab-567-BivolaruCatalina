from Domain.vanzare import getNewSell, get_sell_string, get_price, get_genre, get_discount, get_title
from Logic.crud import create, read, update, delete
from Logic.discount import reducere_carte
from Logic.ordonare_vanzari import ordonare_pret
from Logic.modificare_gen import schimbare_gen

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
        x. Iesire
        """
    )


def handle_add(lista_vanzari):
    try:
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        reducere = input('Dati noul tip de reducere al cartii: ')
        lista_vanzari = create(lista_vanzari, id_carte, titlu, gen, pret, reducere)
        return lista_vanzari
    except ValueError as ve:
        print("Eroare: ", ve)


def handle_update(lista_vanzari):
    try:
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        reducere = input('Dati noul tip de reducere al cartii: ')
        return update(lista_vanzari, getNewSell(id_carte, titlu, gen,  pret, reducere))
    except ValueError as ve:
        print("Eroare: ", ve)


def handle_delete(lista_vanzari):
    try:
        id_carte = int(input('Dati id-ul cartii care se va sterge: '))
        lista_vanzari = delete(lista_vanzari, id_carte)
        print('Stergerea a fost efectuata cu succes.')
        return lista_vanzari
    except ValueError as ve:
        print("Eroare: ", ve)


def handle_show_all(lista_vanzari):
        for carte in lista_vanzari:
            print(get_sell_string(carte))


def handle_show_details(lista_vanzari):
        id_carte = int(input('Dati id-ul cartii pentru care doriti detalii: '))
        vanzare = read(lista_vanzari, id_carte)
        print(f'Titlu: {get_title(vanzare)}')
        print(f'Gen: {get_genre(vanzare)}')
        print(f'Pret: {get_price(vanzare)}')
        print(f'Tip reducere: {get_discount(vanzare)}')


def handle_reducere(lista_vanzari):
    lista_vanzari = reducere_carte(lista_vanzari)
    handle_show_all(lista_vanzari)


def handle_schimbare_gen(lista_vanzari):
    titlu = input('Introduceti titlul carti ce va fi schimbata: ')
    lista_vanzari = schimbare_gen(lista_vanzari, titlu)
    return lista_vanzari


def handle_ordonare_pret(lista_vanzari):
    lista_vanzari = ordonare_pret(lista_vanzari)
    handle_show_all(lista_vanzari)


def handle_crud(lista_vanzari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_vanzari = handle_add(lista_vanzari)
        elif optiune == '2':
            lista_vanzari = handle_update(lista_vanzari)
        elif optiune == '3':
            lista_vanzari = handle_delete(lista_vanzari)
        elif optiune == 'a':
            handle_show_all(lista_vanzari)
        elif optiune == 'd':
            handle_show_details(lista_vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return lista_vanzari


def run_ui(lista_vanzari):
    stop = True
    while stop:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_vanzari = handle_crud(lista_vanzari)
        elif optiune == '2':
            lista_vanzari = handle_reducere(lista_vanzari)
        elif optiune == '3':
            lista_vanzari = handle_schimbare_gen(lista_vanzari)
        elif optiune == '5':
            result = lista_vanzari
            result = handle_ordonare_pret(result)
        elif optiune == 'x':
            stop = False
        else:
            print('Optiune invalida.')

    return lista_vanzari
