import pytest
from main.cadastro_de_rendimentos import CadastroDeRendimentos
from main.deducao import Deducoes

@pytest.mark.parametrize("descricao,descricao2,descricao3,valor,valor2,valor3,esperado",
    [
        ("Funpresp","Privada","FAPI",500.0,150.0,200.0,[{"descricao":"Funpresp","valor":500.0},{"descricao":"Privada","valor":150.0},{"descricao":"FAPI","valor":200.0}]), 
        ("Funpresp","Privada","FAPI",500.0,150.0,200.0,[{"descricao":"Funpresp","valor":500.0},{"descricao":"Privada","valor":150.0},{"descricao":"FAPI","valor":200.0}]), 
        ("Funpresp","Privada","FAPI",500.0,150.0,200.0,[{"descricao":"Funpresp","valor":500.0},{"descricao":"Privada","valor":150.0},{"descricao":"FAPI","valor":200.0}])
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

def testCadastrarTotalDeducoes():
    #deducao1
    valor1 = 500.0
    descricao1 = "Funpresp"

    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao1,valor1)
    resultado = deducao.calculoValorTotalDeducoes()
    
    esperado = valor1 

    assert resultado == esperado

def testCadastroDoisTotalDeducoes():
    valor1 = 400.0 #deducao1

    valor2 = 150.0 #deducao2
    descricao2 = 'Privada'

    valor3 = 200.0 #deducao3
    descricao3 = 'FAPI'
    
    deducao = Deducoes()
    deducao.cadastrarPensaoAlimenticia(valor1)
    deducao.cadastrarOutrasDeducoes(descricao2,valor2)
    deducao.cadastrarPrevidenciaOficial(descricao3,valor3)
    resultado = deducao.calculoValorTotalDeducoes()
    
    esperado = valor1 + valor2 + valor3

    assert resultado == esperado

def testCadastroTresTotalDeducoes():
    valor1 = 400.0 #deducao1

    valor2 = 150.0 #deducao2
    descricao2 = 'Privada'

    valor3 = 200.0 #deducao3
    descricao3 = 'FAPI'
    
    valor4 = 189.59

    nome = 'Maria' #deducao4
    data_nascimento = '14/12/2000'
    
    deducao = Deducoes()
    deducao.cadastrarPensaoAlimenticia(valor1)
    deducao.cadastrarOutrasDeducoes(descricao2,valor2)
    deducao.cadastrarPrevidenciaOficial(descricao3,valor3)
    deducao.cadastrarDependente(nome,data_nascimento)

    resultado = deducao.calculoValorTotalDeducoes()
    
    esperado = valor1 + valor2 + valor3 + valor4

    assert resultado == esperado 
