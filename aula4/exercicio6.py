print("me de um numero")
numero1= int(input())
print("me de outro numero")
numero2= int(input())

if numero1> numero2:
    print("numero 1 e maior que numero 2")
    diferença= numero1 - numero2
    
elif numero1< numero2:
    print("numero 1 e menor que numero 2")
    diferença= numero2 - numero1
else:
    print("os numeros sao iguais") 
    
print("a diferenca entre os numeros e :"+str(diferença))
