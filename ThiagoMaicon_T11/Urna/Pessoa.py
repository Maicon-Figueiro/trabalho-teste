class Pessoa():    
    def __init__(self,nome, CPF, data_nascimento):   
        self._nome=nome    
        self._CPF=CPF    
        self._data_nascimento=data_nascimento    
        
    def __str__(self) -> str:    
        return f"Nome: {self.nome} | CPF: {self.CPF} | Data de Nascimento: {self.data_nascimento}"    
    
    @property    
    def nome(self,):    
        return self._nome    
    
    @nome.setter    
    def nome(self, nome):    
        if len(nome) > 50: 
            raise ValueError("O nome pode ter no máximo 50 caracteres")    
        self._nome=nome 
        
    @nome.deleter    
    def nome(self,):    
        del self.nome  
        
    @property    
    def CPF(self,):    
        return self._CPF    
    @CPF.setter    
    def CPF(self, CPF):    
        if len(CPF) > 11: 
            raise ValueError("O CPF não pode ser maior que 11")   
        
    @CPF.deleter    
    def CPF(self,):    
        del self._CPF  
    
    @property    
    def data_nascimento(self,):    
        return self._data_nascimento  
    
    @data_nascimento.setter    
    def dataNascimento(self,data_nascimento):    
        self._data_nascimento=data_nascimento    
        
    @data_nascimento.deleter    
    def data_nascimento(self,):    
        del self._data_nascimento    

from abc import ABC, abstractmethod 
class Candidato(Pessoa):    
    def __init__(self, nome, CPF, data_nascimento, numero,partido, proposta):    
        super().__init__(nome, CPF, data_nascimento)   
        self._numero = numero   
        self._partido = partido   
        self._proposta = proposta   
        
    def __str__(self,):   
        return f"Numero: {self.numero} | Partido: {self.partido} | Proposta: {self.proposta}"   
    
    @abstractmethod    
    def verifica_numero_cargo(self,):    
        pass   
    
    @property   
    def numero(self,):   
        return self._numero   
    
    @numero.setter   
    def numero(self,numero):   
        self._numero=numero   
        
    @numero.deleter   
    def numero(self,):   
        del self._numero  

    @property 
    def partido(self,): 
        return self._partido 
    
    @partido.setter 
    def partido(self,partido): 
        self._partido=partido 
        
    @partido.deleter 
    def partido(self,): 
        del self._partido 

    @property 
    def proposta(self,): 
        return self._proposta 
    
    @proposta.setter 
    def proposta(self, proposta): 
        self._proposta = proposta 
        
    @proposta.deleter 
    def proposta(self,): 
        del self._proposta 

class DepFederal(Candidato):    
    def __init__(self, nome, CPF, data_nascimento, numero, partido, proposta):   
        super().__init__(nome, CPF, data_nascimento,numero, partido, proposta)   

    def verifica_numero_cargo(self):    
            if len(str(self._numero)) == 4: 
                print(f"O número {self._numero} está de acordo com o cargo") 
            else: 
                raise ValueError("O número está errado") 
            
class DepEstadual(Candidato): 
    def __init__(self,nome, CPF, data_nascimento, numero,partido, proposta): 
        super().__init__(nome, CPF, data_nascimento, numero, partido, proposta)   
        
    def verifica_numero_cargo(self):   
            if len(str(self._numero)) == 5:
                print(f"O número {self._numero} está de acordo com o cargo.") 
            else: 
                raise ValueError("O número está errado")
            
class Senador(Candidato): 
    def __init__(self,nome, CPF, data_nascimento, numero,partido, proposta): 
        super().__init__(nome, CPF, data_nascimento, numero, partido, proposta)   
        
    def verifica_numero_cargo(self):     
            if len(str(self._numero)) == 3:   
                print(f"O número {self._numero} está de acordo com o cargo.")   
            else:   
                raise ValueError("O número está errado")   
    
class Governador(Candidato): 
    def __init__(self,nome, CPF, data_nascimento, numero,partido, proposta): 
        super().__init__(nome, CPF, data_nascimento, numero, partido, proposta) 
        
    def verifica_numero_cargo(self):   
            if len(str(self._numero)) == 2: 
                print(f"O número {self._numero} está de acordo com o cargo.")   
            else: 
                raise ValueError("O número está errado!!") 
            
class Presidente(Candidato): 
    def __init__(self,nome, CPF, data_nascimento, numero, partido, proposta): 
        super().__init__(nome, CPF, data_nascimento, numero, partido, proposta) 
        
    def verifica_numero_cargo(self):   
            if len(str(self._numero)) == 2:
                print(f"O número {self._numero} está de acordo com o cargo.") 
            else: 
                raise ValueError("O número está errado")


if __name__ == "__main__":
    # Exemplo de uso        
    pessoa = Pessoa("Thiago Farias", "12345678910", "01/01/1980")
    print(pessoa)

    # deputado federal
    candidato_dep_federal = DepFederal("Maria Souza", "10987654321", "15/05/1975", 1234, "Partido X", "Proposta Y", 1234)
    print(candidato_dep_federal)
    candidato_dep_federal.verifica_numero_cargo()

    #deputado estadual
    candidato_dep_estadual = DepEstadual("Carlos Alberto", "98765432101", "23/03/1982", 5678, "Partido Y", "Proposta Z", 5678)
    print(candidato_dep_estadual)
    candidato_dep_estadual.verifica_numero_cargo()

    #Senador
    senador = Senador("Vinicius almeida", "60039900012", "10/12/1990", 4321, "Partido Z", "Proposta X", 4321)
    print(senador)
    senador.verifica_numero_cargo()

    #Presidente
    presidente = Presidente("Rafaella Rossoni", "60369503052", "22/05/1988", 6789, "Partido H", "Proposta T", 6789)
    print(presidente)
    presidente.verifica_numero_cargo()

    #Governador
    governador = Governador("Ener Valencia", "30059967842", "20/10/1996", 5000, "Partido E", "Proposta O", 5000)
    print(governador)
    governador.verifica_numero_cargo()