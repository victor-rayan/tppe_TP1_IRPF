import pytest
from main.aliquota_efetiva import AliquotaEfetiva

def testVerificaAliquotaEfetiva():
    assert 24.42 == AliquotaEfetiva(30000, 189.59).valorAliquotaEfetiva()
    assert 23.76 == AliquotaEfetiva(27500, 568.77).valorAliquotaEfetiva()

def testVerificaAliquotaEfetiva1():
    assert 4.86 == AliquotaEfetiva(3500, 0).valorAliquotaEfetiva()
    assert 25.01 == AliquotaEfetiva(35000, 0).valorAliquotaEfetiva()
    assert 0.00 == AliquotaEfetiva(3500, 3791.80).valorAliquotaEfetiva()