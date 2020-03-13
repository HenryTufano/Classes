class Retan():
    x=0
    y=0
    ar=0
    per=0
    def altv(self):
        self.x=int(input("Digite o valor de x: "))
        self.y=int(input("Digite o valor de y: "))
    def retorv(self):
        print("o valor de x é: {}".format(self.x))
        print("o valor de y é: {}".format(self.y))
              
    def calar(self):
        self.ar=self.x*self.y
        print("o valor do area é: {}".format(self.ar))
    def calper(self):
        self.per=(self.x+self.y)*2
        print("o valor do perimetro é: {}".format(self.per))





