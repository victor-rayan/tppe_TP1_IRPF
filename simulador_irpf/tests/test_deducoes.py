import pytest
from main.cadastro_de_rendimentos import CadastroDeRendimentos
from main.deducao import Deducoes

@pytest.mark.parametrize("descricao,descricao2,descricao3,valor,valor2,valor3,esperado",
    [
        ("Funpresp","Privada","FAPI",900.0,250.0,300.0,[{"descricao":"Funpresp","valor":900.0},{"descricao":"Privada","valor":250.0},{"descricao":"FAPI","valor":300.0}]), 
        ("Privada","Aposentadoria","Funpresp",700.0,850.0,690.0,[{"descricao":"Privada","valor":700.0},{"descricao":"Aposentadoria","valor":850.0},{"descricao":"Funpresp","valor":690.0}]), 
        ("Carne","Livro","Privada",700.80,250.60,360.55,[{"descricao":"Carne","valor":700.80},{"descricao":"Livro","valor":250.60},{"descricao":"Privada","valor":360.55}])
    ])
def testCadastroDeducao(descricao: str,descricao2: str,descricao3: str, valor: float, valor2: float,valor3: float, esperado:list):

    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao,valor)
    deducao.cadastrarOutrasDeducoes(descricao2,valor2)
    deducao.cadastrarOutrasDeducoes(descricao3,valor3)
    resultado = deducao.getOutrasDeducoes()

    assert resultado == esperado
    

@pytest.mark.parametrize("valor,valor2,valor3,esperado",
    [
        (500.0, 150.0, 200.0,[500.0, 150.0, 200.0]), 
        (100.0, 900.0, 850.0,[100.0, 900.0, 850.0]), 
        (1000.0, 1050.0, 2000.0,[1000.0, 1050.0, 2000.0])
    ])
def testCadastrarPensaoAlimenticia(valor: float, valor2: float,valor3: float, esperado:list):
    
    pensao = Deducoes()
    pensao.cadastrarPensaoAlimenticia(valor)
    pensao.cadastrarPensaoAlimenticia(valor2)
    pensao.cadastrarPensaoAlimenticia(valor3)
    resultado = pensao.getpensaoAlimenticia() 

    assert resultado == esperado 

@pytest.mark.parametrize("descricao,descricao2,descricao3,valor,valor2,valor3,esperado",
    [
        ("Aposentadoria","Investimento","Contribuicao",580.7, 149.5, 300.1,[{"descricao":"Aposentadoria","valor":580.7},{"descricao":"Investimento","valor":149.5},{"descricao":"Contribuicao","valor":300.1}]), 
        ("RendaExtra","Rendimento","Poupanca",550.4, 154.0, 201.1,[{"descricao":"RendaExtra","valor":550.4},{"descricao":"Rendimento","valor":154.0},{"descricao":"Poupanca","valor":201.1}]), 
        ("Patrimonio","FundoInvestimento","BeneficiosFiscais",344.9, 169.7, 254.8,[{"descricao":"Patrimonio","valor":344.9},{"descricao":"FundoInvestimento","valor":169.7},{"descricao":"BeneficiosFiscais","valor":254.8}])
    ])
def cadastrarPrevidenciaOficial(descricao: str,descricao2: str,descricao3: str, valor: float, valor2: float,valor3: float, esperado:list):
    
    previdencia = Deducoes()
    previdencia.cadastrarPrevidenciaOficial(descricao,valor)
    previdencia.cadastrarPrevidenciaOficial(descricao2,valor2)
    previdencia.cadastrarPrevidenciaOficial(descricao3,valor3)
    resultado = previdencia.getPrevidenciaOficial() 

    assert resultado == esperado
    
@pytest.mark.parametrize("nome1,nome2,nome3,data_nascimento1,data_nascimento2,data_nascimento3,esperado",
    [
        ("Ernesto da Silva","Marcelo Fernandez","Maria Antonieta",'10/09/2005','14/11/2009','20/10/2012',[{"nome": "Ernesto da Silva", "data_nascimento": '10/09/2005'},{"nome": "Marcelo Fernandez", "data_nascimento": '14/11/2009'},{"nome": "Maria Antonieta", "data_nascimento": "20/10/2012"}]), 
        ("Andressa","Leticia","Marcos","10/11/2009","10/11/2012","10/01/2007",[{"nome": "Andressa", "data_nascimento": "10/11/2009"},{"nome": "Leticia", "data_nascimento": "10/11/2012"},{"nome": "Marcos", "data_nascimento": "10/01/2007"}]), 
        ("Deolane","Pedro","Mia","10/01/2007","10/11/2012","10/11/2009",[{"nome": "Deolane", "data_nascimento": "10/01/2007"},{"nome": "Pedro", "data_nascimento": "10/11/2012"},{"nome": "Mia", "data_nascimento": "10/11/2009"}])
    ])
def testCadastrarDependente(nome1:str,nome2:str,nome3:str,data_nascimento1:str,data_nascimento2:str,data_nascimento3,esperado:list):
    
    dependente = Deducoes()
    dependente.cadastrarDependente(nome1,data_nascimento1)
    dependente.cadastrarDependente(nome2,data_nascimento2)
    dependente.cadastrarDependente(nome3,data_nascimento3)
    resultado = dependente.getDependentes()

    assert resultado == esperado

@pytest.mark.parametrize("descricao1,descricao2,nome,data_nascimento,nome2,data_nascimento2,valor1,valor2,valor3,valor4,esperado",
    [
        ("Privada","FAPI","Maria",'10/09/2005','Joao','20/10/2012',400.0,150.0,379.18,700.00,1629.18), 
        ("Aposentadoria","Funpresp","Marcos","10/11/2009","Nilmar","10/01/2007",1250.00,600.00,379.18,670.00,2899.18), 
        ("FAPI","Investimento","Mia","10/01/2007","Jorge","10/11/2009",700.50,900.00,379.18,1200.00,3179.68)
    ])
def testCalculoTotalDeducao(descricao1: str,descricao2: str,nome:str,data_nascimento:str, nome2:str,data_nascimento2:str, valor1: float, valor2: float,valor3: float,valor4: float, esperado:list):
    
    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao1,valor1)
    deducao.cadastrarPrevidenciaOficial(descricao2,valor2)
    deducao.cadastrarDependente(nome,data_nascimento)
    deducao.cadastrarPensaoAlimenticia(valor4)
    deducao.cadastrarDependente(nome2,data_nascimento2)
    
    resultado = deducao.calculoValorTotalDeducoes()
    
    esperado = round((valor1 + valor2 + valor3 + valor4),2)

    assert resultado == esperado
