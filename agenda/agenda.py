from .contato import Contato


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print("Contato removido com sucesso!")
                return
        print("Contato não encontrado.")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(contato)
                return
        print("Contato não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in self.contatos:
                print(contato)
