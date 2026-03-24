class Vel_media():
    def _init_(self):
        self.d = 0
        self.h = 0
        self.m = 0
    
    def Calc_Vel_media(self):
        return self.d / (self.h + (self.m/60))

x = Vel_media()

x.d = float(input('Digite a distância percorrida: '))
x.h = float(input('Digite o gasto de horas (somente a HORA): '))
x.m = float(input('Digite o gasto restante em minutos (se tiver extra): '))

Vlm = x.Calc_Vel_media()

print(f'A velocidade média nessa viagem foi {Vlm:.2f}km')