from Domain.cheltuiala import getApartament, creeazaCheltuiala, getId, getSuma, getData, getTip
from Logic.CRUD import stergeCheltuiala


def stergereCheltuieliDupaApartament(nr_apartament, lista):
    '''
    sterge toate cheltuielile care au nr. de apartament egal cu cel dat de la tastatura
    :param nr_apartament: nr. apartamentului citit de la tastatura dupa care se va face stergerea
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli in urma stergerii
    '''
    listaNoua= []
    for cheltuiala in lista:
        if getApartament(cheltuiala)!=nr_apartament:
            listaNoua.append(cheltuiala)
    return listaNoua

def adunareValoareLaCheltuialaDupaData(data1, adunarevaloare, lista):
    '''
    aduna o valoare la toate cheltuielile dupa o data citita
    :param data1: data cheltuielii in functie de care se va face adunarea
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli in urma adunarii valorii
    '''
    listaNoua=[]
    for cheltuiala in lista:
        if getData(cheltuiala)== data1:
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getApartament(cheltuiala),
                    getSuma(cheltuiala) + adunarevaloare,
                    getData(cheltuiala),
                    getTip(cheltuiala)
                )
                listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

def maxCheltuieliPentruFiecareTip(lista):
    '''
    cauta maximul de cheltuieli pentru fiecare tip de cheltuiala
    :param lista: lista de cheltuieli
    :return: maximul de cheltuieli pentru fiecare tip de cheltuiala
    '''
    rezultat={}
    for cheltuiala in lista:
        tipul = getTip(cheltuiala)
        suma = getSuma(cheltuiala)
        if tipul in rezultat:
            if suma > rezultat[tipul]:
                rezultat[tipul] = suma
        else:
            rezultat[tipul] = suma
    return rezultat

def ordonareDescrescatorDupaSuma(lista):
    '''
    ordoneaza descrescator dupa suma
    :param lista: lista de cheltuieli
    :return: lista ordonata descrescator dupa suma
    '''
    return sorted(lista, key=lambda cheltuiala: getSuma(cheltuiala), reverse=True)


