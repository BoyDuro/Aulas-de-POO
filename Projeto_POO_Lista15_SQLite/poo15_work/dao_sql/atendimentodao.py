from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = '''INSERT INTO atendimento
                     (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            params = (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_queixa_principal(),
                      obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(),
                      obj.get_id_horario(), obj.get_total(), obj.get_pago())
            self.execute(sql, params)
            obj.set_id(self.conn.execute('SELECT last_insert_rowid()').fetchone()[0])
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            rows = self.execute('''SELECT id, data, queixa_principal, historico_saude, avaliacao,
                                   prescricao, id_horario, total, pago FROM atendimento''').fetchall()
            return [self._objeto(row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            row = self.execute('''SELECT id, data, queixa_principal, historico_saude, avaliacao,
                                  prescricao, id_horario, total, pago FROM atendimento WHERE id = ?''', (id,)).fetchone()
            return self._objeto(row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = '''UPDATE atendimento SET data = ?, queixa_principal = ?, historico_saude = ?,
                     avaliacao = ?, prescricao = ?, id_horario = ?, total = ?, pago = ? WHERE id = ?'''
            params = (obj.get_data().strftime('%d/%m/%Y %H:%M'), obj.get_queixa_principal(),
                      obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(),
                      obj.get_id_horario(), obj.get_total(), obj.get_pago(), obj.get_id())
            self.execute(sql, params)
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            self.execute('DELETE FROM atendimento WHERE id = ?', (id,))
        finally:
            self.fechar()

    def _objeto(self, row):
        id, data, queixa, historico, avaliacao, prescricao, id_horario, total, pago = row
        obj = Atendimento(id, datetime.strptime(data, '%d/%m/%Y %H:%M'), queixa, historico, avaliacao, prescricao)
        obj.set_id_horario(id_horario)
        obj.set_total(total if total is not None else 0)
        obj.set_pago(pago)
        return obj
