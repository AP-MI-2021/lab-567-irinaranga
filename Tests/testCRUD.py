from Domain.cheltuiala import getNumar, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNumar, stergeCheltuiala, modificaCheltuiala


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

def testModificaCheltuiala():
    lista=[]
    lista= adaugaCheltuiala(23, 250, "25.12.2021", "intretinere", lista)
    lista = adaugaCheltuiala(34, 500, "25.12.2021", "intretinere", lista)

    lista = modificaCheltuiala(23, 640, "25.07.2022", "canal", lista)

    cheltuialaUpdatata = getByNumar(23, lista)
    assert getNumar(cheltuialaUpdatata) == 23
    assert getSuma(cheltuialaUpdatata) == 640
    assert getData(cheltuialaUpdatata) == "25.07.2022"
    assert getTip(cheltuialaUpdatata) == "canal"

    cheltuialaNeupdatata=getByNumar(34, lista)
    assert getNumar(cheltuialaNeupdatata) == 34
    assert getSuma(cheltuialaNeupdatata) == 500
    assert getData(cheltuialaNeupdatata) == "25.12.2021"
    assert getTip(cheltuialaNeupdatata) == "intretinere"


def testGetByNumar():
    lista=[]
    lista = adaugaCheltuiala(23, 250, "25.12.2021", "intretinere", lista)
    lista = adaugaCheltuiala(34, 500, "25.12.2021", "intretinere", lista)

    assert getByNumar(23, lista)== [("numar", 23), ("suma",250), ("data","25.12.2021"), ("tip","intretinere")]
    assert getByNumar(34,lista)==[("numar", 34), ("suma",500), ("data","25.12.2021"), ("tip","intretinere")]



