from datetime import datetime
class Paciente:
    def __init__(self, id, nome, c, telefone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(c)
        self.set_telefone(telefone)
        self.set_nasc(nasc)
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
    def set_cpf(self, c):
        if len(c) > 0:
            self.__cpf = c
        else:
            raise ValueError
    def set_telefone(self, telefone):
        if len(telefone) > 0:
            self.__telefone = telefone
        else:
            raise ValueError
    def set_nasc(self, nasc):
        self.__nasc = nasc
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nasc(self):
        return self.__nasc
    def idade(self):
        tempo = datetime.now() - self.__nasc
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f'Idade: {anos} ano(s) e {meses} mes(es)'
    def __str__(self):
        return f'id: {self.get_id()} - nome: {self.get_nome()} - CPF: {self.get_cpf()} - telefone: {self.get_telefone()} - nasc: {self.get_nasc().strftime('%d/%m/%Y')}'

class PacienteUI:
    Pacientes = []
   
    @staticmethod
    def main():
        op = 0
        while op!= 11:
            op = PacienteUI.menu()
            if op == 1:
                PacienteUI.inserir_Paciente()
            if op == 2:
                PacienteUI.listar_Paciente()
            if op == 3:
                PacienteUI.atualizar_Paciente()
            if op == 4:
                PacienteUI.excluir_Paciente()
            if op == 5:
                PacienteUI.Aniversariantes()
    @staticmethod
    def menu():
        print('1 - inserir Paciente  2 - listar Paciente  3 - atualizar Paciente  4 - excluir Paciente  5 - pesquisar  6 - aniversariantes  11 - Sair')
        return int(input('Escolha a opção: '))

    @classmethod
    def inserir_Paciente(cls):
        id = int(input('Id do Paciente: '))
        nome = input('Nome: ')
        cpf = input('CPF: ')
        telefone = input('telefone: ')
        nascimento = datetime.strptime(input('Data de nascimento: '), '%d/%m/%Y')

        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.Pacientes.append(x)
        print('Paciente inserido')
    
    @classmethod
    def listar_Paciente(cls):
        if len(cls.Pacientes) == 0:
            print('Nenhum Paciente cadastrado')

        else:
            for x in cls.Pacientes:
                print(x)
    
    @classmethod
    def atualizar_Paciente(cls):
        PacienteUI.listar_Paciente()

        id = int(input('Informe o id do Paciente: '))

        for x in cls.Pacientes:
            if x.get_id() == id:
                cls.Pacientes.remove(x)

                nome = input('Novo nome: ')
                telefone = input('Novo telefone: ')

                novo = Paciente(id, nome, telefone)

                cls.Pacientes.append(novo)
                print('Paciente atualizado')

    @classmethod
    def excluir_Paciente(cls):
        PacienteUI.listar_Paciente()
        id = int(input('Informe o id do Paciente: '))

        for x in cls.Pacientes:
            if x.get_id() == id:
                cls.Pacientes.remove(x)
                print('Paciente removido')

    @classmethod
    def Aniversariantes(cls):
        for x in cls.Pacientes:
            if (x.get_nasc()).month == (datetime.now()).month:
                print(x.get_nome())

PacienteUI.main()