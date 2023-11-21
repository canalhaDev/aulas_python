print("me de um numero")
numero1= int(input())
print("me de outro numero")
numero2= int(input())
print("o que vocçê deseja fazer com os numeros:")
print("\n (1) para somar")
print("\n (2) para subtrair")
print("\n (3) para multiplicar")
print("\n (4) para dividir")
acao=int(input())

if acao == 1:
    print("a soma dos dois numeros e"+str(numero1+numero2))
elif acao == 2:
    print("a subtracao dos dois numeros e"+str(numero1-numero2))
elif acao == 3:
    print("a multiplicacao dos dois numeros e"+str(numero1*numero2))
elif acao == 4:
    print("a divisao dos dois numeros e"+str(numero1/numero2))




