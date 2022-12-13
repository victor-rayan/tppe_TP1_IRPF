from .rendimento import Rendimento

class CadastroDeRendimentos:
    def __init__(self):
        self._rendimentos: list[Rendimento] = []
    
    def getTotalRendimentos(self) -> float:
        total: float = 0
        for rendimento in self._rendimentos:
            total = total + rendimento.getValor()

        return total

    def cadastrarRendimento(self, descricao, valor):
        novoRendimento = Rendimento(descricao, valor)
        self._rendimentos.append(novoRendimento)