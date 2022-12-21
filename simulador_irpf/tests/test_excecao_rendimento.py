import pytest
from main.cadastro_de_rendimentos import CadastroDeRendimentos

from exceptions.exceptions import (ValorRendimentoInvalidoException, DescricaoEmBrancoException)

class TesteRendimentoExcecao:

    def testDescricaoRendimentoInvalido(self):
        simuladorIRPF = CadastroDeRendimentos()
        with pytest.raises(DescricaoEmBrancoException):
            simuladorIRPF.cadastrarRendimento("", 1000.00)
        
    def testValorRendimentoInvalido(self):  
        simuladorIRPF = CadastroDeRendimentos()
        with pytest.raises(ValorRendimentoInvalidoException):
            simuladorIRPF.cadastrarRendimento("Aluguel", 0.0)

