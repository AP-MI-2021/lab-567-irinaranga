from Domain.cheltuiala import creeazaCheltuiala, getId


def adaugaCheltuiala(id, apartament, suma, data, tip, lista):
    """
    adauga o cheltuiala intr o lista
    :param id: id-ul cheltuielii, int
    :param apartament: nr. apartamentului cheltuielii, int
    :param suma: suma cheltuielii, int
    :param data: data cheltuielii, string
    :param tip: tipul cheltuielii, string
    :param lista: lista de cheltuieli
    :return: lista continand vechile elemente si noua cheltuiala
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    cheltuiala= creeazaCheltuiala(id, apartament, suma, data, tip)
    return lista + [cheltuiala]

def stergeCheltuiala(id,lista):
    """
    sterge o cheltuiala dupa id dintr o lista
    :param id: id-ul cheltuielii de sters, int
    :param lista: lista de cheltuieli
    :return: o lista continand cheltuielile cu numarul diferit de numar
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista cheltuiala cu id-ul dat!")
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != id]

def modificaCheltuiala(id, apartament, suma, data, tip,lista):
    '''
    modifica cheltuiala dintr o lista
    :param id: id-ul cheltuielii
    :param apartament: nr. apartamentului cheltuielii
    :param suma: suma cheltuielii, int
    :param data: data cheltuielii, string
    :param tip: tipul cheltuielii, string
    :param lista: lista de cheltuieli
    :return: lista continand vechile elemente si cheltuiala modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista cheltuiala cu id-ul dat!")
    listaNoua=[]
    for cheltuiala in lista:
        if getId(cheltuiala)== id:
            cheltuialaNoua=creeazaCheltuiala(id, apartament, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

def getById(id, lista):
    '''
    ia cheltuiala cu id-ul dat dintr o lista
    :param id: id-ul cheltuielii
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat sau None, daca nu exista cheltuiala cu id-ul dat
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None