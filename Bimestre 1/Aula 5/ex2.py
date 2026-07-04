class pais:
    def _init_(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0

    def calc_densidade(self):
        return self.populacao / self.area
    
lista_paises = []
lista_nomes = []

for b in range(10):
    b = pais()
    b.nome = input('Digite o nome do país: ')
    b.populacao = int(input('Digite sua população: '))
    b.area = int(input('Digite a área em km2: '))
    densidade_do_pais = b.calc_densidade()
    lista_paises.append(densidade_do_pais)
    lista_nomes.append(b.nome)

maior_densidade = max(lista_paises)
indice = lista_paises.index(maior_densidade)

print(f'O país com a maior densidade demográfica é {lista_nomes[indice]}, com densidade de {maior_densidade}')