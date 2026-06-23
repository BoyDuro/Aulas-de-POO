import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    def set_id(self, id):
        if id < 0:
            raise ValueError('Não pode ser valor negativo')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == '':
            raise ValueError('Não pode ser vazio')
        self.__nome = nome
    def set_email(self, email):
        if len(email) == '':
            raise ValueError('Não pode ser vazio')
        self.__email = email
    def set_fone(self, fone):
        if len(fone) == '':
            raise ValueError('Não pode ser vazio')
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f'Id: {self.__id} - Nome: {self.__nome} - Email: {self.__email} - Telefone: {self.__fone}'
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'email': self.__email, 'fone': self.__fone}
    @staticmethod
    def from_json(dic):
        return Cliente(dic['id'], dic['nome'], dic['email'], dic['fone'])
    
class ClienteUI:
    __lista = []

    @staticmethod
    def main():
        op = 0

        while op != 8:
            op = ClienteUI.menu()
            if op == 1: 
                ClienteUI.inserir()
            if op == 2:
                ClienteUI.listar()
            if op == 3:
                ClienteUI.listar_id()
            if op == 4:
                ClienteUI.atualizar()
            if op == 5:
                ClienteUI.excluir()
            if op == 6:
                ClienteUI.abrir()
            if op == 7:
                ClienteUI.salvar()
    
    @staticmethod
    def menu():
        print('1 - Inserir cliente')
        print('2 - Listar clientes')
        print('3 - Listar cliente por Id')
        print('4 - Atualizar cliente')
        print('5 - Excluir cliente')
        print('6 - Abrir arquivo de dados de clientes')
        print('7 - Salvar arquivo de dados de clientes')
        print('8 - Sair')
        
        return int(input('Digite o número do que você quer fazer: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('Digite o id: '))
        nome = input('Digite o nome: ')
        email = input('Digite o E-mail: ')
        fone = input('Digite o telefone: ')
        x = Cliente(id, nome, email, fone)
        cls.__lista.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__lista) == 0:
            print('Lista vazia')
        else:
            for x in cls.__lista:
                print(x)
    
    @classmethod
    def listar_id(cls):
        id = int(input('Digite o id do cliente que quer ver: '))
        for x in cls.__lista:
            if x.get_id() == id:
                print(x)
            else:
                print('Id não existe')

    @classmethod
    def atualizar(cls):
        id = int(input('Digite o id do cliente que quer atualizar: '))
        for x in cls.__lista:
            if x.get_id() == id:
                novo_nome = input('Digite o novo nome: ')
                novo_email = input('Digite o novo E-mail: ')
                novo_fone = input('Digite o novo telefone: ')
                x.set_nome(novo_nome)
                x.set_email(novo_email)
                x.set_fone(novo_fone)
    
    @classmethod
    def excluir(cls):
        id = int(input('Digite o id do cliente que quer excluir: '))
        for x in cls.__lista:
            if x.get_id() == id:
                cls.__lista.remove(x)

    @classmethod
    def abrir(cls):
            arquivo = open('clientes.json', 'r')
            lista_dic = json.load(arquivo)
            cls.__lista.clear()

            for dic in lista_dic:
                cls.__lista.append(Cliente.from_json(dic))
            arquivo.close()
            print('Dados carregados.')
    
    @classmethod
    def salvar(cls):
        arquivo = open('clientes.json', 'w')
        json.dump(cls.__lista, arquivo,  default=Cliente.to_json, indent=2)
        arquivo.close()
        print('Dados salvos')

ClienteUI.main()