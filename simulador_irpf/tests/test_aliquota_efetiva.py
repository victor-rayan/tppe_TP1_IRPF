import pytest
from main.aliquota_efetiva import AliquotaEfetiva


@pytest.mark.parametrize("totalRendimentos, totalDeducoes, aliquotaEsperada", 
    [
        (30000, 189.59, 24.42), 
        (27500, 568.77, 23.76), 
        (3500, 0, 4.86)
    ])
def testVerificaAliquotaEfetiva(totalRendimentos:float, totalDeducoes:float, aliquotaEsperada:float):
    assert aliquotaEsperada == AliquotaEfetiva(totalRendimentos, totalDeducoes).valorAliquotaEfetiva()
