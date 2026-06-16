from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
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
        if self.__situacaoPagamento != Pagamento.EM_ABERTO:
            raise ValueError('Boleto já foi pago')
        self.__valorPago = valor_pago
        self.__dataPagto = datetime.now()
        if self.__valorBoleto == self.__valorPago:
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
        s = f'Boleto: {self.__codBarras} - Emissão: {datetime.strftime(self.__dataEmissao, '%d/%m/%Y')} '
        s += f'Valor: R$ {self.__valorBoleto} - Valor Pago: R$ {self.__valorPago} '
        s += f'Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')} '
        s += f'Data de pagamento: {self.__dataPagto} '
        s += f'Situação: {self.__situacaoPagamento} '
        return s
class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()
            if op == 1:
                BoletoUI.inserir()
            elif op == 2:
                BoletoUI.listar()
            elif op == 3:
                BoletoUI.atualizar()
            elif op == 4:
                BoletoUI.excluir()
            elif op == 5:
                BoletoUI.emAberto()
            elif op == 6:
                BoletoUI.pagos()
            elif op == 7:
                BoletoUI.aVencer()
            elif op == 8:
                BoletoUI.vencidos()
            elif op == 9:
                BoletoUI.pagar()

    @staticmethod
    def menu():
        print('---------------------------------------------')
        print(' 1-Inserir  2-Listar  3-Atualizar  4-Excluir')
        print(' 5-Boletos em Aberto  6-Boletos pagos')
        print(' 7-Boletos a Vencer  8-Boletos Vencidos')
        print(' 9-Pagar Boletos  10-Fim')
        print('---------------------------------------------')
        return int(input('Escolha uma opção: '))

    @classmethod
    def inserir(cls):
        cod = input('Informe o código de 10 dígitos: ')
        emissao = datetime.strptime(input('Informe a data de emissão dd/mm/aaaa: '), '%d/%m/%Y')
        venc = datetime.strptime(input('Informe a data de vencimento dd/mm/aaaa: '), '%d/%m/%Y')
        valor = float(input('Digite o valor do boleto: '))
        x = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(x)
    @classmethod
    def listar(cls):
        for x in cls.__boletos:
            print(x)
    
    @classmethod
    def atualizar(cls):
        cod = input('Informe o código do boleto: ')
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                emissao = datetime.strptime(input('Informe a NOVA data de emissão dd/mm/aaaa: '), '%d/%m/%Y')
                venc = datetime.strptime(input('Informe a NOVA data de vencimento dd/mm/aaaa: '), '%d/%m/%Y')
                valor = float(input('Digite o NOVO valor do boleto: '))
                x.set_dataEmissao(emissao)
                x.set_dataVencimento(venc)
                x.set_valorBoleto(valor)
    
    @classmethod
    def excluir(cls):
        cod = input('Informe o código do boleto: ')
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                cls.__boletos.remove(x)
    
    @classmethod
    def emAberto(cls):
        for x in cls.__boletos:
            if x.situacao() == Pagamento.EM_ABERTO or Pagamento.PAGO_PARCIAL:
                print(x)

    @classmethod
    def pagos(cls):
        for x in cls.__boletos:
            if x.situacao() == Pagamento.PAGO:
                print(x)
    
    @classmethod
    def aVencer(cls):
        for x in cls.__boletos:
            if x.situacao() == Pagamento.EM_ABERTO and x.get_dataVencimento() > datetime.now():
                print(x)

    @classmethod
    def vencidos(cls):
        for x in cls.__boletos:
            if x.situacao() == Pagamento.EM_ABERTO and x.get_dataVencimento() < datetime.now():
                print(x)
    
    @classmethod
    def pagar(cls):
        cod = input('Informe o código do boleto que você vai pagar: ')
        for x in cls.__boletos:
            if x.get_codBarras() == cod:
                valor_pago = float(input('Digite o valor que irá pagar: '))
                x.Pagar(valor_pago)

BoletoUI.main()