from stock import cadastrar_item, entrada_item, saida_item, consultar_historico

def mostrar_menu():
    while True:
        print("\n===== UNISTOCK =====")
        print("[1] - Cadastrar item")
        print("[2] - Entrada")
        print("[3] - Saída")
        print("[4] - Histórico")
        print("[5] - Sair")

        opcao = input("\nSelecione uma ação: ").strip()

        if opcao in ["1", "2", "3", "4","5"]:
            return opcao

        print("\nOpção inválida. Tente novamente.")

def main():
    estoque = {}

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_item(estoque)

        elif opcao == "2":
            entrada_item(estoque)

        elif opcao == "3":
            saida_item(estoque)
        
        elif opcao == "4":
            consultar_historico(estoque)

        elif opcao == "5":
            print("\nEncerrando sistema...")
            break

main()