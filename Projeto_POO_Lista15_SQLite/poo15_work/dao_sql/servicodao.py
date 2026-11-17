from dao_sql.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            self.execute('INSERT INTO servico (descricao, valor) VALUES (?, ?)', (obj.get_descricao(), obj.get_valor()))
            obj.set_id(self.conn.execute('SELECT last_insert_rowid()').fetchone()[0])
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            rows = self.execute('SELECT id, descricao, valor FROM servico').fetchall()
            return [Servico(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            row = self.execute('SELECT id, descricao, valor FROM servico WHERE id = ?', (id,)).fetchone()
            return Servico(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = 'UPDATE servico SET descricao = ?, valor = ? WHERE id = ?'
            self.execute(sql, (obj.get_descricao(), obj.get_valor(), obj.get_id()))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            self.execute('DELETE FROM servico WHERE id = ?', (id,))
        finally:
            self.fechar()
