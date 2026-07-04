# A classe é um modelo
class Triangulo:
    # Os atributos da classe serão armazenados em b - base, h - altura
    def _init_(self):
        self.b = 0
        self.h = 0
    # método - cálculo que irá ser feito
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()

x.b = float(input('Informe a base do triângulo: '))
x.h = float(input('Informe o valor da altura: '))

a = x.calc_area()
print(f'A área do triângulo é {a:.2f}')    





y = Triangulo()

y.b = float(input('Informe a base do segundo triângulo: '))
y.h = float(input('Informe o valor da altura: '))

a = y.calc_area()
print(f'A área do segundo triângulo é {a:.2f}')