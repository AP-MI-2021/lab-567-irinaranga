def creeazaCheltuiala(id, apartament, suma, data, tip):
    '''
    creeaza o cheltuiala
    :param id: int
    :param apartament: int
    :param suma: int
    :param data: string
    :param tip: string
    :return: un dictionar ce retine o cheltuiala
    '''
    return [id,  apartament, suma, data, tip]

def getId(cheltuiala):
    '''
    ia id-ul cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: id-ul cheltuielii
    '''
    return cheltuiala[0]
    #return cheltuiala['id']

def getApartament(cheltuiala):
    '''
    ia nr. apartamentului cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: numarul cheltuielii
    '''
    return cheltuiala[1]
    #return cheltuiala['numar']

def getSuma(cheltuiala):
    '''
    ia suma cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala[2]
    #return cheltuiala['suma']

def getData(cheltuiala):
    '''
    ia data cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: data cheltuielii
    '''
    return cheltuiala[3]
    #return cheltuiala['data']

def getTip(cheltuiala):
    '''
    ia tipul cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: tipul cheltuielii
    '''
    return cheltuiala[4]
    #return cheltuiala['tip']

def toString(cheltuiala):
    return "id: {}, apartament: {}, suma: {}, data: {}, tip: {} ".format(
        getId(cheltuiala),
        getApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )