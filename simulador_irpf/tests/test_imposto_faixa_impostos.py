import pytest
from decimal import *
from main.imposto_faixa_impostos import ImpostoFaixaImpostos

def testCalculaValorFaixaUm():
    simulador = ImpostoFaixaImpostos(1500)
    assert 1500 == simulador.valorFaixa1()
    assert 0 == simulador.valorFaixa2()
    assert 0 == simulador.valorFaixa3()
    assert 0 == simulador.valorFaixa4()
    assert 0 == simulador.valorFaixa5()

def testCalculaValorFaixaCinco():
    simulador = ImpostoFaixaImpostos(10000)
    assert 1903.98 == simulador.valorFaixa1()
    assert 922.67 == simulador.valorFaixa2()
    assert 924.40 == simulador.valorFaixa3()
    assert 913.63 == simulador.valorFaixa4()
    assert 5335.32 == simulador.valorFaixa5()

def testCalculaValorImpostoFaixaUm():
    simulador = ImpostoFaixaImpostos(1500)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa1(), 0.001)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa2(), 0.001)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa3(), 0.001)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa4(), 0.001)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa5(), 0.001)

def testCalculaValorImpostoFaixaCinco():
    simulador = ImpostoFaixaImpostos(10000)
    assert 0 == pytest.approx(simulador.valorImpostoFaixa1(), 0.001)
    assert 69.2003 == pytest.approx(simulador.valorImpostoFaixa2(), 0.001)
    assert 138.6600 == pytest.approx(simulador.valorImpostoFaixa3(), 0.001)
    assert 205.5667 == pytest.approx(simulador.valorImpostoFaixa4(), 0.001)
    assert 1467.2130 == pytest.approx(simulador.valorImpostoFaixa5(), 0.001)