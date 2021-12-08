class Verifica:

    def __init__(self, numero):
        self.numero = numero

    def ver_pos_neg(self):
        if self.numero > 0:
            print("O número digitado é positivo.")
        else:
            print("O número digitado é negativo.")

