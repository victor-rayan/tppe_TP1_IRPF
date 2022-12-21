from exceptions.exceptions import (DescricaoEmBrancoException,ValorDeducaoInvalidoException,NomeEmBrancoException)

class Deducoes:
    
    def __init__(self) -> None:
        self.deducoes:list = []
        self.dependentes:list = []
        self.pensaoAlimenticia:list = []
        self.previdenciaOficial: list = []
        self.totalValorDeducao: float = 0.0
    
    def cadastrarOutrasDeducoes(self, descricao: str, valor: float) -> None: 
        if descricao == None or descricao == "":
            raise DescricaoEmBrancoException
        if valor <= 0 or valor == None:
            raise ValorDeducaoInvalidoException
           
        deducao:dict = {}
        deducao = {"descricao": descricao, "valor": valor}
        self.deducoes.append(deducao)
        self.totalValorDeducao += valor
    
    def cadastrarPensaoAlimenticia(self,valor: float) -> None:
        if valor <= 0 or valor == None:
            raise ValorDeducaoInvalidoException
        
        self.pensaoAlimenticia.append(valor)
        self.totalValorDeducao += valor

    def cadastrarPrevidenciaOficial(self, descricao: str, valor: float) -> None:
        if descricao == None or descricao == "":
            raise DescricaoEmBrancoException
        if valor <= 0 or valor == None:
            raise ValorDeducaoInvalidoException  
        
        previdencia:dict = {}
        previdencia = {"descricao": descricao, "valor": valor}
        self.previdenciaOficial.append(previdencia)
        self.totalValorDeducao += valor

    def cadastrarDependente(self, nome: str, data_nascimento: str) -> None:
        if nome == None or nome == "":
            raise NomeEmBrancoException
        
        dependente:dict = {}
        dependente = {"nome": nome, "data_nascimento": data_nascimento if data_nascimento else None}
        self.dependentes.append(dependente)

    def getPrevidenciaOficial(self) -> list:
        return self.previdenciaOficial

    def getpensaoAlimenticia(self)-> list:
        return self.pensaoAlimenticia

    def getDependentes(self)-> list:
        return self.dependentes

    def getOutrasDeducoes(self)-> list:
        return self.deducoes

    def getQtdeDependente(self)-> int:
        totalDependente:int = 0

        for dependente in self.dependentes:
            totalDependente += 1

        return totalDependente    

    def calculoValorTotalDeducoes(self)-> float:
        qtdeDependente = self.getQtdeDependente()
        self.totalValorDeducao += (189.59 * qtdeDependente)
        return round(self.totalValorDeducao,2)      