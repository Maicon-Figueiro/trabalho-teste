class Partido:    
    def __init__(self,  nome,cnpj,numero):    
        self._nome=nome    
        self._cnpj=cnpj    
        self._numero=numero  
        
    def __str__(self,):    
        return f"Nome: {self.nome} | CNPJ: {self.cnpj} | Número: {self.numero}"    
    
    @property    
    def nome(self,):    
        return self._nome    
    
    @nome.setter    
    def nome(self, nome):    
        if len(nome) > 50: 
            raise ValueError("O Nome não pode ter 50 caracteres")    
        self._nome=nome   
         
    @nome.deleter    
    def nome(self,):    
      del self._nome   
      
    @property    
    def cnpj(self,):    
        return self._cnpj    
    
    @cnpj.setter    
    def cnpj(self, cnpj):    
        if len(cnpj) > 15: 
            raise ValueError("O numero do cnpj não pode ser maior que 15")    
        self._cnpj=cnpj   
         
    @cnpj.deleter    
    def cnpj(self,):    
        del self.cnpj   
        
    @property     
    def numero(self,):    
        return self._numero   
     
    @numero.setter    
    def numero(self, numero):    
        if len(numero) > 2: 
            raise ValueError("O numero não pode ser maior que 2") 
        self._numero=numero 
        
    @numero.deleter   
    def numero(self,):   
        del self._numero  

if __name__ == "__main__":
    #Partido
    partido = Partido("Maicon", "123456789", "12345")
    print(partido)      
