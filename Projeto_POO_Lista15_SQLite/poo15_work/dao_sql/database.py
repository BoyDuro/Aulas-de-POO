import sqlite3

class Database:
    nome_bd = 'agenda.bd'

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute('PRAGMA foreign_keys = ON')

    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @classmethod
    def criar_tabelas(cls):
        cls.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            )
        ''')
        cls.execute('''
            CREATE TABLE IF NOT EXISTS profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especialidade TEXT,
                senha TEXT NOT NULL
            )
        ''')
        cls.execute('''
            CREATE TABLE IF NOT EXISTS servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
            )
        ''')
        cls.execute('''
            CREATE TABLE IF NOT EXISTS horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                confirmado INTEGER DEFAULT 0,
                id_cliente INTEGER,
                id_servico INTEGER,
                id_profissional INTEGER,
                FOREIGN KEY (id_cliente) REFERENCES cliente(id),
                FOREIGN KEY (id_servico) REFERENCES servico(id),
                FOREIGN KEY (id_profissional) REFERENCES profissional(id)
            )
        ''')
        cls.execute('''
            CREATE TABLE IF NOT EXISTS atendimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                queixa_principal TEXT,
                historico_saude TEXT,
                avaliacao TEXT,
                prescricao TEXT,
                id_horario INTEGER,
                total REAL DEFAULT 0,
                pago INTEGER,
                FOREIGN KEY (id_horario) REFERENCES horario(id)
            )
        ''')
        # Mantém compatibilidade com bancos criados pela versão inicial da aula.
        colunas = [linha[1] for linha in cls.execute('PRAGMA table_info(atendimento)').fetchall()]
        if 'total' not in colunas:
            cls.execute('ALTER TABLE atendimento ADD COLUMN total REAL DEFAULT 0')
        if 'pago' not in colunas:
            cls.execute('ALTER TABLE atendimento ADD COLUMN pago INTEGER')

    @classmethod
    def inicializar(cls):
        cls.abrir()
        try:
            cls.criar_tabelas()
        finally:
            cls.fechar()

if __name__ == '__main__':
    Database.inicializar()
