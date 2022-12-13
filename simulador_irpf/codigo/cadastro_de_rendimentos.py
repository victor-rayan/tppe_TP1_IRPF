from .rendimento import Rendimento

class CadastroDeRendimentos:
    def __init__(self):
        self._rendimentos: list[Rendimento] = []

    def getDescricao(self) -> str:
        return "Salario"

    def getTotalRendimentos(self) -> list[Rendimento]:
        return 1000

    def cadastrarRendimento(self, descricao, valor):
        self._rendimento = Rendimento(descricao, valor)