#Você não precisa fazer este exercício para continuar no treinamento, mas é bom praticar, certo?
#Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar.
#Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:

#from datas import Data
#d = Data(21,11,2007)
#d.formatada()

#Imprime:

#21/11/2007

class Data:

    def __init__(self, dia, mes, ano):
        print("Formatando uma data")
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{} / {} / {}".format(self.dia, self.mes, self.ano))