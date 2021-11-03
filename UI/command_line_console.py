from Domain.cheltuiala import toString
from Logic.CRUD import stergeCheltuiala, adaugaCheltuiala


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))

def main_line(lista):
    print("Scrieti ajutor (pentru a vedea optiunile disponibile) sau dati comanda: ")
    while True:
        givenString = input()
        if givenString == "ajutor":
            print("add, id, apartament, suma, data, tip")
            print("delete, id")
            print("showAll")
            print("Exit")
        else:
            optiuni = givenString.split(";")
            if optiuni[0] == "Exit":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if(opt[0] == "add"):
                        try:
                            lista = adaugaCheltuiala(opt[1], opt[2], opt[3], opt[4], opt[5], lista)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showAll":
                        showAll(lista)
                    elif opt[0] == "delete":
                        lista = stergeCheltuiala(opt[1], lista)
                    else:
                        print("Optiune gresita! Scrieti 'ajutor' pentru a vedea optiunile disponibile")