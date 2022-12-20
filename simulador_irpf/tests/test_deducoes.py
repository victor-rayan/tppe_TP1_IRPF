import pytest
from main.cadastro_de_rendimentos import CadastroDeRendimentos
from main.deducao import Deducoes

def testCadastroDeducao():
    valor = 200.0
    descricao = "FAPI"

    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao,valor)

    resultado = deducao.getOutrasDeducoes()

    esperado = [{"descricao":descricao,"valor":valor}]

    assert resultado == esperado

def testCadastroDuasDeducao():
    #deducao1
    valor1 = 500.0
    descricao1 = "Funpresp"

    #deducao2
    valor2 = 150.0
    descricao2 = 'Privada'
    
    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao1,valor1)
    deducao.cadastrarOutrasDeducoes(descricao2,valor2)
    resultado = deducao.getOutrasDeducoes()

    esperado = [{"descricao":descricao1,"valor":valor1}, {"descricao":descricao2,"valor":valor2}]
    
    assert resultado == esperado

def testCadastroTresDeducao():

    #deducao1
    valor1 = 500.0
    descricao1 = "Funpresp"

    #deducao2
    valor2 = 150.0
    descricao2 = 'Privada'

    #deducao3
    valor3 = 200.0
    descricao3 = 'FAPI'
    
    deducao = Deducoes()
    deducao.cadastrarOutrasDeducoes(descricao1,valor1)
    deducao.cadastrarOutrasDeducoes(descricao2,valor2)
    deducao.cadastrarOutrasDeducoes(descricao3,valor3)
    resultado = deducao.getOutrasDeducoes()

    esperado = [{"descricao":descricao1,"valor":valor1},{"descricao":descricao2,"valor":valor2},{"descricao":descricao3,"valor":valor3}]

    assert resultado == esperado

def testCadastrarPensaoAlimenticia():
   
    valor1 = 500.0 #pensao 1

    esperado = [valor1]

    pensao = Deducoes()
    pensao.cadastrarPensaoAlimenticia(valor1)
    resultado = pensao.getpensaoAlimenticia()

    assert resultado == esperado
    

def testCadastrarDuasPensaoAlimenticia():
    valor1 = 500.0 #pensao 1
    valor2 = 150.0 #pensao 2
    esperado = [valor1,valor2]

    pensao = Deducoes()
    pensao.cadastrarPensaoAlimenticia(valor1)
    pensao.cadastrarPensaoAlimenticia(valor2)
    resultado = pensao.getpensaoAlimenticia()

    assert resultado == esperado

def testCadastrarTresPensaoAlimenticia():
    valor1 = 500.0 #pensao 1
    valor2 = 150.0 #pensao 2
    valor3 = 200.0 #pensao 3
    esperado = [valor1,valor2,valor3]

    pensao = Deducoes()
    pensao.cadastrarPensaoAlimenticia(valor1)
    pensao.cadastrarPensaoAlimenticia(valor2)
    pensao.cadastrarPensaoAlimenticia(valor3)
    resultado = pensao.getpensaoAlimenticia() 

    assert resultado == esperado 

def cadastrarUmPrevidenciaOficial():
    #previdenciaComplementar1
    valor1 = 550.0
    descricao1 = 'FundoInvestimento'
    
    previdencia = Deducoes()
    previdencia.cadastrarPrevidenciaOficial(descricao1, valor1)
    resultado = previdencia.getPrevidenciaOficial() 
    esperado = [{"descricao":descricao1,"valor":valor1}]
    assert resultado == esperado

def cadastrarDoisPrevidenciaOficial():
    #previdenciaComplementar1
    valor1 = 500.0
    descricao1 = 'Privada'

    #previdenciaComplementar2
    valor2 = 250.0
    descricao2 = 'Complementar'
    
    previdencia = Deducoes()
    previdencia.cadastrarPrevidenciaOficial(descricao1, valor1)
    previdencia.cadastrarPrevidenciaOficial(descricao2,valor2)
    resultado = previdencia.getPrevidenciaOficial() 
    esperado = [{"descricao":descricao1,"valor":valor1},{"descricao":descricao2,"valor":valor2}]
    assert resultado == esperado

def cadastrarTresPrevidenciaOficial():
    #previdenciaComplementar1
    valor1 = 600.0
    descricao1 = 'Aposentadoria'

    #previdenciaComplementar2
    valor2 = 150.0
    descricao2 = 'Investimento'

    #previdenciaComplementar3
    valor3 = 300.0
    descricao3 = 'Contribuicao'

    previdencia = Deducoes()
    previdencia.cadastrarPrevidenciaOficial(descricao1, valor1)
    previdencia.cadastrarPrevidenciaOficial(descricao2,valor2)
    previdencia.cadastrarPrevidenciaOficial(descricao3,valor3)
    resultado = previdencia.getPrevidenciaOficial() 
    esperado = [{"descricao":descricao1,"valor":valor1},{"descricao":descricao2,"valor":valor2},{"descricao":descricao3,"valor":valor3}]
    assert resultado == esperado
    

def testCadastrarUmDependente():
    nome = 'Matheus Alves'
    data_nascimento = '14/12/2000'

    dependente = Deducoes()
    dependente.cadastrarDependente(nome,data_nascimento)
    resultado = dependente.getDependentes()

    esperado = [{"nome": nome, "data_nascimento": data_nascimento}]   

    assert resultado == esperado

def testCadastrarDoisDependente():
    nome1 = 'Samuel Vasconcelos'
    data_nascimento1 = '10/09/2005'

    nome2 = 'Eduarda Tavares'
    data_nascimento2 = '14/11/2009'


    dependente = Deducoes()
    dependente.cadastrarDependente(nome1,data_nascimento1)
    dependente.cadastrarDependente(nome2,data_nascimento2)
    resultado = dependente.getDependentes()

    esperado = [{"nome": nome1, "data_nascimento": data_nascimento1},{"nome": nome2, "data_nascimento": data_nascimento2}]   

    assert resultado == esperado

def testCadastrarTresDependente():
    nome1 = 'Ernesto da Silva'
    data_nascimento1 = '10/09/2005'

    nome2 = 'Marcelo Fernandez'
    data_nascimento2 = '14/11/2009'

    nome3 = 'Maria Antonieta'
    data_nascimento3 = '20/10/2012'

    dependente = Deducoes()
    dependente.cadastrarDependente(nome1,data_nascimento1)
    dependente.cadastrarDependente(nome2,data_nascimento2)
    dependente.cadastrarDependente(nome3,data_nascimento3)
    resultado = dependente.getDependentes()

    esperado = [{"nome": nome1, "data_nascimento": data_nascimento1},{"nome": nome2, "data_nascimento": data_nascimento2},{"nome": nome3, "data_nascimento": data_nascimento3}]   

    assert resultado == esperado