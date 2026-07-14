from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 16:
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
            if op == 11:
                UI.profissional_inserir()
            if op == 12:
                UI.profissional_listar()
            if op == 13:
                UI.profissional_pesquisar_nome()
            if op == 14:
                UI.profissional_atualizar()
            if op == 15:
                UI.profissional_excluir()

    @staticmethod
    def menu():
        print('1 - Inserir cliente   6 - Inserir serviço   11 - Inserir profissional')
        print('2 - Listar clientes   7 - Listar serviço   12 - Listar profissional')
        print('3 - Pesquisar cliente por nome   8 - Pesquisar serviço por descrição  13 - Pesquisar profissional por nome')
        print('4 - Atualizar cliente   9 - Atualizar serviço   14 - Atualizar profissional')
        print('5 - Excluir cliente   10 - Excluir serviço   15 - Excluir profisssional')
        print('16 - Sair')

        return int(input('Informe uma opção: '))

    @staticmethod
    def cliente_inserir():
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        fone = input('Informe o telefone: ')
        senha = input('Informe a senha: ')
        Service.cliente_inserir(nome, email, fone, senha)

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
        senha = input('Informe a nova senha: ')
        Service.cliente_atualizar(id, nome, email, fone, senha)

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

    @staticmethod
    def profissional_inserir():
        nome = input('Informe o nome: ')
        email = input('Informe o e-mail: ')
        senha = input('Informe a senha: ')
        especialidade = input('Informe a especialidade: ')
        Service.profissional_inserir(nome, email, senha, especialidade)

    @staticmethod
    def profissional_listar():
        for obj in Service.profissional_listar():
            print(obj)

    @staticmethod
    def profissional_pesquisar_nome():
        iniciais = input('Informe as iniciais do nome: ')
        for obj in Service.profissional_listar_nome(iniciais):
            print(obj)

    @staticmethod
    def profissional_atualizar():
        for obj in Service.profissional_listar():
            print(obj)
        id = int(input('Informe o id do profissional: '))
        nome = input('Informe o novo nome: ')
        email = input('Informe o novo e-mail: ')
        senha = input('Informe a nova senha: ')
        especialidade = input('Informe a nova especialidade: ')
        Service.profissional_atualizar(id, nome, email, senha, especialidade)

    @staticmethod
    def profissional_excluir():
        for obj in Service.profissional_listar():
            print(obj)
        id = int(input('Informe o id do profissional: '))
        Service.profissional_excluir(id)

UI.main()