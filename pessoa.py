from ClassePessoa import Pessoa
op=5
nome=input("Digite o nome do Meliante: ")
idade=int(input("Digite a idade do Meliante: "))
peso=int(input("Digite p peso do Meliante: "))
altura=int(input("Digite a altura do Meliante: "))
p=Pessoa(nome,idade,peso,altura)

while op!=0:
    op=int(input(" [1] - envelhece \n [2] - engordar \n [3] - emagrecer \n [4] - Informação da pessoa \ndigite a opção: "))
    if op==1:
        anos = int(input("Digite a quantidades de ano a ser envelhecido: "))
        p.envelhecer(anos)
        print("A nova idade do meliante é:{0}".format(p.getIdade()))
    elif op==2:
        kg=int(input("Digite a quantidade de quilos a ser engordado: "))
        p.engordar(kg)
    elif op==3:
        kg=int(input("Digite a quantidade de quilos a ser engordado: "))
        p.emagrecer(kg)
    elif op==4:
         print("O nome: {0}".format(p.getNome()))
         print("A idade é: {0} anos".format(p.getIdade()))
         print("O peso é: {0} kg".format(p.getPeso()))
         print("A altura é: {0} cm".format(p.getAltura()))