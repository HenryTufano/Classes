class Pessoa(): 
    def __init__(self):
        self.nome=input("Digite o nome do Meliante: ")
        self.idade=int(input("Digite a idade do Meliante: "))
        self.peso=int(input("Digite p peso do Meliante: "))
        self.altura=int(input("Digite a altura do Meliante: "))
    def envelhecer(self):
        self.t=int(input("Digite a quantidades de ano a ser envelhecido: "))
        self.idade=self.t+self.idade
        self.y=self.idade-21
        self.x=self.t-self.y
        if( self.x>=0):
            self.altura=0.5*self.x+self.altura
    def engordar(self):
        self.g=int(input("Digite a quantidade de quilos a ser engordado: "))
        self.peso=self.peso+self.g
    def emagrecer(self):
        self.e=int(input("Digite a quantidade de quilos a ser emagrecido: "))
        self.peso=self.peso-self.e
    def crescer(self):
        self.c=int(input("Digite a quantidades de quilos a ser engordado: "))
        self.altura=self.altura+self.c
    def info(self):
        print("O nome do meliante é : {}".format(self.nome))
        print("A idade do meliante é : {}".format(self.idade))
        print("O peso do meliante é : {} Kg".format(self.peso))
        print("A altura do meliante é : {} cm".format(self.altura))