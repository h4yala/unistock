from datetime import datetime

# ------------------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------------------

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

    while True:

        if opcao == "1": # mostrar todos os itens cadastrados no sistema

            print()

            for codigo, item in estoque.items():
                print(
                    f"{codigo} - {item['nome']} | Estoque: {item['quantidade']}"
                )

            codigo = input("\nInforme o código do item: ").strip()


        elif opcao == "2": # buscar pelo codigo de cadastro do item

            codigo = input("\nInforme o código: ").strip()


        if codigo not in estoque: # verificação do codigo

            if item_nao_encontrado():
                continue

            return

        break


    while True:

        quantidade = input("\nQuantidade recebida: ").strip() # movimentar o estoque após as validações adicionando a quantidade

        if not quantidade.isdigit():
            print("\nInforme apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade < 1:
            print("\nQuantidade mínima: 1.")
            continue

        break


    while True:

        data = input("Data da entrada (DD/MM/AAAA): ").strip() # formatar data de entrada para facilitar no registro e futuras melhorias

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
    estoque[codigo]["movimentacoes"].append( # necessário para adicionar cada movimentação no historico do item
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

# ------------------------------------------------------------------------------------------------------------

def saida_item(estoque): # função para dar saída nos itens

    if not estoque:
        print("\nNenhum item cadastrado.")

        input("\nPressione ENTER para voltar ao menu...")
        return


    while True:

        print("\n===== SAÍDA =====")
        print("[1] - Listar itens")
        print("[2] - Buscar por código")

        opcao = input("\nSelecione: ").strip() # mecanismo de busca, igual da entrada

        if opcao not in ["1", "2"]:
            print("\nOpção inválida.")
            continue

        break

    while True:

        if opcao == "1": # listagem do estoque

            print()

            for codigo, item in estoque.items():
                print(
                    f"{codigo} - {item['nome']} | Estoque: {item['quantidade']}"
                )

            codigo = input("\nInforme o código do item: ").strip()


        else:

            codigo = input("\nInforme o código: ").strip()


        if codigo not in estoque: # verificação do codigo

            if item_nao_encontrado():
                continue

            return

        break

    while True:

        quantidade = input("\nQuantidade retirada: ").strip() # movimentação de saída do estoque com validações

        if not quantidade.isdigit():
            print("\nInforme apenas números.") 
            continue

        quantidade = int(quantidade)

        if quantidade < 1:
            print("\nQuantidade mínima: 1.")
            continue


        if quantidade > estoque[codigo]["quantidade"]:
            print("\nQuantidade indisponível.")
            continue


        break


    while True:

        data = input("Data da saída (DD/MM/AAAA): ").strip() # validação da data para histórico

        if data == "":
            print("\nData obrigatória.")
            continue

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break

        except ValueError:
            print("\nData inválida.")


    while True:

        responsavel = input("Responsável: ").strip() # armazenamento das informações do responsável, opção livre para colocar nome ou setor
        if responsavel == "":
            print("\nInforme o responsável.")
            continue

        break


    estoque[codigo]["quantidade"] -= quantidade


    estoque[codigo]["movimentacoes"].append( # registrar a movimentação das saidas do item
        {
            "tipo": "saida",
            "quantidade": quantidade,
            "data": data,
            "responsavel": responsavel
        }
    )


    print("\nSaída registrada com sucesso.")
    print(f"Estoque atual: {estoque[codigo]['quantidade']}")


    if estoque[codigo]["quantidade"] == 0:
        print("\nAviso: estoque zerado.")


    input("\nPressione ENTER para voltar ao menu...")

# ------------------------------------------------------------------------------------------------------------

def consultar_historico(estoque): # mostrar todo o historico do item 

    if not estoque:
        print("\nNenhum item cadastrado.")

        input("\nPressione ENTER para voltar ao menu...")
        return


    while True:

        print("\n===== HISTÓRICO =====")
        print("[1] - Listar itens")
        print("[2] - Buscar por código")

        opcao = input("\nSelecione: ").strip()

        if opcao not in ["1", "2"]:
            print("\nOpção inválida.")
            continue

        break


    while True: # listagem dos itens em estoque

        if opcao == "1":

            print()

            for codigo, item in estoque.items():

                print(
                    f"{codigo} - {item['nome']}"
                )

            codigo = input(
                "\nInforme o código: "
            ).strip()


        else:

            codigo = input(
                "\nInforme o código: "
            ).strip()


        if codigo not in estoque: # verificação do codigo

            if item_nao_encontrado():
                continue

            return

        break


    historico = estoque[codigo]["movimentacoes"]


    if not historico:

        print("\nNenhuma movimentação registrada.")

        input("\nPressione ENTER para voltar ao menu...")
        return


    print(
        f"\n===== HISTÓRICO - {estoque[codigo]['nome']} ====="
    )


    for movimento in historico: # impressão da movimentação do item no estoque 

        print(
            f"\n{movimento['tipo'].upper()}"
        )

        print(
            f"Quantidade: {movimento['quantidade']}"
        )

        print(
            f"Data: {movimento['data']}"
        )


        if movimento["responsavel"]:

            print(
                f"Responsável: {movimento['responsavel']}"
            )
        
        print("------------------------------")


    input("\nPressione ENTER para voltar ao menu...")

# ------------------------------------------------------------------------------------------------------------

def item_nao_encontrado(): # função para facilitar a busca dos itens no estoque

    while True:

        print("\nItem não encontrado.")
        print("[1] - Pesquisar novamente")
        print("[2] - Voltar")

        opcao = input("\nSelecione: ").strip()

        if opcao == "1":
            return True

        if opcao == "2":
            return False

        print("\nOpção inválida.")

# ------------------------------------------------------------------------------------------------------------
