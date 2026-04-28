class Viagem:
    def __init__(self, v, d, l):
        self.set_Destino(v)
        self.set_Distancia(d)
        self.set_litros(l)
    def set_Destino(self, v):
        if len(v) > 0:
            self.__v = v
        else:
            raise ValueError()
    def set_Distancia(self, d):
        if d > 0:
            self.__d = d
        else:
            raise ValueError()
    def set_litros(self, l):
        if l > 0:
            self.__l = l
        else:
            raise ValueError()
    def get_destino(self):
        return self.__v
    def get_distancia(self):
        return self.__d
    def get_litros(self):
        return self.__l
    def consumo(self):
        return self.__d / self.__l
    def __str__(self):
        return f'A viagem para {self.get_destino()}, teve distância = {self.get_distancia()} e gasto em litros {self.get_litros()}'


class UI:
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1:
                UI.calculo()

    @staticmethod
    def menu():
        print('1 - Calcular   2 - Fim')
        op = int(input('Digite sua escolha: '))
        return op

    @staticmethod
    def calculo():
        v = input('Digite seu destino: ')
        d = float(input('Digite a distância percorrida em Km: '))
        l = float(input('Digite o gasto de combustível em litros: '))
        x = Viagem(v, d, l)
        print(x)
        print(f'O gasto total da viagem foi = {x.consumo():.2f}')

UI.main()
