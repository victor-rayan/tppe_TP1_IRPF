class ImpostoFaixaImpostos:
    def __init__(self, rendimentosTributaveis: float) -> None:
        self._rendimentosTributaveis = rendimentosTributaveis
        self._maximoFaixa1: float = 1903.98
        self._maximoFaixa2: float = 922.67
        self._maximoFaixa3: float = 924.40
        self._maximoFaixa4: float = 913.63
        self._maximoFaixa5: float = 5335.32
        self._impostoFaixa1: float = 0
        self._impostoFaixa2: float = 0.075
        self._impostoFaixa3: float = 0.15
        self._impostoFaixa4: float = 0.2250
        self._impostoFaixa5: float = 0.2750

    def valorFaixa1(self) -> float:
        if (self._rendimentosTributaveis <= self._maximoFaixa1):
            return self._rendimentosTributaveis
        else:
            return self._maximoFaixa1

    def valorFaixa2(self) -> float:
        faixasAnteriores = self._maximoFaixa1
        if (self._rendimentosTributaveis > faixasAnteriores + self._maximoFaixa2):
            return self._maximoFaixa2
        elif (self._rendimentosTributaveis <= faixasAnteriores):
            return 0
        else:
            return self._rendimentosTributaveis - faixasAnteriores

    def valorFaixa3(self) -> float:
        faixasAnteriores = self._maximoFaixa1 + self._maximoFaixa2
        if (self._rendimentosTributaveis > faixasAnteriores + self._maximoFaixa3):
            return self._maximoFaixa3
        elif (self._rendimentosTributaveis <= faixasAnteriores):
            return 0
        else:
            return self._rendimentosTributaveis - faixasAnteriores

    def valorFaixa4(self) -> float:
        faixasAnteriores = self._maximoFaixa1 + self._maximoFaixa2 + self._maximoFaixa3
        if (self._rendimentosTributaveis > faixasAnteriores + self._maximoFaixa4):
            return self._maximoFaixa4
        elif (self._rendimentosTributaveis <= faixasAnteriores):
            return 0
        else:
            return self._rendimentosTributaveis - faixasAnteriores

    def valorFaixa5(self) -> float:
        faixasAnteriores = self._maximoFaixa1 + self._maximoFaixa2 + \
            self._maximoFaixa3 + self._maximoFaixa4
        if (self._rendimentosTributaveis <= faixasAnteriores):
            return 0
        else:
            return self._rendimentosTributaveis - faixasAnteriores

    def valorImpostoFaixa1(self) -> float:
        return self.valorFaixa1() * self._impostoFaixa1

    def valorImpostoFaixa2(self) -> float:
        return self.valorFaixa2() * self._impostoFaixa2

    def valorImpostoFaixa3(self) -> float:
        return self.valorFaixa3() * self._impostoFaixa3

    def valorImpostoFaixa4(self) -> float:
        return self.valorFaixa4() * self._impostoFaixa4

    def valorImpostoFaixa5(self) -> float:
        return self.valorFaixa5() * self._impostoFaixa5

    def valorImpostoTotal(self) -> float:
        valorTotal: float = self.valorImpostoFaixa1() + self.valorImpostoFaixa2() + \
            self.valorImpostoFaixa3() + self.valorImpostoFaixa4() + self.valorImpostoFaixa5()
        return valorTotal
