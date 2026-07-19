import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def menu():

    limpar()

    print("=" * 55)
    print("         🚗 SISTEMA DE ESTACIONAMENTO 🚗")
    print("=" * 55)
    print()
    print(" [1] Cadastrar veículo")
    print(" [2] Remover veículo")
    print(" [3] Editar veículo")
    print(" [4] Procurar veículo")
    print(" [5] Listar veículos")
    print(" [6] Mostrar vagas")
    print()
    print(" -------- Relatórios --------")
    print(" [7] Exportar CSV")
    print(" [8] Criar relatório")
    print(" [9] Enviar relatório por e-mail")
    print()
    print(" [0] Sair")
    print()
    print("=" * 55)

    return input("Escolha uma opção: ")