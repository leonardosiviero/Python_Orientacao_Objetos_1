#Francisco precisa criar a classe chamada Sistema com os métodos le_entrada() e exibe_saida().
# O primeiro, ao ser chamado, deve ler do teclado um texto qualquer e guardar internamente na propriedade texto.
# Já o segundo método, quando for chamado, deve exibir o valor de texto.
# Exemplo de uso:

#sistema = Sistema()
#sistema.le_entrada()
#sistema.exibe_saida()


class Sistema:

    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input()

    def exibe_saida(self):
        print(self.texto)