class Funcionario:
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self._salario_base = salario_base
    def get_nome(self):
        return self.__nome
    def get_salario(self):
        return self._salario_base
    def __str__(self):
        return f'{self.__nome} - {self.get_salario()}'

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, gratificacao):
        super().__init__(nome, salario_base)
        self.__gratificacao = gratificacao
    def get_salario(self):
        return super().get_salario() + self.__gratificacao

x = Funcionario('José Maria', 5000)
print(x)
print(x.get_nome())
print(x.get_salario())

y = Gerente('Maria José', 5000, 1000)
print(y)
print(y.get_nome())
print(y.get_salario())