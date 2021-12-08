# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

class Populacao_comp:

    def __init__(self, populacao_a, populacao_b, taxa_a, taxa_b):
        self.popA = int(populacao_a)
        self.popB = int(populacao_b)
        self.txA = float(taxa_a)
        self.txB = float(taxa_b)

    def se_maior(self):
        while self.popA < self.popB:
            self.popA = int(round(self.popA * self.txA, 0))
            self.popB = int(round(self.popB * self.txB, 0))

    def qd_maior(self):
        print("População A possui {} habitantes, enquanto População B "
              "possui um número inferior com total de {} habitante."
              .format(self.popA, self.popB))