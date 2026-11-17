import sqlite3
from abc import ABC, abstractmethod
from dao_sql.database import Database

class DAO(ABC):
    nome_bd = Database.nome_bd

    def __init__(self):
        Database.inicializar()
        self.conn = None

    def abrir(self):
        self.conn = sqlite3.connect(self.nome_bd)
        self.conn.execute('PRAGMA foreign_keys = ON')

    def fechar(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def execute(self, sql, params=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, params or [])
        self.conn.commit()
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass
