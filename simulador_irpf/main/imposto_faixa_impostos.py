class ImpostoFaixaImpostos:
    def __init__(self, rendimentosTributaveis: float) -> None:
        self.rendimentosTributaveis = rendimentosTributaveis

    def valorFaixa1(self) -> float:
        return 1903.98

    def valorFaixa2(self) -> float:
        return 922.67

    def valorFaixa3(self) -> float:
        return 924.40

    def valorFaixa4(self) -> float:
        return 913.63

    def valorFaixa5(self) -> float:
        return 5335.32

    def valorImpostoFaixa1(self) -> float:
        return 0

    def valorImpostoFaixa2(self) -> float:
        return 69.2003

    def valorImpostoFaixa3(self) -> float:
        return 138.6600

    def valorImpostoFaixa4(self) -> float:
        return 205.5667

    def valorImpostoFaixa5(self) -> float:
        return 1467.2130