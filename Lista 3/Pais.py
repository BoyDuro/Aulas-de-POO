class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)
    def set_nome(self, n):
        if len(n) > 0:
            self.__n = n
        else:
            raise ValueError()
    def set_populacao(self, p):
        if p > 0:
            self.__p = p
        else:
            raise ValueError()
    def set_area(self, a):
        if a > 0:
            self.__a = a
        else:
            raise ValueError()
    def get_nome(self):
        return self.__n
    def get_populacao(self):
        return self.__p
    def get_area(self):
        return self.__a
    def Densidade(self):
        return self.__p / self.__a
    def __str__(self):
        return f'O {self.get_nome()} tem população = {self.get_populacao()} e área {self.get_area()}'

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
        n = input('Digite o nome do país: ')
        p = float(input('Digite a população do país: '))
        a = float(input('Digite a área do país: '))
        x = Pais(n, p, a)
        print(x)
        print(f'Dito isso, têm densidade demográfica = {x.Densidade():.2f}')

UI.main()
