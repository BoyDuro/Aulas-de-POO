from datetime import datetime
class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avalicao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(0)
    
    def set_id(self, id):
        if id < 0: raise ValueError('Id deve ser positivo')
        self.__id = id
    def set_data(self, data):
        self.__data = data
    def set_queixa_principal(self, queixa):
        if queixa == '': raise ValueError('Queixa deve ser informada')
        self.__queixa_principal = queixa
    def set_historico_saude(self, historico):
        if historico == '': raise ValueError('Histórico deve ser informado')
        self.__historico_saude = historico
    def set_avalicao(self, avaliacao):
        if avaliacao == '': raise ValueError('Avaliação deve ser informada')
        self.__avaliacao = avaliacao
    def set_prescricao(self, prescricao):
        if prescricao == '': raise ValueError('Prescrição deve ser informada')
        self.__prescricao = prescricao
    def set_id_horario(self, horario):
        self.__id_horario = horario

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario


    def __str__(self):
        return f'{self.__id} - {self.__data.strftime("%d/%m/%Y %H:%M")} - {self.__queixa_principal} - {self.__historico_saude} - {self.__avaliacao} - {self.__prescricao} - {self.__id_horario}'
    
    def to_json(self):
        return { 'id':self.__id, 'data':self.__data.strftime("%d/%m/%Y %H:%M"), 'queixa':self.__queixa_principal, 'historico':self.__historico_saude, 'avaliacao':self.__avaliacao, 'prescricao':self.__prescricao, 'id_horario':self.__id_horario}
    
    @staticmethod
    def from_json(dic):
        atendimento = Atendimento(dic['id'], datetime.strptime(dic['data'], "%d/%m/%Y %H:%M"), dic['queixa'], dic['historico'], dic['avaliacao'], dic['prescricao'])
        atendimento.set_id_horario(dic['id_horario'])
        return atendimento