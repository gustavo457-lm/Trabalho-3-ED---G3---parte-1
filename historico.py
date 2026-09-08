#imprimi traços para separar uma parte do programa de outro, com o objetivo de ter melhor visbilidade para o usúario
def separaTexto():
    print("-"*40)

#imprimi as opções do menu principal
def menuPrincipal():
    separaTexto()
    print(f"{'NAVEGADOR WEB':^40}")
    separaTexto()
    print("1. Visitar novo site")
    print("2. Navegar no histórico de visitação")
    print("3. Imprimir histórico de navegação")
    print("4. Sair")

#imprimi as opções do menu da navegação do histórico de visitação de sites
def menuHistorico():
    print("1. Avançar")
    print("2. Voltar")
    print("3. Sair do histórico de visitação")

#navega no histórico de visitação de sites
def navegar(hist):
    index = len(hist) - 1
    while True:
        print(f"SITE ATUAL: {hist[index]}")
        separaTexto()
        menuHistorico()
        opcao = int(input("Escolha: "))
        separaTexto()
        if opcao == 1:
            index += 1

        elif opcao == 2:
            index -= 1

        elif opcao == 3:
            return
        
        else:
            print("Digite um dígito válido")

        if index >= len(hist):
            print("Não é possível avançar mais!")
            index -= 1

        if index < 0:
            print("Não é possível voltar mais!")
            index += 1

#função principal
def main():

    #array para guardar histórico de visitas de sites
    historico = []
    
    while True:
        #try/except foram usados para tratar entradas de valores inválidos
        try:
            menuPrincipal()
            opcao = int(input("Escolha: "))
            separaTexto()

            if opcao == 1:
                historico.append(input("Digite a URL do site: "))
            elif opcao == 2:
                if len(historico) == 0:
                    print("Histórico vazio")
                else:
                    navegar(historico)
            elif opcao == 3:
                print(f"{'Histórico':^40}")
                separaTexto()
                if len(historico) == 0:
                    print("Histórico vazio")
                else:
                    print(f"{'Lista de sites visitados:'}")
                    print("")
                    for i in range(len(historico)-1, -1, -1):
                        print(f" - {historico[i]}")
            elif opcao == 4:
                print("Você saiu do navegador")
                separaTexto()
                break
            else:
                print("Digite uma opção válida!")
        except ValueError:
            print("Valor inválido")

main()
