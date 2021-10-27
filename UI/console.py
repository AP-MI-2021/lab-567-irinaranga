from Domain.cheltuiala import toString
from Logic.CRUD import modificaCheltuiala, stergeCheltuiala, adaugaCheltuiala


def printMenu():
    print("1.Adauga cheltuiala")
    print("2.Sterge cheltuiala")
    print("3.Modifica cheltuiala")
    print("a.Afiseaza toate cheltuielile")
    print("x.Iesire")

def uiAdaugaCheltuiala(lista):
    numar=int(input("Dati numarul: "))
    suma=int(input("Dati suma: "))
    data=input("Dati data: ")
    tip=input("Dati tipul: ")
    return adaugaCheltuiala(numar, suma, data, tip, lista)

def uiStergeCheltuiala(lista):
    numar= int(input("Dati numarul cheltuielii de sters: "))
    return stergeCheltuiala(numar, lista)

def uiModificaCheltuiala(lista):
    numar = int(input("Dati numarul cheltuielii de modificat: "))
    suma = int(input("Dati noua suma : "))
    data =input("Dati noua data: ")
    tip = input("Dati noul tip: ")
    return modificaCheltuiala(numar, suma, data, tip, lista)

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))

def runMenu(lista):
    while True:
        printMenu()
        optiune= input("Dati optiunea: ")
        if optiune=="1":
            lista= uiAdaugaCheltuiala(lista)
        elif optiune=="2":
            lista= uiAdaugaCheltuiala(lista)
        elif optiune=="3":
            lista= uiModificaCheltuiala(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati: ")