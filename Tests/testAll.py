from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala,  \
    testGetById
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testStergereChetuieliDupaApartament, testAdunareValoareLaCheltuialaDupaData, \
    testMaxCheltuieliPentruFiecareTip, testOrdonareDescrescatorDupaSuma


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testModificaCheltuiala()
    testGetById()

    testStergereChetuieliDupaApartament()
    testAdunareValoareLaCheltuialaDupaData()
    testMaxCheltuieliPentruFiecareTip()
    testOrdonareDescrescatorDupaSuma()