class Retangulo():
    def _init_(self):
        self.__base = 0         # ATRIBUTOS ENCAPSULADOS
        self.__altura = 0

    def set_base(self, valor):
        if valor < 0:               # O SET DEFINE OS VALORES DIGITADOS COMO AS VARIÁVEIS ENCAPSULADAS
            raise ValueError('Valor deve ser positivo')
        self.__base = valor

    def set_altura(self, valor):
        if valor < 0:
            raise ValueError('Valor deve ser positivo')
        self.__altura = valor

    def get_base(self):
        return self.__base  # VALORES DA BASE E DA ALTURA GUARDADOS
    
    def get_altura(self):
        return self.__altura

    def diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5
    

class UI:
    def main():

        x = Retangulo()

        x.set_base = ( float(input('Digite o valor da base: ')) )
        x.set_altura = ( float(input('Digite o valor da altura: ')) )


        print(f'O retângulo de base = {x.get_base()} e altura {x.get_altura()}')

        diagonal = x.diagonal
        print(f'tem diagonal = {diagonal}')

UI.main()
