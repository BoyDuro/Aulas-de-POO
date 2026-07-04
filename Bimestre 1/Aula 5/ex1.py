class agua():
    def _init_(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0

    def conta_dagua(self):
        consumo_m = self.consumo//1000

        if consumo_m <= 10:
            return 38
        elif consumo_m >= 11 and consumo_m <= 20:
            return (38 + 5*(consumo_m - 10))
        elif consumo_m >= 21:
            return (88 + 6*(consumo_m - 20))
        
x = agua()

x.mes = 'março'
x.ano = '2026'
x.consumo = 40000

valor_total = x.conta_dagua()

print(f'O consumo do mês de {x.mes} de {x.ano} foi {valor_total} reais')