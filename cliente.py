#Criar cadastro de cliente

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self):
        print("chamando setter nome()")
        return self.__nome = nome



# Teste: from cliente import
# Cliente: cliente = Cliente("nico")
# cliente.nome = "marco"