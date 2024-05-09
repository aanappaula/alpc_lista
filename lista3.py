# Ler dois números inteiros e apresentar o resultado da diferença do maior pelo menor.

num1 = int(input('Informe o número 1:'))
num2 = int(input('Informe o número 2:'))

if num1 > num2:
  print(num1 - num2)
else:
  print(num2 - num1)

  
# Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um valor positivo, ou seja, o algoritmo deverá apresentar o módulo de um número fornecido.  Lembre-se de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1.
  
# Ler quatro números  referentes a quatro notas e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição.
nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Inoforme a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))
nota4 = float(input('Informe a quarta nota:'))
soma = (nota1 + nota2 + nota3 + nota4) / 4

if soma >= 5:
  print('Aprovado')
else:
  print('Reprovado')

  
# Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3.
# Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 ou 3.
# Faça um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias: 

# Construa um algoritmo que, considerando que se tenha o nome e a quantidade em estoque de quatro produtos, mostre quais produtos estão abaixo do estoque mínimo (30 unidades).

# bolacha = 30
# banana = 100
# chocolate = 10
# arroz = 4
# frutas = ['banana','pera', 'uva', 'maçã']
# if 

# Elabore um algoritmo que leia as quatro notas de  prova (P1, P2, P3 E P4) e quatro notas de trabalho (T1, T2, T3, T4) e posteriormente exiba a mensagem “aprovado” ou “não aprovado”dependendo dos valores obtidos, conforme as regras de cálculos definidas a seguir:
# Média de provas: MP = (P1 + P2 + P3 + P4)/4
# Média de trabalhos MT = (T1 + T2 + T3 + T4) / 4
# Média final MF = 0,8MP + 0,2MT

nota1 = float(input('Informe a nota 1:'))
nota2 = float(input('Informe a nota 2:'))
nota3 = float(input('Informe a nota 3:'))
nota4 = float(input('Informe a nota 4:'))

trabalho1 = float(input('Informe o trabalho 1:'))
trabalho2 = float(input('Informe o trabalho 2:'))
trabalho3 = float(input('Informe o trabalho 3:'))
trabalho4 = float(input('Informe o trabalho 4:'))

mediaP = (nota1 + nota2 + nota3 + nota4) / 4
mediaT = (trabalho1 + trabalho2 + trabalho3 + trabalho4) / 4

mediaF = (0.8 * mediaP) + (0.2 * mediaT)
print(mediaF)

#Faça um programa que leia três números e imprima o maior deles.

numero1 = float(input('Informe um número:'))
numero2 = float(input('Informe outro número:'))
numero3 = float(input('Informe outro número:'))

if numero1 > numero2 and numero1 > numero3:
  print('O número 1 é o maior')
elif numero2 > numero1 and numero2 > numero3:
  print('O número 2 é o maior')
else:
  print('O número 3 é o maior')

# Faça um programa que receba como entrada três valores e os imprima em ordem crescente.

numero1 = int(input('Informe um número:'))
numero2 = int(input('Informe outro número:'))
numero3 = int(input('Informe outro número:'))

lista = [numero1, numero2, numero3]
nova_lista = sorted(lista)
print(nova_lista)

# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12 unidades. Escreva um programa que leia o número de maçãs compradas, calcule e imprima o custo total da compra.

macas_compradas = int(input('Informe a quantidade de maçãs compradas:'))
if macas_compradas < 12:
  print(macas_compradas * 1.30)
else:
  print(macas_compradas * 1.00)

# Faça um programa para aprovar empréstimos bancários. O código deve pedir três informações: valor do empréstimo, número de parcelas e salário do solicitante. Aprovar empréstimo caso o valor das parcelas represente no máximo 30% do salário do solicitante.

emprestimo = float(input('Informe o valor do empréstimo:'))
parcelas = int(input('Informe o número de parcelas:'))
salario = float(input('Informe o seu salário:'))

valor_parcelas = (emprestimo / parcelas)
if valor_parcelas <= (salario * 0.3):
  print('O seu empréstimo foi aprovado!')
else:
  print('O seu empréstimo foi reprovado!')


# A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor 
# for maior que R$ 50.000,00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000,00 
# e R$ 50.000,00 (incluindo extremos) a comissão será de 9,5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa 
# onde será informado nome do corretor e o valor da venda, após isto o programa irá calcular o valor da comissão.

venda = float(input('Informe o valor da comissão:'))
comissao1 = venda + (venda * 0.12)
comissao2 = venda + (venda * 0.95) 
comissao3 = venda + (venda *0.7)


if venda > 50000:
    print(comissao1)
elif venda >= 30000 and venda <= 50000:
    print(comissao2)
else:
    print(comissao3)


# Faça um programa onde serão informados as quatro notas do aluno. O programa irá então apresentar a média, se foi aprovado 
# (nota ≥ 7) ou se ficou em exame. Caso o aluno ficou em exame, o programa irá então perguntar qual foi a nota do exame e 
# então irá calcular a nova média (média anteior com a nota do exame) e informar se ele foi aprovado (nova média ≥ 5) ou se foi reprovado.

nota1 = float(input('Informe a nota 1:'))
nota2 = float(input('Informe a nota 2:'))
nota3 = float(input('Informe a nota 3:'))
nota4 = float(input('Informe a nota 4:'))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 7:
    print("Você foi reprovado, faça exame!")
    exame = float(input('Informe a nota do seu exame '))
    mediaFinal = (media + exame) /2
    if mediaFinal >= 5:
        print("Parabéns, você foi aprovado no exame. Essa é a sua média: ", mediaFinal)
    else:
        print("Você foi reprovado no exame. Essa é a sua média: ", mediaFinal)
else:
    print("Você foi aprovado!")
    
# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar
# mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo
# de 50%. Escreva um programa que leia o número de horas trabalhadas em um mês, o salário por 
# hora e imprima o salário total do funcionário, que deverá ser acrescido das horas extras, 
# caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

horasTrabalhadas = float(input('Insira as horas trabalhadas:'))
salarioHora = float(input('Insira o sálario por hora'))