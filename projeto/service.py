from models.cliente import Cliente         # entidade
from models.clientedao import ClienteDAO   # persistência
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horarios import Horario
from models.horariosdao import HorarioDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    @staticmethod
    def horario_inserir(data):
        obj = Horario(0, data)
        HorarioDAO().inserir(obj)
    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)
    @staticmethod
    def horario_atualizar(id, data):
        obj = Horario(id, data)
        HorarioDAO().atualizar(obj)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)