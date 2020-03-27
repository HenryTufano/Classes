class Pessoa(): 
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade 
        self.peso=peso 
        self.altura=altura
    
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura
    
    def envelhecer(self,anos):
        self.i=0
        for self.i in range(anos):
          if(anos<=21):
            self.y=+1         
            self.altura=0.5*self.y+self.altura
    def engordar(self,kg):
        self.peso=self.peso+kg
    def emagrecer(self,kg):
        self.peso=self.peso-kg
    