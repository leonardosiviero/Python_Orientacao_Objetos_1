#Exercicio para escrever Nome e Sobrenome de uma pessoa

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def NomeSobrenome(self):
        print("{0} {1}".format(self.nome, self.sobrenome))


#Teste:
#pessoa = Pessoa("Chalita", "Steppat")
#pessoa.NomeSobrenome()