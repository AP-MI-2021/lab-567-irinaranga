from Domain.cheltuiala import getNumar, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNumar, stergeCheltuiala


def testAdaugaCheltuiala():
    lista=[]
    lista= adaugaCheltuiala(23, 250, 25/12/2021, "intretinere", lista)
    assert len(lista)==1
    assert getNumar(getByNumar(23,lista)) == 23
    assert getSuma(getByNumar(23,lista)) == 250
    assert getData(getByNumar(23,lista)) == 25 / 12 / 2021
    assert getTip(getByNumar(23,lista)) == "intretinere"

def testStergeCheltuiala():
    lista=[]
    lista = adaugaCheltuiala(23, 250, 25 / 12 / 2021, "intretinere", lista)
    lista = adaugaCheltuiala(34, 500, 25 / 12 / 2021, "intretinere", lista)

    lista= stergeCheltuiala(23, lista)
    assert len(lista)== 1
    assert getByNumar(23, lista) is None


    lista= stergeCheltuiala(24, lista)
    assert len(lista)== 1
    assert getByNumar(34, lista) is not None


