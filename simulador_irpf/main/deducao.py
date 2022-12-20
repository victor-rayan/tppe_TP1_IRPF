class Deducoes:
    
    def __init__(self) -> None:
        self.deducoes:list = []
        self.dependentes:list = []
        self.pensaoAlimenticia:list = []
        self.previdenciaOficial: list = []
        self.totalValorDeducao: float = 0.0
    
    def cadastrarOutrasDeducoes(self, descricao: str, valor: float) -> None: 
           
        deducao:dict = {}
        deducao = {"descricao": descricao, "valor": valor}
        self.deducoes.append(deducao)
        self.totalValorDeducao += valor
    
    def cadastrarPensaoAlimenticia(self,valor: float) -> None:

        self.pensaoAlimenticia.append(valor)
        self.totalValorDeducao += valor

    def cadastrarPrevidenciaOficial(self, descricao: str, valor: float) -> None: 
        previdencia:dict = {}
        previdencia = {"descricao": descricao, "valor": valor}
        self.previdenciaOficial.append(previdencia)
        self.totalValorDeducao += valor

    def cadastrarDependente(self, nome: str, data_nascimento: str) -> None:
        
        dependente:dict = {}
        dependente = {"nome": nome, "data_nascimento": data_nascimento}
        self.dependentes.append(dependente)

    def getPrevidenciaOficial(self):
        return self.previdenciaOficial

    def getpensaoAlimenticia(self):
        return self.pensaoAlimenticia

    def getDependentes(self):
        return self.dependentes

    def getOutrasDeducoes(self):
        return self.deducoes

    def getQtdeDependente(self):
        totalDependente:int = 0

        for dependente in self.dependentes:
            totalDependente += 1

        return totalDependente    

    def calculoValorTotalDeducoes(self):
        qtdeDependente = self.getQtdeDependente()
        self.totalValorDeducao += (189.59 * qtdeDependente)
        return round(self.totalValorDeducao,2)      