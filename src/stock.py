from datetime import datetime

def cadastrar_item(estoque): # função de cadastro do item

    while True:

        codigo = input("\nCódigo do item: ").strip() # remover espaços e caracteres 1° validação

        if codigo == "":
            print("\nO código não pode estar vazio.") # validações de código
            continue
        
        if not codigo.isdigit():
            print("\nInforme apenas números.")
            continue

        if int(codigo) == 0:
            print("\nO código não pode ser zero.")
            continue


        if codigo in estoque:
            print("\nCódigo já cadastrado.")
            continue

        break

    while True:

        nome = input("Nome do item: ").strip()

        if nome == "":
            print("\nO nome não pode estar vazio.") # validações de nome
            continue

        if len(nome) < 2:
            print("\nInforme um nome válido.")
            continue

        break

    estoque[codigo] = { # o estoque do produto cadastrado inicia zerado
        "nome": nome,
        "quantidade": 0,
        "movimentacoes": []
    }

    print("\nItem cadastrado com sucesso.")

    input("\nPressione ENTER para voltar ao menu...")

def entrada_item(estoque): # função para dar entrada nos itens 

    if not estoque:
        print("\nNenhum item cadastrado.")

        input("\nPressione ENTER para voltar ao menu...")
        return


    while True:

        print("\n===== ENTRADA =====")
        print("[1] - Listar itens")
        print("[2] - Buscar por código")

        opcao = input("\nSelecione: ").strip()

        if opcao not in ["1", "2"]:
            print("\nOpção inválida.")
            continue

        break


    if opcao == "1": # mostrar todos os itens cadastrados no sistema

        print()

        for codigo, item in estoque.items():
            print(
                f"{codigo} - {item['nome']} | Estoque: {item['quantidade']}"
            )

        codigo = input("\nInforme o código do item: ").strip()


    elif opcao == "2": # buscar pelo codigo de cadastro do item

        codigo = input("\nInforme o código: ").strip()


    if codigo not in estoque:
        print("\nItem não encontrado.")

        input("\nPressione ENTER para voltar ao menu...")
        return


    while True:

        quantidade = input("\nQuantidade recebida: ").strip()

        if not quantidade.isdigit():
            print("\nInforme apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade < 1:
            print("\nQuantidade mínima: 1.")
            continue

        break


    while True:

        data = input("Data da entrada (DD/MM/AAAA): ").strip()

        if data == "":
            print("\nData obrigatória.")
            continue

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break

        except ValueError:
            print("\nData inválida.")
            continue


    estoque[codigo]["quantidade"] += quantidade
    estoque[codigo]["movimentacoes"].append(
        {
            "tipo": "entrada",
            "quantidade": quantidade,
            "data": data,
            "responsavel": None
        }
     )

    print("\nMovimentação registrada com sucesso.")

    print("\nEntrada registrada com sucesso.")
    print(
        f"Estoque atual: {estoque[codigo]['quantidade']}"
    )

    input("\nPressione ENTER para voltar ao menu...")

