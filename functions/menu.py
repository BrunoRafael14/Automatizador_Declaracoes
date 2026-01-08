from .declaracoes import declaracao_foro, declaracao_laudemio, declaracao_dominio_direto

def menu():
    while True:
        print("\n" + "=" * 20 + " AUTOMATIZADOR DE DECLARAÇÕES " + "=" * 20)
        print("\nEscolha uma opção:")
        print("1. Declaração de Foro")
        print("2. Laudêmio")
        print("3. Domínio Direto")
        print("4. Sair")
        print("=" * 50)
        
        opcao = int(input("\nDigite a opção desejada (1-4): "))
        
        if opcao == 1:
            declaracao_foro()
        elif opcao == 2:
            declaracao_laudemio()
        elif opcao == 3:
            declaracao_dominio_direto()
        elif opcao == 4:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        