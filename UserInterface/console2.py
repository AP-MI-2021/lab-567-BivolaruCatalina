from Logic.crud import create, delete, update
from Domain.vanzare import get_sell_string, getNewSell
from Logic.discount import reducere_carte
from Logic.modificare_gen import schimbare_gen
from Logic.ordonare_vanzari import ordonare_pret


def show_menu():
    print("""
    *Lista comenzi posibile*
    
    Adaugare: id, titlu, gen, pret, tip reducere (silver, gold sau none)   -> comanda: add
    Exemplu adaugare: add,4,Razboi si Pace,drama,45.75,gold
    Stergere: id carte                                                     -> comanda: delete
    Exemplu stergere: delete,3
    Modificare: id, titlu, gen, pret, tip reducere (silver, gold sau none) -> comanda: update
    Exemplu modificare: update,2,Lama,animals,25.40,silver
    Afisare lista vanzari.                                                 -> comanda: showall
    Aplicare reduceri.                                                     -> comanda: discount
    Modificarea genului unei carti date: titlu, noul gen                   -> comanda: gen
    Exemplu modificare gen: gen,Sherlock Holmes,romance
    Ordonarea vanzarilor crescator in functie de pret.                     -> comanda: ordonare
    Oprire.                                                                -> comanda: x
    """)


def show_all(lista_vanzari):
    for vanzare in lista_vanzari:
        print(get_sell_string(vanzare))


def run_ui(lista_vanzari):
    stop = True
    show_menu()
    command_line = input("""
                           Linia de comenzi trebuie sa contina separatorul ; intre seriile de comenzi.
                           Separatorul comenzilor va fi , (virgula).
                           La sfarsitul liniei de comenzi se va pune x pentru oprire, tot separat prin ;
                           Introduceti comenzile: """)
    while stop:
        serie_comanda = command_line.split(";")
        for comanda in serie_comanda:
            com = comanda.split(",")
            if com[0] == "add":
                try:
                    lista_vanzari = create(lista_vanzari, int(com[1]), com[2], com[3], float(com[4]), com[5])
                except ValueError:
                    print("Cel putin una dintre valori nu corespunde tipului de parametru!")
                    continue
            elif com[0] == "delete":
                try:
                    lista_vanzari = delete(lista_vanzari, int(com[1]))
                except ValueError:
                    print("A doua valoare introdusa nu este un numar intreg!")
                    continue
            elif com[0] == "update":
                try:
                    lista_vanzari = update(lista_vanzari, getNewSell(int(com[1]), com[2], com[3], float(com[4]), com[5]))
                except ValueError:
                    print("Cel putin una dintre valori nu corespunde tipului de parametru!")
                    continue
            elif com[0] == "showall":
                show_all(lista_vanzari)
            elif com[0] == "discount":
                 lista_vanzari = reducere_carte(lista_vanzari)
            elif com[0] == "gen":
                try:
                    lista_vanzari = schimbare_gen(lista_vanzari, com[1], com[2])
                except ValueError:
                    print("Cel putin una dintre valori nu corespunde tipului de parametru!")
                    continue
            elif com[0] == "ordonare":
                lista_vanzari = ordonare_pret(lista_vanzari)
            elif com[0] == "x":
                stop = False
                break





