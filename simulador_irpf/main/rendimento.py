class Rendimento:
    def __init__(self, descricao: str, valor: float) -> None:
        self._descricao = descricao
        self._valor = valor

    def getDescricao(self) -> str:
        return self._descricao

    def getValor(self) -> float:
        return self._valor