import json
from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_nasc(nasc)
    def set_id(self, id):
        if id < 0:
            raise ValueError('Não pode ser valor negativo')
        self.__id = id
    def set_nome(self, nome):
        if nome == '':
            raise ValueError('Não pode ser vazio')
        self.__nome = nome
    def set_email(self, email):
        if email == '':
            raise ValueError('Não pode ser vazio')
        self.__email = email
    def set_telefone(self, telefone):
        if telefone == '':
            raise ValueError('Não pode ser vazio')
        self.__telefone = telefone
    def set_nasc(self, nasc):
        if nasc > datetime.now():
            raise ValueError('Data de nascimento não pode ser no futuro')
        self.__nasc = nasc
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_telefone(self):
        return self.__telefone
    def get_nasc(self):
        return self.__nasc
    def __str__(self):
        return f'Id: {self.__id} - Nome: {self.__nome} - Email: {self.__email} - Telefone: {self.__telefone} - Nascimento: {self.__nasc.strftime("%d/%m/%Y")}'
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'email': self.__email, 'telefone': self.__telefone, 'nasc': self.__nasc.strftime('%d/%m/%Y')}
    @staticmethod
    def from_json(dic):
        return Contato(dic['id'], dic['nome'], dic['email'], dic['telefone'], datetime.strptime(dic['nasc'], '%d/%m/%Y'))

class ContatoUI:
    __lista = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = ContatoUI.menu()
            ContatoUI.abrir()

            if op == 1:
                ContatoUI.inserir()
            if op == 2:
                ContatoUI.listar()
            if op == 3:
                ContatoUI.listar_id()
            if op == 4:
                ContatoUI.atualizar()
            if op == 5:
                ContatoUI.excluir()
            if op == 6:
                ContatoUI.pesquisar()
            if op == 7:
                ContatoUI.aniversariantes()

    @staticmethod
    def menu():
        print('1 - Inserir contato   2 - Listar contatos')
        print('3 - Listar contato por Id   4 - Atualizar contato')
        print('5 - Excluir contato   6 - Pesquisar por iniciais')
        print('7 - Listar aniversariantes   10 - Sair\n')

        return int(input('Digite o número do que você quer fazer: '))

    @classmethod
    def inserir(cls):
        id = int(input('Digite o id: '))
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')
        nasc = datetime.strptime(input('Digite a data (dd/mm/aaaa): '), '%d/%m/%Y')

        x = Contato(id, nome, email, telefone, nasc)
        cls.__lista.append(x)
        ContatoUI.salvar()

    @classmethod
    def listar(cls):
        if len(cls.__lista) == 0:
            print('Lista vazia')
        else:
            for x in cls.__lista:
                print(x)

    @classmethod
    def listar_id(cls):
        id = int(input('Digite o id do contato que quer ver: '))

        for x in cls.__lista:
            if x.get_id() == id:
                print(x)
            else:
                print('Id não existe')

    @classmethod
    def atualizar(cls):
        id = int(input('Digite o id do contato que quer atualizar: '))

        for x in cls.__lista:
            if x.get_id() == id:
                nome = input('Digite o novo nome: ')
                email = input('Digite o novo email: ')
                fone = input('Digite o novo telefone: ')
                nasc = datetime.strptime(input('Digite a nova data (dd/mm/aaaa): '),'%d/%m/%Y')
                x.set_nome(nome)
                x.set_email(email)
                x.set_telefone(fone)
                x.set_nasc(nasc)
                ContatoUI.salvar()

    @classmethod
    def excluir(cls):
        id = int(input('Digite o id do contato que quer excluir: '))

        for x in cls.__lista:
            if x.get_id() == id:
                cls.__lista.remove(x)
                ContatoUI.salvar()

    @classmethod
    def pesquisar(cls):
        iniciais = input('Digite as iniciais: ')

        for x in cls.__lista:
            if x.get_nome().startswith(iniciais):
                print(x)

    @classmethod
    def aniversariantes(cls):
        mes = int(input('Digite o mês: '))

        for x in cls.__lista:
            if x.get_nasc().month == mes:
                print(x)

    @classmethod
    def abrir(cls):
        try:
            arquivo = open('contatos.json', 'r')
            lista_dic = json.load(arquivo)
            cls.__lista.clear()

            for dic in lista_dic:
                cls.__lista.append(Contato.from_json(dic))

            arquivo.close()
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        arquivo = open('contatos.json', 'w')
        json.dump(cls.__lista, arquivo, default=Contato.to_json, indent=2)
        arquivo.close()

ContatoUI.main()