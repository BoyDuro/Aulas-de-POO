from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, codBarras, dataEmissao, dataVencimento, data_pagto, valorBoleto, valor_pago, situacao_pagamento):
        self.set_codBarras(codBarras)
        self.set_dataEmissao(dataEmissao)
        self.set_dataVencimento(dataVencimento)
        self.set_valorBoleto(valorBoleto)
        self.__dataPagto = None
        self.__valorPago = 0
        self.__situacaoPagamento = Pagamento.EM_ABERTO
    def set_codBarras(self, codBarras):
        if len(codBarras) != 10:
            raise ValueError('Código deve ter 10 dígitos')
        self.__codBarras = codBarras
    def set_dataEmissao(self, dataEmissao):
        if dataEmissao > datetime.now():
            raise ValueError('Data não pode ser no futuro')
        self.__dataEmissao = dataEmissao
    def set_dataVencimento(self, dataVencimento):
        if dataVencimento < datetime.now():
            raise ValueError('Vencimento não pode ser no passado')
        self.__dataVencimento = dataVencimento
    def set_valorBoleto(self, valorBoleto):
        if valorBoleto < 0:
            raise ValueError('Valor não pode ser negativo')
        self.__valorBoleto = valorBoleto
    def Pagar(self, valor_pago):
        if valor_pago < 0:
            raise ValueError('Valor não pode ser negativo')
        if self.__situacao_pagamento != Pagamento.EM_ABERTO:
            raise ValueError('Boleto já foi pago')
        self.__valorPago = valor_pago
        self.__dataPagto = datetime.now()
        if self.__valorBoleto == self.__valor_pago:
            self.__situacaoPagamento = Pagamento.PAGO
        else:
            self.__situacaoPagamento = Pagamento.PAGO_PARCIAL
    def get_codBarras(self):
        return self.__codBarras
    def get_dataEmissao(self):
        return self.__dataEmissao
    def get_dataVencimento(self):
        return self.__dataVencimento
    def get_valorBoleto(self):
        return self.__valorBoleto
    def get_valorPagto(self):
        return self.__valorPagto
    def get_dataPagto(self):
        return self.__dataPagto
    def situacao(self):
        return self.__situacaoPagamento
    def __str__(self):
        s = f'Boleto: {self.__codBarras} - Emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}'
        s += f'Valor: R$ {self.__valorBoleto} - Valor Pago: R$ {self.__valorPago}'
        s += f'Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}'
        s += f'Data de pagamento: {self.__dataPagto}'
        s += f'Situação: {self.__situacaoPagamento}'
        return s
class BoletoUI:
    __boletos = []

    def main():
        op = 0
        while op != 9:
            op = BoletoUI.menu()
