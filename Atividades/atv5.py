num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")

print("Média aritmética:", media)