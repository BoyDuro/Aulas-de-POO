from datetime import datetime, timedelta
from enum import Enum

class Sessao(Enum):
    PASSOU = 1
    N_PASSOU = 2

class Cinema:
    def __init__(self, id, nome, data, hora):
        self.set_id(id)
        self.set_nome(nome)
        self.set_data(data)
        self.set_hora(hora)
        self.__situacao = None
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0:
            raise ValueError
        self.__nome = nome
    def set_data(self, data):
        self.__data = data
    def set_hora(self, hora):
        if hora < timedelta():
            raise ValueError
        self.__hora = hora
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_data(self):
        return self.__data
    def get_hora(self):
        return self.__hora
    def get_situacao(self):
        return self.__situacao
    def sessao_passa(self, data):
        if data < datetime.now():
            self.__situacao = Sessao.PASSOU
        else:
            self.__situacao = Sessao.N_PASSOU
    def __str__(self):
        return f'Id: {self.__id} - Nome: {self.__nome} - Data: {datetime.strftime(self.__data, '%d/%m/%Y')} - Horário: {self.__hora}'
    
class CinemaUI:
    __sessoes = []

    @staticmethod
    def main():
        op = 0
        while op !=7:
            op = CinemaUI.menu()
            if op == 1: CinemaUI.inserir()
            if op == 2: CinemaUI.listar()
            if op == 3: CinemaUI.atualizar()
            if op == 4: CinemaUI.excluir()
            if op == 5: CinemaUI.sessao_passada()
            if op == 6: CinemaUI.sessao_futura()
    
    @staticmethod
    def menu():
        print('1 - Inserir  2 - Listar  3 - Atualizar  4 - Excluir  5 - Sessões que passaram  6 - Sessões que não passaram')
        return int(input('Escolha uma opção: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('Digite o id: '))
        nome = input('Digite o nome do filme: ')
        data = datetime.strptime(input('Digite a data do filme: '), '%d/%m/%Y')
        tempo = input('Digite o horário: (H:Min:Sec) ').split(':')
        hora = timedelta(hours=int(tempo[0]), minutes=int(tempo[1]), seconds=int(tempo[2]))
        x = Cinema(id, nome, data, hora)
        cls.__sessoes.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__sessoes:
            print(x)
    
    @classmethod
    def atualizar(cls):
        id = int(input('Digite o id da sessão: '))
        for x in cls.__sessoes:
            if x.get_id() == id:
                nome = input('Digite o NOVO nome: ')
                data = datetime.strptime(input('Digite a NOVA data: '), '%d/%m/%Y')
                tempo = input('Digite o NOVO horário: (H:Min:Sec)').split(':')
                hora = timedelta(hours=int(tempo[0]), minutes=int(tempo[1]), seconds=int(tempo[2]))
                x.set_nome(nome)
                x.set_data(data)
                x.set_hora(hora)
    
    @classmethod
    def excluir(cls):
        id = int(input('Digite o id da sessão: '))
        for x in cls.__sessoes:
            if x.get_id() == id:
                cls.__sessoes.remove(x)

    @classmethod
    def sessao_passada(cls):
        for x in cls.__sessoes:
            x.sessao_passa(x.get_data())
            if x.get_situacao() == Sessao.PASSOU:
                print(x)
    
    @classmethod
    def sessao_futura(cls):
        for x in cls.__sessoes:
            x.sessao_passa(x.get_data())
            if x.get_situacao() == Sessao.N_PASSOU:
                print(x)

CinemaUI.main()