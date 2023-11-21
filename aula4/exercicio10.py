print("me de uma altura")
altura= float(input())
print("me de um sexo (M)para masculino e (F) para feminino")
sexo=input()
if sexo== "M":
    peso_ideal= (72.7 * altura) - 58
    print(f"o seu peso ideal e: {peso_ideal}")
elif sexo== "F":
    peso_ideal= (62.1 * altura) - 44.7
    print(f"o seu peso ideal e: {peso_ideal}")
else:
    print("opcao invalida")