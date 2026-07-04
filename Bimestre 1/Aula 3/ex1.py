class Circulo():
    def _init_(self):
        self.r = 0
        
    def calc_area(self):
        return 2*3.14*self.r


x = Circulo()

x.r = float(input('Digite o valor do raio: '))

a = x.calc_area()
print(f'A área do triângulo é {a:.2f}')