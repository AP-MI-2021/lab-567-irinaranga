from Domain.cheltuiala import creeazaCheltuiala, getNumar, getSuma, getData, getTip

def testCheltuiala():
    cheltuiala=creeazaCheltuiala(23,250,25/12/2021,"intretinere")
    assert getNumar(cheltuiala)== 23
    assert getSuma(cheltuiala)== 250
    assert getData(cheltuiala)== 25/12/2021
    assert getTip(cheltuiala)== "intretinere"