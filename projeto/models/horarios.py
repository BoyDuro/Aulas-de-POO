from datetime import datetime
class Horario:
    def __init__(self, id, data, confirmado, id_cliente, id_servico):
        self.set_id(id)
        self.set_data(data)

    def set_id(self, id):
        if id < 0: raise ValueError('Id deve ser positivo')
        self.__id = id
    def set_data(self, data):
        if data < datetime.now(): raise ValueError('Data não pode ser no passado')
        self.__data = data
    

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self):
        return f'{self.__id} - {self.__data.strftime("%H%M, %d/%m/%Y")}'
    
    def to_json(self):
        return { 'id':self.__id, 'data':self.__data.strftime("%H%M, %d/%m/%Y") }
    
    @staticmethod
    def from_json(dic):
        return Horario(dic['id'], datetime.strptime(dic['data']))