def creeazaCheltuiala(numar, suma, data, tip):
    '''
    creeaza o cheltuiala
    :param numar: int
    :param suma: int
    :param data: string
    :param tip: string
    :return: un dictionar ce retine o cheltuiala
    '''
    return [("numar", numar), ("suma",suma), ("data",data), ("tip",tip)]



def getNumar(cheltuiala):
    '''
    ia numarul cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: numarul cheltuielii
    '''
    return cheltuiala[0][1]
    #return cheltuiala['numar']

def getSuma(cheltuiala):
    '''
    ia suma cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala[1][1]
    #return cheltuiala['suma']

def getData(cheltuiala):
    '''
    ia data cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: data cheltuielii
    '''
    return cheltuiala[2][1]
    #return cheltuiala['data']

def getTip(cheltuiala):
    '''
    ia tipul cheltuielii
    :param cheltuiala: dictionar de tipul cheltuiala
    :return: tipul cheltuielii
    '''
    return cheltuiala[3][1]
    #return cheltuiala['tip']

def toString(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return "numar: {}, suma: {}, data: {}, tip: {} ".format(
        getNumar(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )