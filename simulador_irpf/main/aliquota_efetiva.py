from .imposto_faixa_impostos import ImpostoFaixaImpostos
from math import trunc

class AliquotaEfetiva:
    def __init__(self, totalRendimentos: float, valorDeducoes: float) -> None:
        self._totalRendimentos = totalRendimentos
        self._valorDeducoes = valorDeducoes
        self._impostoTotal = ImpostoFaixaImpostos(totalRendimentos-valorDeducoes).valorImpostoTotal()
    
    def valorAliquotaEfetiva(self) -> float:
        valorAliquota = ((self._impostoTotal)/self._totalRendimentos)*100
        return trunc(valorAliquota * 100)/100