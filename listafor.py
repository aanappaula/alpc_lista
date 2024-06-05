# 1
count = 0
for i in range(3, 334, 3):
    count += i
print(count)

# 2
count = 0
for i in range(1, 11):
    count += i
media = count/10
print(media)

# 3
numero = int(input("Informe um número:"))
for i in range(1, numero + 1):
    for j in range(1, 11):
        print(i, "X", j, "=", j * numero)

# 4
salarios = []
for i in range(10):
    salario = float(input("Digite o salário:"))
    salarios.append(salario)
    
maior_salario = max(salarios)
soma_salarios = sum(salarios)
media_salarios = soma_salarios / len(salarios)
menor_salario = min(salarios)

print("Maior salário: R$", maior_salario)
print("Salário médio: R$", media_salarios)
print("Menor salário: R$", menor_salario)

# 5
numero = int(input("Informe um número:"))
for i in range(2, numero + 1):
    if numero == 2:
        print("Esse é um número especifico primo")
    elif numero % i == 0:
        print("não é primo")
    else:
        print("primo")
    break