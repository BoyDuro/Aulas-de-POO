# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: 
            self.__b = v
        else: 
            raise ValueError()
    def set_altura(self, v):
        if v >= 0: 
            self.__h = v
        else: 
            raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2

class Circulo:
    def _init_(self):
        self.__r = 0.0
    def set_raio(self, v):
        if v >= 0:
            self.__r = v
        else:
            raise ValueError()
    def get_raio(self):
        return self.__r
    def calc_area(self):
        return 3.14 * (self.__r**2)
    def calc_circuferencia(self):
        return 2 * 3.14 * self.__r

class Viagem:
    def _init_(self):
        self.__d = 0.0
        self.__t = 0.0
    def set_distancia(self, d):
        if d >= 0:
            self.__d = d
        else:
            raise ValueError()
    def set_tempo(self, t):
        if t >= 0:
            self.__t = t
        else:
            raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_velocidade_media(self):
        return self.__d / self.__t
    
class Banco:
    def _init_(self):
        self.__n = ''
        self.__c = 0
        self.__s = 0.0
    

# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: 
                UI.triangulo()
            elif op == 2: 
                UI.circulo()
            elif op == 3: 
                UI.viagem()


    @staticmethod
    def menu():
        print('1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim')
        op = int(input('Informe uma opção: '))
        return op    

    @staticmethod
    def triangulo():
        print('Cálculo da área do triângulo')
        x = Triangulo()
        x.set_base(float(input('Informe o valor da base: ')))     # método de instância
        x.set_altura(float(input('Informe o valor da altura: ')))
        area = x.calc_area()
        print(f'Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}')

    @staticmethod
    def circulo():
        print('Cálculo da área do círculo')
        x = Circulo()
        x.set_raio(float(input('Informe o valor do raio: ')))
        area = x.calc_area()
        perimetro = x.calc_circuferencia()
        print(f'Um cículo com raio {x.get_raio()} tem área = {area} e perímetro = {perimetro}')

    @staticmethod
    def viagem():
        print('Cálculo da velocidade média')
        x = Viagem()
        x.set_distancia(float(input('Informe o valor da distância: ')))
        x.set_tempo(float(input('Informe o valor do tempo: ')))
        velocidade_media = x.calc_velocidade_media()
        print(f'A viagem de tempo {x.get_tempo()} com distância {x.get_distancia()} teve a velocidade média de {velocidade_media}')



UI.main()