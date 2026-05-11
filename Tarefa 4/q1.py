class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError
    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError
    def set_estado(self, estado):
        if len(estado) > 0:
            self.__estado = estado
        else:
            raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def __str__(self):
        return f'O Time {self.get_nome()} do Estado de {self.get_estado()} tem id: {self.get_id()}'

class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)
    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError
    def set_idTime(self, idTime):
        if idTime > 0:
            self.__idTime = idTime
        else:
            raise ValueError
    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError
    def set_camisa(self, camisa):
        if camisa > 0 and camisa <= 99:
            self.__camisa = camisa
        else:
            raise ValueError
    def get_id(self):
        return self.__id
    def get_idTime(self):
        return self.__idTime
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def __str__(self):
        return f'O jogador {self.get_nome()}, camisa {self.get_camisa()} tem id: {self.get_id()}'
    

class TimeUI:
    times = []
    jogadores = []
   
    @staticmethod
    def main():
        op = 0
        while op!= 11:
            op = TimeUI.menu()
            if op == 1:
                TimeUI.inserir_time()
            if op == 2:
                TimeUI.listar_time()
            if op == 3:
                TimeUI.atualizar_time()
            if op == 4:
                TimeUI.excluir_time()
            if op == 5:
                TimeUI.inserir_jogador()
            if op == 6:
                TimeUI.listar_jogador()
            if op == 7:
                TimeUI.atualizar_jogador()
            if op == 8:
                TimeUI.excluir_jogador()
            if op == 9:
                TimeUI.listar_jogadores_time()
            if op == 10:
                TimeUI.transferir_jogador()
    
    @staticmethod
    def menu():
        print('1 - inserir time  2 - listar time  3 - atualizar time  4 - excluir time  5 - inserir jogador  6 - listar jogador  7 - atualizar jogador  8 - excluir jogador  9 - listar jogadores do time  10 - transferir jogador para outro time  11 - Sair')
        return int(input('Escolha a opção: '))

    @classmethod
    def inserir_time(cls):
        id = int(input('Id do time: '))
        nome = input('Nome: ')
        estado = input('Estado: ')

        x = Time(id, nome, estado)
        cls.times.append(x)
        print('Time inserido')
    
    @classmethod
    def listar_time(cls):
        if len(cls.times) == 0:
            print('Nenhum time cadastrado')

        else:
            for x in cls.times:
                print(x)
    
    @classmethod
    def atualizar_time(cls):
        TimeUI.listar_time()

        id = int(input('Informe o id do time: '))

        for x in cls.times:
            if x.get_id() == id:
                cls.times.remove(x)

                nome = input('Novo nome: ')
                estado = input('Novo estado: ')

                novo = Time(id, nome, estado)

                cls.times.append(novo)
                print('Time atualizado')

    @classmethod
    def excluir_time(cls):
        TimeUI.listar_time()
        id = int(input('Informe o id do time: '))

        for x in cls.times:
            if x.get_id() == id:
                cls.times.remove(x)
                print('Time removido')
    
    @classmethod
    def inserir_jogador(cls):
        id = int(input('Informe o id do jogador: '))
        idTime = int(input('Informe o id do time: '))
        nome = input('Informe o nome: ')
        camisa = int(input('Informe a camisa: '))

        x = Jogador(id, idTime, nome, camisa)
        cls.jogadores.append(x)
        print('Jogador inserido')

    @classmethod
    def listar_jogador(cls):
        if len(cls.jogadores) == 0:
            print('Nenhum jogador cadastrado')

        else:
            for x in cls.jogadores:
                print(x)

    @classmethod
    def atualizar_jogador(cls):
        TimeUI.listar_jogador()

        id = int(input('Informe o id do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                cls.jogadores.remove(x)

                idTime = int(input('Novo id do time: '))
                nome = input('Novo nome: ')
                camisa = int(input('Nova camisa: '))

                novo = Jogador(id, idTime, nome, camisa)

                cls.jogadores.append(novo)
                print('Jogador atualizado')

    @classmethod
    def excluir_jogador(cls):
        TimeUI.listar_jogador()
        id = int(input('Informe o id do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                cls.jogadores.remove(x)
                print('Jogador removido')

    @classmethod
    def listar_jogadores_time(cls):
        idTime = int(input('Informe o id do time: '))

        for x in cls.jogadores:
            if x.get_idTime() == idTime:
                print(x)

    @classmethod
    def transferir_jogador(cls):
        TimeUI.listar_jogador()

        id = int(input('Informe o id do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                novoTime = int(input('Novo id do time: '))
                x.set_idTime(novoTime)

                print('Jogador transferido')

TimeUI.main()