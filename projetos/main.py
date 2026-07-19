from estacionamento import Estacionamento
from menu import menu

estacionamento = Estacionamento()

while True:

    opcao = menu()

    if opcao == "1":
        estacionamento.inserir_veiculo()

    elif opcao == "2":
        estacionamento.remover_veiculo()

    elif opcao == "3":
        estacionamento.editar_veiculo()

    elif opcao == "4":
        estacionamento.procurar_veiculo()

    elif opcao == "5":
        estacionamento.listar_veiculos()

    elif opcao == "6":
        estacionamento.mostrar_estacionamento()

    elif opcao == "7":
        estacionamento.exportar_csv()

    elif opcao == "8":
        estacionamento.filtrar_csv()

    elif opcao == "9":
        estacionamento.enviar_email()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")

    input("\nPressione ENTER para continuar...")