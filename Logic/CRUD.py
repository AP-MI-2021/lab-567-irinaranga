from Domain.cheltuiala import getNumar, creeazaCheltuiala


def adaugaCheltuiala(numar, suma, data, tip, lista):
    """
    adauga o cheltuiala intr o lista
    :param numar: numarul cheltuielii, int
    :param suma: suma cheltuielii, int
    :param data: data cheltuielii
    :param tip: tipul cheltuielii, string
    :param lista: lista de cheltuieli
    :return: lista continand vechile elemente si noua cheltuiala
    """
    cheltuiala= creeazaCheltuiala(numar, suma, data, tip)
    return lista + [cheltuiala]

def stergeCheltuiala(numar,lista):
    """
    sterge o cheltuiala dupa numar dintr o lista
    :param numar: numarul cheltuielii de sters, int
    :param lista: lista de cheltuieli
    :return: o lista continand cheltuielile cu numarul diferit de numar
    """
    return [cheltuiala for cheltuiala in lista if getNumar(cheltuiala) != numar]

def modificaCheltuiala(numar, suma, data, tip,lista):
    '''

    :param numar:
    :param suma:
    :param data:
    :param tip:
    :param lista:
    :return:
    '''
    listaNoua=[]
    for cheltuiala in lista:
        if getNumar(cheltuiala)== numar:
            cheltuialaNoua=creeazaCheltuiala(numar, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

def getByNumar(numar, lista):
    '''

    :param numar:
    :param lista:
    :return:
    '''
    for cheltuiala in lista:
        if getNumar(cheltuiala) == numar:
            return cheltuiala
    return None