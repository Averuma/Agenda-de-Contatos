from agenda.db import DBManager
from agenda.contato import Contato


class Agenda:
    def __init__(self):
        self.db = DBManager()

    def adicionar_contato(self, contato):
        self.db.adicionar_contato(contato)
        print("Contato adicionado com sucesso!")

    def remover_contato(self, nome):
        self.db.remover_contato(nome)

    def buscar_contato(self, nome):
        self.db.buscar_contato(nome)

    def listar_contatos(self):
        self.db.listar_contatos()

    def limpar_agenda(self):
        self.db.limpar_agenda()
