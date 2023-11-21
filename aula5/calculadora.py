while True:
    print("Me dê dois numeros:")
    num1 = int(input())
    num2 = int(input())

    print("-="*20)
    print("Escolha qual operação deseja realizar")
    print("(1) Para soma")
    print("(2) Para subtração")
    print("(3) Para multiplicação")
    print("(4) Para divisão")
    print("(5) Para Sair")
    print("-="*20)

    opcao = int(input())

    if opcao >= 5 or opcao <= 0:
        break

    elif opcao == 1:
        print(str(num1+num2))
        continue

    elif opcao == 2:
        if num1 >= num2:
            print(str(num1-num2))

        else:
            print(str(num2-num1))

        continue

    elif opcao == 3:
        print(str(num1*num2))
        continue

    elif opcao == 4:
        if num1 >= num2:
            print(str(num1/num2))
        else:
            print(str(num2/num1))
        continue

    else:
        print("Opção inválida")
        continue