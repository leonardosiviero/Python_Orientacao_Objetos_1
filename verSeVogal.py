class Verificar:

    def  __init__(self, letra):
        self.letra = letra
        self.vogais = "AEIOU"

    def imprimeLetra(self):
        self.letra = str.upper(self.letra)

    def verVogal(self):
        if self.letra in self.vogais:
            print("Vogal.")
        else:
            print("Consoante.")