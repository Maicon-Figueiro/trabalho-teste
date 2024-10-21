# Uma eleição costuma ter diversas urnas, por isso implemente a classe Urna, esta deve
# agregar os dados da eleição e da votação. Através do conceito de sobrecarga de operadores
# implemente uma contagem de votos entre as urnas, permitindo a soma de dois objetos da
# classe Urna, concatenando o ID das mesmas (ex. 1_2) e a lista das votações.

from Eleicao import Eleicao
from Votacao import Votacao
from Pessoa import Candidato

class Urna:
    def __init__(self, ID, eleicao):
        self._id = ID
        self._eleicao = eleicao
        self._votacoes = []
        
            
    def __add__(self, other):#soma os dados de votação 
        if isinstance(other, Urna):

            votacao = (self._votacao + other._votacao)
            urna =Urna(self._id + "_" + other._id, self._eleicao )
            urna._votacoes=votacao
            return urna

    # ordem dos candidatos: depEstadual, depFederal, senador, governador, presidente
    def votar(self, nums_candidatos):#achando o candidatoa classe candidato será colocado dentro da lista
        candidatos = []
        for num_candidato in nums_candidatos:
            candidatos.append(self._eleicao.search_candidate_by_number(num_candidato))
        
        votacao = Votacao(candidatos)
        self._votacoes.append(votacao)
        
    def __str__(self,):
        return f"Eleição: {self._candidatos} \n Partidos: {self._partidos} \n Votação: {self._votacao.quant_eleitores()}"