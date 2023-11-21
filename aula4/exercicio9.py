print("me de um valor do salario")
salario= int(input())
print("me de um valor da prestacao")
prestacao= int(input())
porcentagem= (prestacao / salario) * 100
if porcentagem > 20:
    print("emprestimo nao concedido")
    print(f"a prestacao equivale a {porcentagem}% do seu salario")
else:
    print("emprestimo concedido")
    print(f"a prestacao equivale a {porcentagem}% do seu salario")
