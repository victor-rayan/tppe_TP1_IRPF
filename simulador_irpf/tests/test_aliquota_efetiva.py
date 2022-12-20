import pytest
from main.aliquota_efetiva import AliquotaEfetiva

def testVerificaAliquotaEfetiva():
    assert 24.42 == AliquotaEfetiva(30000, 189.59).valorAliquotaEfetiva()
  