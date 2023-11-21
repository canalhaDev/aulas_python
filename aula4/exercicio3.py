import math

print("me de um numero:")
numero= float(input())
if numero> 0:
    raiz= math.sqrt(numero)
    print("a raiz quadrada e:"+ str(raiz))
else:
    quadrado= math.pow(numero, 2)
    print("o numero elevado ao quadrado e :"+ str(quadrado))
    

    