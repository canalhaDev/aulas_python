print("me de uma nota")
nota1= int(input())
print("me de outra nota")
nota2= int(input())
if nota1<0 or nota1>10:
    print("a nota 1 e invalida")
    raise Exception("ocorreu um erro")
elif nota2<0 or nota2>10:
    print("a nota 2 e invalida")
    raise Exception("ocorreu um erro")
media= (nota1 + nota2)/2
print("a media das notas e:"+str(media))



