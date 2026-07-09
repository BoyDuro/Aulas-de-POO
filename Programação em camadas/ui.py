from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            if op == 2:
                UI.cliente_listar()
            if op == 3:
                UI.cliente_pesquisar_nome()
            if op == 4:
                UI.cliente_atualizar()
            if op == 5:
                UI.cliente_excluir()
            if op == 6:
                UI.servico_inserir()
            if op == 7:
                UI.servico_listar()
            if op == 8:
                UI.servico_pesquisar_descricao()
            if op == 9:
                UI.servico_atualizar()
            if op == 10:
                UI.servico_excluir()

    @staticmethod
    def menu():
        print('1 - Inserir cliente')
        print('2 - Listar clientes')
        print('3 - Pesquisar cliente por nome')
        print('4 - Atualizar cliente')
        print('5 - Excluir cliente')
        print('6 - Inserir serviço')
        print('7 - Listar serviços')
        print('8 - Pesquisar serviço por descrição')
        print('9 - Atualizar serviço')
        print('10 - Excluir serviço')
        print('11 - Sair')

        return int(input('Informe uma opção: '))

    @staticmethod
    def cliente_inserir():
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        fone = input('Informe o telefone: ')
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_pesquisar_nome():
        iniciais = input('Informe as iniciais do nome: ')
        for obj in Service.cliente_listar_nome(iniciais):
            print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input('Informe o id do cliente: '))
        nome = input('Informe o novo nome: ')
        email = input('Informe o novo e-mail: ')
        fone = input('Informe o novo telefone: ')
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input('Informe o id do cliente: '))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        descricao = input('Informe a descrição: ')
        valor = float(input('Informe o valor: '))
        Service.servico_inserir(descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar():
            print(obj)

    @staticmethod
    def servico_pesquisar_descricao():
        iniciais = input('Informe as iniciais da descrição: ')
        for obj in Service.servico_listar_descricao(iniciais):
            print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input('Informe o id do serviço: '))
        descricao = input('Informe a nova descrição: ')
        valor = float(input('Informe o novo valor: '))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar():
            print(obj)
        id = int(input('Informe o id do serviço: '))
        Service.servico_excluir(id)

UI.main()