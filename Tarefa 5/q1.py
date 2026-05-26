from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, dist, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_dist(dist)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: 
            raise ValueError
        self.__id = id
    def set_data(self, data):
        if data > datetime.now():
            raise ValueError
        self.__data = data
    def set_dist(self, dist):
        if dist < 0:
            raise ValueError
        self.__dist = dist
    def set_tempo(self, tempo):
        if tempo < 0:
            raise ValueError
        self.__tempo = tempo
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_dist(self):
        return self.__dist
    def get_tempo(self):
        return self.__tempo
    def pace(self):
        tempo = self.__tempo.total_seconds()
        distancia = self.__dist * 1000
        pace = tempo / distancia
        return timedelta(seconds=pace)
    def __str__(self):
        return f'id: {self.__id} - data: {self.__data} - distância: {self.__dist} - tempo: {self.__tempo}'
    

class TreinoUI:
    __treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = TreinoUI.menu()
            if op == 1: 
                TreinoUI.inserir()
            if op == 2: 
                TreinoUI.listar()
            if op == 3: 
                TreinoUI.listar_Id()
            if op == 4:
                TreinoUI.atualizar()
            if op == 5:
                TreinoUI.excluir()
            if op == 6:
                TreinoUI.MaisRapido()
    
    @staticmethod
    def menu():
        print('1-Inserir, 2-Listar, 3-Listar pelo id 4-Atualizar, 5-Excluir, 6-Treino mais rápido, 9-Fim')
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input('Digite o id: '))
        data = datetime.strptime(input('Informe a data do treino: '), '%d/%m/%Y')
        dist = float(input('Digite o valor da distância: '))
        duracao = input('Informe o tempo (H:Min:Sec): ').split(':')
        tempo = timedelta(hours=int(duracao[0]), minutes=int(duracao[1]), seconds=int(duracao[2]))
        x = Treino(id, data, dist, tempo)
        cls.__treinos.append(x)

    @classmethod
    def listar(cls):
        for x in cls.treinos:
            print(x)

    @classmethod
    def listar_Id(cls):
        id = int(input('Digite o id do treino: '))
        for x in cls.__treinos:
            if x.get_id() == id:
                print(x)

    @classmethod
    def atualizar(cls):
        id = int(input('Digite o id do treino: '))
        for x in  cls.__treinos:
            if x.get_id() == id:
                data = datetime.strptime(input('Informe a NOVA data do treino: '), '%d/%m/%Y')
                dist = float(input('Digite o NOVO valor da distância: '))
                duracao = input('Informe o NOVO tempo (H:Min:Sec): ').split(':')
                tempo = timedelta(hours=int(duracao[0]), minutes=int(duracao[1]), seconds=int(duracao[2]))
                x.set_data(data)
                x.set_dist(dist)
                x.set_tempo(tempo)
    
    @classmethod
    def excluir(cls):
        id = int(input('Digite o id do treino: '))
        for x in cls.__treinos:
            if x.get_id() == id:
                cls.__treinos.remove(x)

    @classmethod
    def MaisRapido(cls):
        pass