import sqlite3
from agenda.contato import Contato


class DBManager:
    def __init__(self, db_file="agenda.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self._criar_tabela_contatos()

    def __del__(self):
        self.conn.close()

    def _criar_tabela_contatos(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT
            )
        """
        )
        self.conn.commit()

    def adicionar_contato(self, contato):
        self.cursor.execute(
            """
            INSERT INTO contatos (nome, telefone, email)
            VALUES (?, ?, ?)
        """,
            (contato.nome, contato.telefone, contato.email),
        )
        self.conn.commit()

    def remover_contato(self, nome):
        self.cursor.execute(
            """
            DELETE FROM contatos WHERE nome = ?
        """,
            (nome,),
        )
        if self.cursor.rowcount > 0:
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")
        self.conn.commit()

    def buscar_contato(self, nome):
        self.cursor.execute(
            """
            SELECT * FROM contatos WHERE nome = ?
        """,
            (nome,),
        )
        contato = self.cursor.fetchone()
        if contato:
            print(f"Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        self.cursor.execute(
            """
            SELECT * FROM contatos
        """
        )
        contatos = self.cursor.fetchall()
        if not contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in contatos:
                print(
                    f"Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}"
                )

    def limpar_agenda(self):
        self.cursor.execute(
            """
            DELETE FROM contatos
        """
        )
        self.conn.commit()
        print("Agenda limpa. Todos os contatos foram removidos.")
