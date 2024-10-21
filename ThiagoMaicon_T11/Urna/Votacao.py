# 7) Precisa ter uma Classe chamada Votacao, que armazena todas as escolhas de Candidatos
# de um eleitor. Esta classe precisa implementar um método de classe responsável por
# contar quantos eleitores votaram.

class Votacao:
    total_de_eleitores = 0 # atributo statico da classe

    def __init__(self, candidatos): 
        self._candidatos = candidatos
        Votacao.total_de_eleitores += 1 


    @property
    def candidatos(self,):
        return self._candidatos
    
    @candidatos.setter
    def candidatos(self, candidatos):
        self._candidatos = candidatos

    def quant_eleitores(self): 
        return len(self._eleitores) 
    
    @classmethod
    def quantidade_total_de_eleitores(Votacao):
        return Votacao.total_de_eleitores

if __name__ == "__main__":
    
    # Exemplo de uso
    eleitores = ["Eleitor 1", "Eleitor 2"]

    votacao = Votacao(eleitores)

    # Para ver os eleitores armazenados
    print(votacao.eleitores)

    # Contando os eleitores
    print(votacao.quant_eleitores())
