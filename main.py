from agenda.contato import Contato
from agenda.agenda import Agenda


def menu(agenda):
    while True:
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Contatos")
        print("5. Limpar Agenda")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        elif escolha == "2":
            nome = input("Nome do contato a remover: ")
            agenda.remover_contato(nome)
        elif escolha == "3":
            nome = input("Nome do contato a buscar: ")
            agenda.buscar_contato(nome)
        elif escolha == "4":
            agenda.listar_contatos()
        elif escolha == "5":
            confirma = input("Tem certeza que deseja limpar a agenda? (s/n): ")
            if confirma.lower() == "s":
                agenda.limpar_agenda()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    agenda = Agenda()
    menu(agenda)
