while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print()
    escolha = int(input("Digite o número da operação desejada: "))
    result = 0
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        result = n1 + n2
        print("O resultado é: ", result)
    elif escolha == 2:
        result = n1 - n2
        print("O resultado é: ", result)
    elif escolha == 3:
        if n2 != 0:
            result = n1 / n2
            print("O resultado é: ", result)
        else:
            print("Não é possível realizar uma divisão por 0")  
    elif escolha == 4:
        result = n1 * n2
        print("O resultado é: ", result)
    else:
        print("Opção inválida")
    resp = input("Deseja continuar (S/N)? ")
    if resp.lower() != "s" and resp.lower() != "sim":
        break
