import pytest
from codigo.cadastro_de_rendimentos import CadastroDeRendimentos
   
@pytest.mark.parametrize("descricao1,descricao2,descricao3,valor1,valor2,valor3",
    [
        ("Aluguel", "Dividendo", "Salario", 5550.59, 4556.71, 8894.0), 
        ("Rendimento", "RendaFixa", "Acoes", 12456.52, 89.73, 86448.77), 
        ("Previdencia", "Venda", "Dividendo", 12.51, 1235.7, 43627.2)
    ])
def testCadastroRendimento(descricao1: str, descricao2: str, descricao3: str, valor1: float, valor2: float, valor3: float):
    simuladorIRPF = CadastroDeRendimentos()

    simuladorIRPF.cadastrarRendimento(descricao1, valor1)
    simuladorIRPF.cadastrarRendimento(descricao2, valor2)
    simuladorIRPF.cadastrarRendimento(descricao3, valor3)

    resultado = simuladorIRPF.getTotalRendimentos()

    assert resultado == valor1 + valor2 + valor3