print("me de uma idade")
idade=int(input())
print("me de um tempo de serviço")
tempserv=int(input())

if idade >= 65:
    print("pode se aposentar")

elif tempserv >= 30:
    print("pode se aposentar")

elif idade >= 60 and tempserv >= 30:
    print("pode se aposentar")

else:
    print("aposentadoria indisponivel")


# if idade >= 65 or tempserv >=30 or (idade >= 60 and tempserv >=25:)