from codigo.cadastro_de_rendimentos import CadastroDeRendimentos
   
def testCadastroUmRendimento():
    simuladorIRPF = CadastroDeRendimentos()
    valor1 = 1000
    descricao = "Salario"

    simuladorIRPF.cadastrarRendimento(descricao, valor1)

    assert descricao == simuladorIRPF.getDescricao()
    assert valor1 == simuladorIRPF.getTotalRendimentos()