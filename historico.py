def navegar(hist):
    index = len(hist) - 1
    while True:
        print(f"SITE ATUAL: {hist[index]}")
        print("-" * 20)

        print("1. Avançar\n2. Adicionar novo site\n3. Voltar\n4. Sair\n")
        opcao = int(input("Escolha: "))

        if opcao == 1:
            index += 1
        elif opcao == 2:
            hist.append(input("Digite a URL do site: "))
            index = len(hist) - 1
        elif opcao == 3:
            index -= 1
        elif opcao == 4:
            return
        else:
            print("Digite um dígito válido")

        if index >= len(hist):
            print("Não é possível avançar mais!")
            index -= 1
        if index < 0:
            print("Não é possível voltar mais!")
            index += 1



historico = []


while True:
    print("1. Visitar novo site\n2. Ver o histórico\n3. Imprimir histórico\n4. Sair")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        historico.append(input("Digite a URL do site: "))
    elif opcao == 2:
        navegar(historico)
    elif opcao == 3:
        for i in range(len(historico)-1, -1, -1):
            print(historico[i])
    elif opcao == 4:
        break
    else:
        print("Digite uma opção válida!")



