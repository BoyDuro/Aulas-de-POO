from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = 'INSERT INTO cliente (nome, email, fone, senha) VALUES (?, ?, ?, ?)'
            self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
            obj.set_id(self.conn.execute('SELECT last_insert_rowid()').fetchone()[0])
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            rows = self.execute('SELECT id, nome, email, fone, senha FROM cliente').fetchall()
            return [Cliente(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            row = self.execute('SELECT id, nome, email, fone, senha FROM cliente WHERE id = ?', (id,)).fetchone()
            return Cliente(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = 'UPDATE cliente SET nome = ?, email = ?, fone = ?, senha = ? WHERE id = ?'
            self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            self.execute('DELETE FROM cliente WHERE id = ?', (id,))
        finally:
            self.fechar()
