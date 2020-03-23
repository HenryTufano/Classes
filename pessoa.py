from ClassePessoa import Pessoa
op=5
p=Pessoa()
while op!=0:
    op=int(input(" [1] - envelhece \n [2] - engordar \n [3] - emagrecer \n [4] - Informação da pessoa \ndigite a opção: "))
    if op==1:
        p.envelhecer()
    elif op==2:
        p.engordar()
    elif op==3:
        p.emagrecer()
    elif op==4:
        p.info()
