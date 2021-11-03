from Domain.cheltuiala import toString
from Logic.CRUD import modificaCheltuiala, stergeCheltuiala, adaugaCheltuiala
from Logic.functionalitati import stergereCheltuieliDupaApartament, adunareValoareLaCheltuialaDupaData, \
    ordonareDescrescatorDupaSuma, maxCheltuieliPentruFiecareTip


def printMenu():
    print("1.Adauga cheltuiala")
    print("2.Sterge cheltuiala")
    print("3.Modifica cheltuiala")
    print("4.Ștergerea tuturor cheltuielilor pentru un apartament dat: ")
    print("5.Adunarea unei valori la toate cheltuielile dintr-o dată citită: ")
    print("6.Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială: ")
    print("7.Ordonarea cheltuielilor descrescător după sumă: ")
    print("a.Afiseaza toate cheltuielile")
    print("x.Iesire")

def uiAdaugaCheltuiala(lista):
    try:
        id=int(input("Dati id-ul: "))
        apartament=int(input("Dati numarul apartamentului: "))
        suma=int(input("Dati suma: "))
        data=input("Dati data: ")
        tip=input("Dati tipul: ")
        return adaugaCheltuiala(id, apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeCheltuiala(lista):
    try:
        id= int(input("Dati id-ul cheltuielii de sters: "))
        return stergeCheltuiala(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaCheltuiala(lista):
    try:
        id= int(input("Dati id-ul cheltuielii de modificat"))
        apartament = int(input("Dati noul numar al apartamentului: "))
        suma = int(input("Dati noua suma : "))
        data =input("Dati noua data: ")
        tip = input("Dati noul tip: ")
        return modificaCheltuiala(id, apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergereCheltuialaDupaApartament(lista):
    try:
        nr_apartament= int(input("Dati nr. apartamentului"))
        return stergereCheltuieliDupaApartament(nr_apartament, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiAdunareValoareDupaData(lista):
    try:
        data1= input("Dati data: ")
        adunarevaloare=int(input("Dati valoarea: "))
        return adunareValoareLaCheltuialaDupaData(data1, adunarevaloare, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMaxCheltuieliPentruTip(lista):
    rezultat= maxCheltuieliPentruFiecareTip(lista)
    for tipul in rezultat:
        print("Tipul {} are cheltuiala maxima {}".format(tipul, rezultat[tipul]))

def uiOrdonareDescrescatorDupaSuma(lista):
    showAll(ordonareDescrescatorDupaSuma(lista))

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
            lista= uiStergeCheltuiala(lista)
        elif optiune=="3":
            lista= uiModificaCheltuiala(lista)
        elif optiune=="4":
            lista= uiStergereCheltuialaDupaApartament(lista)
        elif optiune=="5":
            uiAdunareValoareDupaData(lista)
        elif optiune=="6":
            uiMaxCheltuieliPentruTip(lista)
        elif optiune=="7":
            uiOrdonareDescrescatorDupaSuma(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati: ")