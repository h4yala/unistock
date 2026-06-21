def cadastrar_item(estoque):

    while True:

        codigo = input("\nCódigo do item: ").strip()

        if codigo == "":
            print("\nO código não pode estar vazio.")
            continue
        
        if codigo.isdigit() == 0:
            print("\nO código não pode ser zero.")
            continue


        if codigo in estoque:
            print("\nCódigo já cadastrado.")
            continue

        break

    while True:

        nome = input("Nome do item: ").strip()

        if nome == "":
            print("\nO nome não pode estar vazio.")
            continue

        break

    estoque[codigo] = {
        "nome": nome,
        "quantidade": 0
    }

    print("\nItem cadastrado com sucesso.")

    input("\nPressione ENTER para voltar ao menu...")