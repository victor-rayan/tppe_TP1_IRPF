from codigo.cadastro_de_rendimentos import CadastroDeRendimentos
   
def testCadastroUmRendimento():
    simuladorIRPF = CadastroDeRendimentos()
    valor1: float = 1000
    descricao = "Salario"

    simuladorIRPF.cadastrarRendimento(descricao, valor1)

    assert valor1 == simuladorIRPF.getTotalRendimentos()

    
def testCadastroDoisRendimentos():
    simuladorIRPF = CadastroDeRendimentos()
    valor1:float = 1000.5
    valor2:float = 2550.2

    simuladorIRPF.cadastrarRendimento("Salario", valor1)
    simuladorIRPF.cadastrarRendimento("Aluguel", valor2)

    resultado = simuladorIRPF.getTotalRendimentos()

    assert resultado == valor1 + valor2

def testCadastroTresRendimentos():
    simuladorIRPF = CadastroDeRendimentos()
    valor1:float = 1000.5
    valor2:float = 2550.2
    valor3:float = 5000.7

    simuladorIRPF.cadastrarRendimento("Salario", valor1)
    simuladorIRPF.cadastrarRendimento("Aluguel", valor2)
    simuladorIRPF.cadastrarRendimento("Heranca", valor3)


    resultado = simuladorIRPF.getTotalRendimentos()

    assert resultado == valor1 + valor2 + valor3


   
