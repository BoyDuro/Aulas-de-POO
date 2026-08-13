from datetime import datetime
class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_fone(fone)
        self.set_nasc(nasc)
    def set_nome(self, nome):
        if nome == '':
            raise ValueError
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf == '':
            raise ValueError
        self.__cpf = cpf
    def set_fone(self, fone):
        if fone == '':
            raise ValueError
        self.__fone = fone
    def set_nasc(self, nasc):
        if nasc > datetime.now():
            raise ValueError
        self.__nasc = nasc
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_fone(self):
        return self.__fone
    def get_nasc(self):
        return self.__nasc
    def idade(self):
        x = datetime.now() - self.__nasc # idade
        dias = x.days                    # dias vividos
        anos = dias // 365
        meses = dias % 365 // 30         # meses
        return f'{anos} ano(s) e {meses} mes(es)'
    def __str__(self):
        return f'nome: {self.__nome} - cpf: {self.__cpf} - fone: {self.__fone} - nasc: {self.__nasc.strftime("%d/%m/%Y")}'