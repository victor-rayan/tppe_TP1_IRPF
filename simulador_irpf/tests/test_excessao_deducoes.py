import pytest
from main.deducao import Deducoes

class TesteDeducoesExcessao:

    def testDescricaoEmBrancoOutrasDeducoes(self):
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.cadastrarOutrasDeducoes("",100.00)
        
    def testValorDeducaoInvalidoOutrasDeducoes(self):
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.cadastrarOutrasDeducoes("FAPI",0.0)

    def testDescricaoEmBrancoPrevidenciaOficial(self):
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.cadastrarPrevidenciaOficial("",100.00)
                
    def testValorDeducaoInvalidoPrevidenciaOficial(self): 
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.cadastrarPrevidenciaOficial("Previdencia",0.0)
        
    def testValorPensaoInvalidoAlimenticia(self):
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.pensaoAlimenticia(0.0)
                
    def testNomeEmBrancoDependentes(self):
        deducao = Deducoes()
        with pytest.raises(Exception):
            deducao.cadastrarDependente("","14/12/2000")
                
