# #Aluna: Ana Paula de Souza - BES - Turma C
# # 1
# #entrada: mensagem
# #processamento: ler mensagem
# #saída: mostrar a mensagem
mensagem = "Hello World",
print(mensagem)

# #2
# #entrada: recebe o numero
# #processamento: ler o numero 
# #saída: mostrar o numero
numero = input("Digite seu numero: ")
print (numero)

# #3
# #entrada: recebe dois numeros
# #processamento: le os dois numeros e faz a soma
# #saída: mostrar a soma dos dois numeros

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
soma = numero1 + numero2
print (soma)

# #4
# #entrada: recebe as notas
# #processamento: le as notas e faz a media
# #saída: mostrar a media das notas

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
nota4 = float(input("Digite a nota 4:"))
media = (nota1 + nota2 + nota3 + nota4) / 4

# print(media)

# #5
# #entrada: recebe o valor em metros
# #processamento: le o valor em metros e converte em centimetros
# #saída: mostrar o valor em centimetros

metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
print(centimetros)

# #6
# #entrada: recebe o raio do circulo
# #processamento: le o raio do circulo e faz o calculo da area
# #saída: mostrar a area do circulo

raio = float(input("Digite o raio do circulo: "))
area = (3.14 * raio) ** 2
print(area)

# #7
# #entrada: recebe o lado do quadrado
# #processamento: le o lado do quadrado,faz o calculo da area, e do dobro da area
# #saída: dobro da area do quadrado

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print(dobro_area)

# #8
# #entrada: recebe o salario do funcionario e as horas trabalhadas
# #processa: le o salario do funcionario e as horas trabalhadas, faz o calculo do salario por mes
# #saída: mostrar o salario por mes

salario_hora = float(input("Digite o salario por hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
salario_mes = salario_hora * horas_trabalhadas

# print(salario_mes)

# #9
# #entrada: recebe a temperatura em graus fahrenheit
# #processamento: le a temperatura em graus fahreheint e faz a conversao para graus celsius
# #saída: mostrar a temperatura em graus celsius

fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(celsius)

# #10
# #entrada: recebe a temperatura em graus celsius
# #processamento: le a temperatura em graus celsius e faz a conversao para graus fahren
# #saída: mostrar a temperatura em graus fahren

temp_celsius = float(input("Digite a temperatura em graus celsius: "))
temp_fahren = (temp_celsius * 9/5) + 32
print(temp_fahren)

# #11
# #entrada: recebe o peso e a altura
# #processamento: le o peso e a altura e faz o calculo do peso ideal
# #saída: mostrar o peso ideal

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))
peso_ideal = (72.7 * altura) - 58
print (round(peso_ideal,2))

#12
#entrada: recebe o peso e a altura
#processamento: le o peso e a altura e faz o calculo do peso ideal, mudando o calculo caso seja homem ou mulher
#se for mulher : (62.1*h) - 44.7
#se for homem : (72.7*h) - 58
#saída: mostrar o peso ideal	
sexo = input("Digite seu sexo (M ou F): ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))
peso_idealM = (72.7 * altura) - 58
peso_idealF = (62.1 * altura) - 44.7

if sexo == "M":
    print (peso_idealM)
else:
  print (peso_idealF)


#13
#entrada: recebe o peso e a altura
#processamento: le o peso e a altura e faz o calculo do peso ideal,
#se for mulher : (62.1*h) - 44.7
#se for homem : (72.7*h) - 58
#saída: mostrar o peso ideal

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))
peso_ideal = (72.7 * altura) - 58
print(peso_ideal)
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))

#13
#entrada: recebe o peso do peixe
#processamento: le o peso do peixe e faz o calculo do excesso, e da multa
#saída: mostrar o excesso e a multa

peso_peixe = float(input("Digite o peso do peixe: "))
excesso = peso_peixe - 50
multa = excesso * 4
print(excesso)

#14
#entrada: recebe a area em metro a ser pintada
#processamento: recebe a area em metro a ser pintada e faz o calculo da quantidade de latas que deve ser comprada
#saída: mostrar a quantidade de latas que deve ser comprada
area = float(input("Digite a area em metros quadrados a ser pintada:"))
area_em_litros = area * 3
latas = area_em_litros / 18
valor_total = latas * 80
print(valor_total)

#15
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
# litros, que custam R$ 25,00.
# o Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# o comprar apenas latas de 18 litros;
# o comprar apenas galões de 3,6 litros;
# o misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%
# de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#entrada: recebe a area em metro a ser pintada
#processamento: recebe a area em metro a ser pintada e faz o calculo da quantidade de latas que deve ser comprada, e o calculo do preço

# area = float(input("Digite a area em metros quadrados a ser pintada:"))
