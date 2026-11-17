from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = '''INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
                     VALUES (?, ?, ?, ?, ?)'''
            params = (obj.get_data().strftime('%d/%m/%Y %H:%M'), int(obj.get_confirmado()),
                      obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional())
            self.execute(sql, params)
            obj.set_id(self.conn.execute('SELECT last_insert_rowid()').fetchone()[0])
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            rows = self.execute('SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario').fetchall()
            objetos = []
            for id, data, confirmado, id_cliente, id_servico, id_profissional in rows:
                obj = Horario(id, datetime.strptime(data, '%d/%m/%Y %H:%M'))
                obj.set_confirmado(bool(confirmado))
                obj.set_id_cliente(id_cliente)
                obj.set_id_servico(id_servico)
                obj.set_id_profissional(id_profissional)
                objetos.append(obj)
            return objetos
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            row = self.execute('SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario WHERE id = ?', (id,)).fetchone()
            if row is None:
                return None
            id, data, confirmado, id_cliente, id_servico, id_profissional = row
            obj = Horario(id, datetime.strptime(data, '%d/%m/%Y %H:%M'))
            obj.set_confirmado(bool(confirmado))
            obj.set_id_cliente(id_cliente)
            obj.set_id_servico(id_servico)
            obj.set_id_profissional(id_profissional)
            return obj
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = '''UPDATE horario SET data = ?, confirmado = ?, id_cliente = ?,
                     id_servico = ?, id_profissional = ? WHERE id = ?'''
            params = (obj.get_data().strftime('%d/%m/%Y %H:%M'), int(obj.get_confirmado()),
                      obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id())
            self.execute(sql, params)
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            self.execute('DELETE FROM horario WHERE id = ?', (id,))
        finally:
            self.fechar()
