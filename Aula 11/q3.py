from enum import Enum
from datetime import datetime

class Grupo(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'

class Fase(Enum):
    GRUPOS = 'Fase de Grupos'
    OITAVAS = 'Oitavas de Final'
    QUARTAS = 'Quartas de Final'
    SEMIFINAL = 'Semifinal'
    FINAL = 'Final'

class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_nome(self, nome):
        if nome == '':
            raise ValueError
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla == '':
            raise ValueError
        self.__sigla = sigla
    def set_grupo(self, grupo):
        self.__grupo = grupo
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_sigla(self):
        return self.__sigla
    def get_grupo(self):
        return self.__grupo
    def __str__(self):
        return f'Id: {self.__id} - Nome: {self.__nome} - Sigla: {self.__sigla} - Grupo: {self.__grupo.value}'

class Jogo:
    def __init__(self, id, pais1, pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais1(pais1)
        self.set_id_pais2(pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)

    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_id_pais1(self, pais):
        if pais < 0:
            raise ValueError
        self.__pais1 = pais
    def set_id_pais2(self, pais):
        if pais < 0:
            raise ValueError
        self.__pais2 = pais
    def set_gols1(self, gols):
        if gols < 0:
            raise ValueError
        self.__gols1 = gols
    def set_gols2(self, gols):
        if gols < 0:
            raise ValueError
        self.__gols2 = gols
    def set_fase(self, fase):
        self.__fase = fase
    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora
    def get_id(self):
        return self.__id
    def get_pais1(self):
        return self.__pais1
    def get_pais2(self):
        return self.__pais2
    def get_gols1(self):
        return self.__gols1
    def get_gols2(self):
        return self.__gols2
    def get_fase(self):
        return self.__fase
    def get_data_hora(self):
        return self.__data_hora
    def __str__(self):
        return f'Id: {self.__id} - Id País 1: {self.__pais1}'

class UI:
    __jogos = []

    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1:
                UI.cadastrar()
            if op == 2:
                UI.listar()

    @staticmethod
    def menu():
        print('\n1 - Cadastrar jogo')
        print('2 - Listar jogos')
        print('3 - Sair')

        return int(input('Opção: '))

    @classmethod
    def cadastrar(cls):
        id = int(input('Id do jogo: '))

        nome1 = input('Nome do primeiro país: ')
        sigla1 = input('Sigla: ')
        grupo1 = Grupo[input('Grupo (A-H): ').upper()]
        pais1 = Pais(1, nome1, sigla1, grupo1)

        nome2 = input('Nome do segundo país: ')
        sigla2 = input('Sigla: ')
        grupo2 = Grupo[input('Grupo (A-H): ').upper()]
        pais2 = Pais(2, nome2, sigla2, grupo2)

        gols1 = int(input('Gols do primeiro país: '))
        gols2 = int(input('Gols do segundo país: '))

        fase = Fase[input('Fase (GRUPOS, OITAVAS, QUARTAS, SEMIFINAL, FINAL): ').upper()]

        data_hora = datetime.strptime(
            input('Data e hora (dd/mm/aaaa hh:mm): '),
            '%d/%m/%Y %H:%M'
        )

        jogo = Jogo(id, pais1, pais2, gols1, gols2, fase, data_hora)
        cls.__jogos.append(jogo)

    @classmethod
    def listar(cls):
        if len(cls.__jogos) == 0:
            print('Nenhum jogo cadastrado')
        else:
            for jogo in cls.__jogos:
                print(jogo)

UI.main()