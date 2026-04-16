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
        self.__B = 0.0
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
        self.__depo = 0.0
        self.__saque = 0.0
    def set_nome(self, n):
        self.__n = n
    def set_numero_conta(self, c):
        if c >= 0:
            self.__c = c
        else:
            raise ValueError()
    def set_saldo(self, s):
        if s >= 0:
            self.__s = s
        else:
            raise ValueError()
    def valor_deposito(self, v):
        if v >= 0:
            self.__depo = v
        else:
            raise ValueError()
    def valor_saque(self, v):
        if v >= 0:
            self.__saque = v
        else:
            raise ValueError()
    def get_nome(self):
        return self.__n
    def get_numero_conta(self):
        return self.__c
    def get_saldo(self):
        return self.__s
    def get_depo(self):
        return self.__depo
    def get_saque(self):
        return self.__saque
    def deposito(self):
        return self.__c + self.__depo
    def saque(self):
        return self.__c - self.__saque
    
class Cinema:
    def _init_(self):
        self.__dia = ''
        self.__hora = 0
        self.__tipo = ''
    def set_dia(self, d):
        self.__dia = d
    def set_hora(self, h):
        if h >= 0 and h <= 24:
            self.__hora = h
        else:
            raise ValueError()
    def set_tipo(self, t):
        self.__tipo = t
    def get_dia(self):
        return self.__dia
    def get_hora(self):
        return self.__hora
    def get_tipo(self):
        return self.__tipo
    def valor_ingresso(self):
        if self.__dia == 'segunda' or self.__dia == 'terça' or self.__dia == 'quinta':
            if self.__tipo == 'meia':
                valor = 8
            else:
                valor = 16
            if self.__hora >= 17:
                valor = (valor/2) + valor
            return valor
        elif self.__dia == 'quarta':
            return 8
        elif self.__dia == 'sexta' or self.__dia == 'sábado' or self.__dia == 'domingo':
            if self.__tipo == 'meia':
                valor = 10
            else:
                valor = 20
            if self.__hora >= 17:
                valor = (valor/2) + valor
            return valor

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
            elif op == 4:
                UI.banco()
            elif op == 5:
                UI.cinema()


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

    @staticmethod
    def banco():
        print('Cálculo para conta bancária')
        x = Banco()
        x.set_nome(float(input('Informe seu nome: ')))
        x.set_numero_conta(float(input('Informe o número da sua conta: ')))
        x.set_saldo(float(input('Informe o seu saldo atual: ')))
        print('Escolha se você quer sacar(1) ou depositar(2):')
        escolha_banco = int(input('Digite sua escolha: '))
        if escolha_banco == 1:
            x.valor_saque(float(input('Digite o valor do saque: ')))
            saque = x.saque()
            print(f'A conta {x.get_numero_conta()}, de {x.get_nome()}, após o saque de {x.get_saque()}, tem saldo = {saque}')
        elif escolha_banco == 2:
            x.valor_deposito(float(input('Digite o valor do depósito: ')))
            deposito = x.deposito()
            print(f'A conta {x.get_numero_conta()}, de {x.get_nome()}, após o depósito de {x.get_depo()}, tem saldo = {deposito}')

    @staticmethod
    def cinema():
        print('Cálculo para cinema')
        x = Cinema()
        x.set_dia(input('Digite o dia da semana, SOMENTE com a primeira palavra e SOMENTE letras minúsculas: '))
        x.set_hora(int(input('Digite o horário que você vai: ')))
        x.set_tipo(input('Informe qual tipo de entrada é (digite "meia" ou "inteira"): '))
        ingresso = x.valor_ingresso()
        print(f'A sua sessão no dia de {x.get_dia()}, de {x.get_hora()} horas, com entrada {x.get_tipo()}, vai lhe custar {ingresso}')

UI.main()