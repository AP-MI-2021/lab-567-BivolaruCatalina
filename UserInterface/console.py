from Domain.carte2 import getNewBook, get_book_string, get_price, get_genre, get_discount, get_title
from Logic.crud import create, read, update, delete

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


def handle_add(lista_carti):
    id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
    titlu = input('Dati noul titlu al cartii: ')
    gen = input('Dati noul gen al cartii: ')
    pret = float(input('Dati noul pret al cartii: '))
    reducere = input('Dati noul tip de reducere al cartii: ')
    lista_carti = create(lista_carti, id_carte, titlu, gen, pret, reducere)
    return lista_carti


def handle_update(lista_carti):
    id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
    titlu = input('Dati noul titlu al cartii: ')
    gen = input('Dati noul gen al cartii: ')
    pret = float(input('Dati noul pret al cartii: '))
    reducere = input('Dati noul tip de reducere al cartii: ')
    return update(lista_carti, getNewBook(id_carte, titlu, gen,  pret, reducere))


def handle_delete(lista_carti):
    id_carte = int(input('Dati id-ul cartii care se va sterge: '))
    lista_carti = delete(lista_carti, id_carte)
    print('Stergerea a fost efectuata cu succes.')
    return lista_carti


def handle_show_all(lista_carti):
    for carte in lista_carti:
        print(get_book_string(carte))


def handle_show_details(lista_carti):
    id_carte = int(input('Dati id-ul cartii pentru care doriti detalii: '))
    carte = read(lista_carti, id_carte)
    print(f'Titlu: {get_title(carte)}')
    print(f'Gen: {get_genre(carte)}')
    print(f'Pret: {get_price(carte)}')
    print(f'Tip reducere: {get_discount(carte)}')


def handle_crud(lista_carti):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_carti = handle_add(lista_carti)
        elif optiune == '2':
            lista_carti = handle_update(lista_carti)
        elif optiune == '3':
            lista_carti = handle_delete(lista_carti)
        elif optiune == 'a':
            handle_show_all(lista_carti)
        elif optiune == 'd':
            handle_show_details(lista_carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return lista_carti


def run_ui(lista_carti):
    stop = True
    while stop:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            lista_carti = handle_crud(lista_carti)
        elif optiune == 'x':
            stop = False
        else:
            print('Optiune invalida.')

    return lista_carti
