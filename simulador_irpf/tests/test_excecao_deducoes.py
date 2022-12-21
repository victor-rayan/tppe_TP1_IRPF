import pytest
from main.deducao import Deducoes

from exceptions.exceptions import (DescricaoEmBrancoException, ValorDeducaoInvalidoException,NomeEmBrancoException)

class TesteDeducoesExcecao:

    def testDescricaoEmBrancoOutrasDeducoes(self):
        deducao = Deducoes()
        with pytest.raises(DescricaoEmBrancoException):
            deducao.cadastrarOutrasDeducoes("",100.00)
        
    def testValorDeducaoInvalidoOutrasDeducoes(self):
        deducao = Deducoes()
        with pytest.raises(ValorDeducaoInvalidoException):
            deducao.cadastrarOutrasDeducoes("FAPI",0.0)

    def testDescricaoEmBrancoPrevidenciaOficial(self):
        deducao = Deducoes()
        with pytest.raises(DescricaoEmBrancoException):
            deducao.cadastrarPrevidenciaOficial("",100.00)
                
    def testValorDeducaoInvalidoPrevidenciaOficial(self): 
        deducao = Deducoes()
        with pytest.raises(ValorDeducaoInvalidoException):
            deducao.cadastrarPrevidenciaOficial("Previdencia",0.0)
        
    def testValorPensaoInvalidoAlimenticia(self):
        deducao = Deducoes()
        with pytest.raises(ValorDeducaoInvalidoException):
            deducao.cadastrarPensaoAlimenticia(0.0)
                
    def testNomeEmBrancoDependentes(self):
        deducao = Deducoes()
        with pytest.raises(NomeEmBrancoException):
            deducao.cadastrarDependente("","14/12/2000")
                
