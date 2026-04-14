class pais:
    def _init_(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0

    def calc_densidade(self):
        return self.populacao / self.area
    
x = pais()

x.nome = input('Digite o nome do país: ')
x.populacao = int(input('Digite sua população: '))
x.area = int(input('Digite a área em km2: '))

densidade_do_pais = x.calc_densidade()

print(f'A densidade demográfica do {x.nome} é: {densidade_do_pais:.2f}')