from dao_sql.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = 'INSERT INTO profissional (nome, email, especialidade, senha) VALUES (?, ?, ?, ?)'
            self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()))
            obj.set_id(self.conn.execute('SELECT last_insert_rowid()').fetchone()[0])
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            rows = self.execute('SELECT id, nome, email, especialidade, senha FROM profissional').fetchall()
            return [Profissional(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            row = self.execute('SELECT id, nome, email, especialidade, senha FROM profissional WHERE id = ?', (id,)).fetchone()
            return Profissional(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = 'UPDATE profissional SET nome = ?, email = ?, especialidade = ?, senha = ? WHERE id = ?'
            self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha(), obj.get_id()))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            self.execute('DELETE FROM profissional WHERE id = ?', (id,))
        finally:
            self.fechar()
