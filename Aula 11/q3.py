import json
from datetime import datetime
from enum import Enum

class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12
class Fase(Enum):
    Grupos = 1
    DezesseisAvos = 2
    Oitavas = 3
    Quartas = 4
    Semifinais = 5
    TerceiroLugar = 6
    Final = 7

class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)
    def set_id(self, id):
        if id < 0:
            raise ValueError('Não pode ser negativo')
        self.__id = id
    def set_nome(self, nome):
        if nome == '':
            raise ValueError('Não pode ser vazio')
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla == '':
            raise ValueError('Não pode ser vazio')
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
        return f'Id: {self.__id} - Nome: {self.__nome} - Sigla: {self.__sigla} - Grupo: {self.__grupo.name}'
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'sigla': self.__sigla, 'grupo': self.__grupo.name}
    @staticmethod
    def from_json(dic):
        return Pais(dic['id'], dic['nome'], dic['sigla'], Grupo[dic['grupo']])

class Jogo:
    def __init__(self, id, id_pais1, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)
    def set_id(self, id):
        if id < 0:
            raise ValueError('Não pode ser negativo')
        self.__id = id
    def set_id_pais1(self, id_pais1):
        if id_pais1 < 0:
            raise ValueError('Não pode ser negativo')
        self.__id_pais1 = id_pais1
    def set_id_pais2(self, id_pais2):
        if id_pais2 < 0:
            raise ValueError('Não pode ser negativo')
        self.__id_pais2 = id_pais2
    def set_gols1(self, gols1):
        if gols1 < 0:
            raise ValueError('Não pode ser negativo')
        self.__gols1 = gols1
    def set_gols2(self, gols2):
        if gols2 < 0:
            raise ValueError('Não pode ser negativo')
        self.__gols2 = gols2
    def set_fase(self, fase):
        self.__fase = fase
    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora
    def get_id(self):
        return self.__id
    def get_id_pais1(self):
        return self.__id_pais1
    def get_id_pais2(self):
        return self.__id_pais2
    def get_gols1(self):
        return self.__gols1
    def get_gols2(self):
        return self.__gols2
    def get_fase(self):
        return self.__fase
    def get_data_hora(self):
        return self.__data_hora
    def __str__(self):
        return f'Id: {self.__id} - País 1: {self.__id_pais1} - País 2: {self.__id_pais2} - Placar: {self.__gols1} x {self.__gols2} - Fase: {self.__fase.name} - Data: {self.__data_hora.strftime("%d/%m/%Y %H:%M")}'
    def to_json(self):
        return {'id': self.__id, 'id_pais1': self.__id_pais1, 'id_pais2': self.__id_pais2, 'gols1': self.__gols1, 'gols2': self.__gols2, 'fase': self.__fase.name, 'data_hora': self.__data_hora.strftime('%d/%m/%Y %H:%M')}
    @staticmethod
    def from_json(dic):
        return Jogo(dic['id'], dic['id_pais1'], dic['id_pais2'], dic['gols1'], dic['gols2'], Fase[dic['fase']], datetime.strptime(dic['data_hora'], '%d/%m/%Y %H:%M'))

class UI:
    __lista_p = []
    __lista_j = []

    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            UI.abrir()
            if op == 1:
                UI.inserir_pais()
            if op == 2:
                UI.inserir_jogo()
            if op == 3:
                UI.listar_jogo()

    @staticmethod
    def menu():
        print('1 - Cadastrar país')
        print('2 - Cadrastar jogo')
        print('3 - Listar jogos')
        print('4 - Sair')
        return int(input('Digite uma opção: '))

    @classmethod
    def inserir_pais(cls):
        id = int(input('Digite o id: '))
        nome = input('Digite o nome: ')
        sigla = input('Digite a sigla: ')
        print('1-A  2-B  3-C  4-D  5-E  6-F  7-G  8-H  9-I  10-J  11-K  12-L')
        grupo = Grupo(int(input('Digite o grupo: ')))

        x = Pais(id, nome, sigla, grupo)
        cls.__lista_p.append(x)
        UI.salvar()

    @classmethod
    def inserir_jogo(cls):
        id = int(input('Digite o id: '))
        id_pais1 = int(input('Digite o id do primeiro país: '))
        id_pais2 = int(input('Digite o id do segundo país: '))
        gols1 = int(input('Digite os gols do primeiro país: '))
        gols2 = int(input('Digite os gols do segundo país: '))
        print('1-Grupos 2-Dezesseis Avos 3-Oitavas 4-Quartas 5-Semifinais 6-Terceiro Lugar 7-Final')
        fase = Fase(int(input('Digite a fase: ')))
        data = datetime.strptime(input('Digite a data e hora (dd/mm/aaaa hh:mm): '), '%d/%m/%Y %H:%M')

        x = Jogo(id, id_pais1, id_pais2, gols1, gols2, fase, data)
        cls.__lista_j.append(x)
        UI.salvar()

    @classmethod
    def listar_jogo(cls):
        if len(cls.__lista_j) == 0:
            print('Lista vazia')
        else:
            for x in cls.__lista_j:
                for p in cls.__lista_p:
                    if p.get_id() == x.get_id_pais1():
                        sigla1 = p.get_sigla()
                for p in cls.__lista_p:
                    if p.get_id() == x.get_id_pais2():
                        sigla2 = p.get_sigla()

                print(f'Id: {x.get_id()} - País 1: {sigla1} - País 2: {sigla2} - Placar: {x.get_gols1()} x {x.get_gols2()} - Fase: {x.get_fase().name} - Data: {x.get_data_hora().strftime("%d/%m/%Y %H:%M")}')
    
    @classmethod
    def abrir(cls):
        try:
            arquivo = open('jogos.json', 'r')
            arquivo2 = open('paises.json', 'r')
            lista_dic = json.load(arquivo)
            lista_dic2 = json.load(arquivo2)
            cls.__lista_j.clear()
            cls.__lista_p.clear()

            for dic in lista_dic:
                cls.__lista_j.append(Jogo.from_json(dic))
            for dic in lista_dic2:
                cls.__lista_p.append(Pais.from_json(dic))

            arquivo.close()
            arquivo2.close()
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        arquivo = open('jogos.json', 'w')
        arquivo2 = open('paises.json', 'w')
        json.dump(cls.__lista_j, arquivo, default=Jogo.to_json, indent=2)
        json.dump(cls.__lista_p, arquivo2, default=Pais.to_json, indent=2)
        arquivo.close()
        arquivo2.close()

UI.main()