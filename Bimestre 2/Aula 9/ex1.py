class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0:
            raise ValueError
        self.__id = id
    def set_nome(self, nome):
        if nome == '':
            raise ValueError
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f'{self.get_id()} - {self.get_nome()} - {self.get_email()} - {self.get_fone()}'
    
class ContatoUI:
    contatos = [] # Atributo de classe

    @staticmethod
    def main():
        op = 0
        while op!= 6:
            op = ContatoUI.menu()
            if op == 1:
                ContatoUI.inserir()
            if op == 2:
                ContatoUI.listar()
            if op == 3:
                ContatoUI.atualizar()
    
    @staticmethod
    def menu():
        print('1 - inserir  2 - listar  3 - atualizar  4 - excluir  5 - pesquisar  6 - fim')
        return int(input('Escolha a opção: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('Informe o id do contato: '))
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        fone = input('Informe o telefone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)

        ids = []
        ids.append(id)
        print('Contato inserido com sucesso')
        return ids

    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0:
            print('Nenhum contato na agenda')
        else:
            for x in cls.contatos:
                print(x)

    @classmethod
    def atualizar(cls):
        z = input('Digite o id do contato que você quer alterar: ')
        print('DIGITE AS NOVAS INFORMAÇÕES DO CONTATO NOVAMENTE:')
        id = int(input('Informe o id do contato: '))
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        fone = input('Informe o telefone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos[cls.ids.index(z)] = x

        


ContatoUI.main()