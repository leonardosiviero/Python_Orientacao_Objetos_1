class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo de R${} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_para_sacar)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R${}, ultrapassa limite da conta.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self): #GET usado sempre qnd quer pegar um atributo
        return self.__limite

    @limite.setter
    def limite(self, limite): #SET usado para alterar a atributo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}

#from conta import Conta
#conta = Conta(123, "Leonardo", 55.5, 1000.0)
#conta2 = Conta(456, "Antonio", 100.0, 500.0)
#conta.deposita(150.0)
#conta2.numero
#conta2.extrato()
#codigos = Conta.codigos_bancos()

