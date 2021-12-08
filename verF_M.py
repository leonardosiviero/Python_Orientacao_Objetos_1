#Verificar o sexo F/M

class VerificaSexo:

    print("Escolha o sexo (F/M): ")

    def __init__(self, sexo):
        self.sexo = sexo

    def sexoMaisculo(self):
        self.sexo = str.upper(self.sexo)
        
    def verSeFouM(self):
        if self.sexo == "M":
            print("Sexo Masculino")
        else:
            print("Sexo Feminino")

