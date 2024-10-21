class Eleicao:  
    def __init__(self, candidatos, partidos):  
        self._candidatos = candidatos  
        self._partidos = partidos  

    def __str__(self):  
        try:     
            return f"Candidatos: {self._candidatos} | Partidos: {self._partidos}" 
        except AttributeError:
            return "Deletados"

    @property 
    def candidatos(self): 
        return self._candidatos 

    @candidatos.setter 
    def candidatos(self, candidatos): 
        self._candidatos = candidatos 

    @candidatos.deleter 
    def candidatos(self): 
        del self._candidatos 

    @property 
    def partidos(self): 
        return self._partidos 

    @partidos.setter 
    def partidos(self, partidos): 
        self._partidos = partidos 

    @partidos.deleter 
    def partidos(self): 
        del self._partidos 
        
    def search_candidate_by_number(self, number):
        for candidate in self._candidatos:
            if candidate.numero == number:
                return candidate
        raise Exception(f'candidato {number} não achado')
    
    def search_partido_by_cnpj(self, cnpj):
        for partido in self._partidos:
            if partido.cnpj == cnpj:
                return partido
        raise Exception("partido não encontrado")

if __name__ == "__main__":
    # Exemplo de candidatos e partidos 
    candidatos = ["Candidato 1", "Candidato 2"] 
    partidos = ["Partido A", "Partido B"] 

    # Criando uma eleição com candidatos e partidos 
    eleicao = Eleicao(candidatos, partidos) 
    # Exibindo a eleição 
    print(eleicao) 
    # Alterando os candidatos 
    eleicao.candidatos = ["Candidato 3", "Candidato 4"] 
    # Exibindo a eleição após alterar os candidatos 
    print(eleicao) 
    # Deletando os candidatos 
    del eleicao.candidatos 
    # Exibindo a eleição após deletar os candidatos 
    print(eleicao) 
    # Deletando os partidos 
    del eleicao.partidos 
    # Exibindo a eleição após deletar os partidos 
    print(eleicao) 
