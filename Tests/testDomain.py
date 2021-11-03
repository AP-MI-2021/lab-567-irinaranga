from Domain.cheltuiala import creeazaCheltuiala, getSuma, getData, getTip, getId, getApartament


def testCheltuiala():
    cheltuiala=creeazaCheltuiala(1,23,250,"25.12.2021","intretinere")
    assert getId(cheltuiala)==1
    assert getApartament(cheltuiala)== 23
    assert getSuma(cheltuiala)== 250
    assert getData(cheltuiala)== "25.12.2021"
    assert getTip(cheltuiala)== "intretinere"