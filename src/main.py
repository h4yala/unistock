from stock import cadastrar_item


def mostrar_menu():
    while True:
        print("\n===== UNISTOCK =====")
        print("[1] - Cadastrar item")
        print("[2] - Entrada")
        print("[3] - Saída")
        print("[4] - Sair")

        opcao = input("\nSelecione uma ação: ").strip()

        if opcao in ["1", "2", "3", "4"]:
            return opcao

        print("\nOpção inválida. Tente novamente.")


def main():
    estoque = {}

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_item(estoque)

        elif opcao == "2":
            print("\nEntrada ainda não implementada.")

        elif opcao == "3":
            print("\nSaída ainda não implementada.")

        elif opcao == "4":
            print("\nEncerrando sistema...")
            break


main()