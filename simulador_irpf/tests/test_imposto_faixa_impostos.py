import pytest
from main.imposto_faixa_impostos import ImpostoFaixaImpostos

simulador = ImpostoFaixaImpostos(10000)

def testCalculaValorFaixa():
    assert 1903.98 == simulador.valorFaixa1()
    assert 922.67 == simulador.valorFaixa2()
    assert 924.40 == simulador.valorFaixa3()
    assert 913.63 == simulador.valorFaixa4()
    assert 5335.32 == simulador.valorFaixa5()

def testCalculaValorImpostoFaixa():
    assert 0 == simulador.valorImpostoFaixa1()
    assert 69.2003 == simulador.valorImpostoFaixa2()
    assert 138.6600 == simulador.valorImpostoFaixa3()
    assert 205.5667 == simulador.valorImpostoFaixa4()
    assert 1467.2130 == simulador.valorImpostoFaixa5()