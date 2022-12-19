import pytest
from decimal import *
from main.imposto_faixa_impostos import ImpostoFaixaImpostos

@pytest.mark.parametrize("simulador,valorFaixa1,valorFaixa2,valorFaixa3,valorFaixa4,valorFaixa5",
    [
        (ImpostoFaixaImpostos(1500), 1500, 0, 0, 0, 0), 
        (ImpostoFaixaImpostos(2500), 1903.98, 596.02, 0, 0, 0),
        (ImpostoFaixaImpostos(3750), 1903.98, 922.67, 923.35, 0, 0),
        (ImpostoFaixaImpostos(4500), 1903.98, 922.67, 924.40, 748.95, 0),
        (ImpostoFaixaImpostos(10000), 1903.98, 922.67, 924.40, 913.63, 5335.32), 
    ])
def testCalculaValorFaixa(simulador: ImpostoFaixaImpostos, valorFaixa1: str, valorFaixa2: str, valorFaixa3: str, valorFaixa4: str, valorFaixa5: str):
    assert valorFaixa1 == pytest.approx(simulador.valorFaixa1(), 0.001)
    assert valorFaixa2 == pytest.approx(simulador.valorFaixa2(), 0.001)
    assert valorFaixa3 == pytest.approx(simulador.valorFaixa3(), 0.001)
    assert valorFaixa4 == pytest.approx(simulador.valorFaixa4(), 0.001)
    assert valorFaixa5 == pytest.approx(simulador.valorFaixa5(), 0.001)

@pytest.mark.parametrize("simulador,valorImposto1,valorImposto2,valorImposto3,valorImposto4,valorImposto5",
    [
        (ImpostoFaixaImpostos(1500), 0, 0, 0, 0, 0),
        (ImpostoFaixaImpostos(2500), 0, 44.7015, 0, 0, 0), 
        (ImpostoFaixaImpostos(3750), 0, 69.2003, 138.5025, 0, 0), 
        (ImpostoFaixaImpostos(4500), 0, 69.2003, 138.6600, 168.5138, 0), 
        (ImpostoFaixaImpostos(10000), 0, 69.2003, 138.6600, 205.5667, 1467.2130), 
    ])
def testCalculaValorImpostoFaixa(simulador: ImpostoFaixaImpostos, valorImposto1: str, valorImposto2: str, valorImposto3: str, valorImposto4: str, valorImposto5: str):
    assert valorImposto1 == pytest.approx(simulador.valorImpostoFaixa1(), 0.001)
    assert valorImposto2 == pytest.approx(simulador.valorImpostoFaixa2(), 0.001)
    assert valorImposto3 == pytest.approx(simulador.valorImpostoFaixa3(), 0.001)
    assert valorImposto4 == pytest.approx(simulador.valorImpostoFaixa4(), 0.001)
    assert valorImposto5 == pytest.approx(simulador.valorImpostoFaixa5(), 0.001)