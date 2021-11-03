from Domain.cheltuiala import getId, getSuma, getData, getTip, getApartament
from Logic.CRUD import adaugaCheltuiala, getById, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    lista=[]
    lista= adaugaCheltuiala(1, 23, 250, "25.12.2021", "intretinere", lista)
    assert len(lista)==1
    assert getId(getById(1,lista)) == 1
    assert getApartament(getById(1,lista)) == 23
    assert getSuma(getById(1,lista)) == 250
    assert getData(getById(1,lista)) == "25.12.2021"
    assert getTip(getById(1,lista)) == "intretinere"

def testStergeCheltuiala():
    lista=[]
    lista = adaugaCheltuiala(1, 23, 250, "25.12.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 34, 500, "25.12.2021", "intretinere", lista)

    lista= stergeCheltuiala(1, lista)
    assert len(lista) == 1
    assert getById(1, lista) is None
    assert getById(2, lista) is not None

    try:
        lista= stergeCheltuiala(3, lista)
        assert False
    except ValueError:
        assert len(lista)== 1
        assert getById(2, lista) is not None
    except Exception:
        assert False

def testModificaCheltuiala():
    lista=[]
    lista= adaugaCheltuiala(1, 23, 250, "25.12.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 34, 500, "25.12.2021", "intretinere", lista)

    lista = modificaCheltuiala(1, 23, 640, "25.07.2022", "canal", lista)

    cheltuialaUpdatata = getById(1, lista)
    assert getId(cheltuialaUpdatata) == 1
    assert getApartament(cheltuialaUpdatata) == 23
    assert getSuma(cheltuialaUpdatata) == 640
    assert getData(cheltuialaUpdatata) == "25.07.2022"
    assert getTip(cheltuialaUpdatata) == "canal"

    cheltuialaNeupdatata=getById(2, lista)
    assert getId(cheltuialaNeupdatata) == 2
    assert getApartament(cheltuialaNeupdatata) == 34
    assert getSuma(cheltuialaNeupdatata) == 500
    assert getData(cheltuialaNeupdatata) == "25.12.2021"
    assert getTip(cheltuialaNeupdatata) == "intretinere"

    lista = []
    lista = adaugaCheltuiala(1, 23, 250, "25.12.2021", "intretinere", lista)

    try:
        lista = modificaCheltuiala(3, 34, 500, "25.12.2021", "intretinere", lista)
    except ValueError:
        cheltuialaNeupdatata = getById(1, lista)
        assert getId(cheltuialaNeupdatata) == 1
        assert getApartament(cheltuialaNeupdatata) == 23
        assert getSuma(cheltuialaNeupdatata) == 250
        assert getData(cheltuialaNeupdatata) == "25.12.2021"
        assert getTip(cheltuialaNeupdatata) == "intretinere"
    except Exception:
        assert False


def testGetById():
    lista=[]
    lista = adaugaCheltuiala(1, 23, 250, "25.12.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 34, 500, "25.12.2021", "intretinere", lista)

    assert getById(1, lista)== [1,  23, 250, "25.12.2021", "intretinere"]
    assert getById(2,lista)==[2,  34, 500, "25.12.2021", "intretinere"]



