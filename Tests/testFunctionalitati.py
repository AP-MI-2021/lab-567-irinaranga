from Domain.cheltuiala import getSuma, getId
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.functionalitati import stergereCheltuieliDupaApartament, adunareValoareLaCheltuialaDupaData, \
    maxCheltuieliPentruFiecareTip, ordonareDescrescatorDupaSuma


def testStergereChetuieliDupaApartament():
    lista=[]
    lista= adaugaCheltuiala(1, 23, 567, "26.04.2022", "canal", lista)
    lista= adaugaCheltuiala(2, 23, 789, "12.07.2022", "intretinere", lista)
    lista= adaugaCheltuiala(3, 45, 589, "23.09.2022", "canal", lista)

    lista= stergereCheltuieliDupaApartament(23, lista)

    assert getById(1, lista) is None
    assert getById(2, lista) is None
    assert getById(3, lista) is not None


def testAdunareValoareLaCheltuialaDupaData():
    lista=[]
    lista= adaugaCheltuiala(1, 67, 890, "25.02.2022", "intretinere", lista)
    lista= adaugaCheltuiala(2, 89, 432, "03.09.2022", "alte cheltuieli", lista)
    lista= adaugaCheltuiala(3, 23, 124, "25.02.2022", "canal", lista)

    lista= adunareValoareLaCheltuialaDupaData("25.02.2022", 50, lista)

    assert getSuma(getById(1, lista))==940
    assert getSuma(getById(2,lista))==432
    assert getSuma(getById(3,lista))==174

def testMaxCheltuieliPentruFiecareTip():
    lista=[]
    lista = adaugaCheltuiala(1, 67, 890, "25.02.2022", "intretinere", lista)
    lista = adaugaCheltuiala(2, 56, 900, "26.07.2022", "intretinere", lista)
    lista = adaugaCheltuiala(3, 68, 345, "23.09.2022", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(4, 78, 123, "12.03.2022", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(5, 45, 600, "11.10.2022", "canal", lista)
    lista = adaugaCheltuiala(6, 23, 235, "24.08.2022", "canal", lista)

    rezultat=  maxCheltuieliPentruFiecareTip(lista)

    assert rezultat["intretinere"]== 900
    assert rezultat["alte cheltuieli"]==345
    assert rezultat["canal"]==600

def testOrdonareDescrescatorDupaSuma():
    lista= []
    lista = adaugaCheltuiala(1, 67, 890, "25.02.2022", "intretinere", lista)
    lista = adaugaCheltuiala(4, 78, 123, "12.03.2022", "alte cheltuieli", lista)
    lista = adaugaCheltuiala(6, 23, 235, "24.08.2022", "canal", lista)

    rezultat = ordonareDescrescatorDupaSuma(lista)

    assert getId(rezultat[0])==1
    assert getId(rezultat[1])==6
    assert getId(rezultat[2])==4