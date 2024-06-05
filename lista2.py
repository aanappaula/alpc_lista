salBase = float(input('informe salário'))
grat = salBase*5/100
Imp = salBase*7/100
SalReceber = (salBase + grat)-Imp

print(SalReceber)

#3

raio = float(input('informe o raio '))
altura = float(input('informe a altura '))
areaBase = ((2 * 3.14) * (raio**2))
areaLateral = (((2 * 3.14) * raio) * altura)
areaTotal = (areaBase + areaLateral) / 3
galoes = areaTotal / 3.6  
totalPagar = galoes * 40

print(round(totalPagar,2),(round(galoes,2)))

#5

usuario = input(' Informe o seu usuario: ')
senha =  input(' Informe a sua senha: ') 
senhaOculta = ''

for e in senha:
  senhaOculta += '*'

print(senhaOculta)
print(usuario)

# 6

valor = float(input('Digite um valor: '))
porcentagem = valor * 0.05
resultado = valor + porcentagem
print(resultado)

tempo = float(input('informe o tempo gasto na viagem: '))
velocidade = float(input('informe a velocidade média: '))
distancia = tempo * velocidade
litros = distancia / 12
print(tempo)
print(distancia)
print(litros)


hora = int(input('informe a hora: '))
minuto = int(input('informe o minuto: '))
segundo = int(input('informe o segundo: '))
segundos = (hora * 3600) + (minuto * 60) + segundo
print(segundos)

preco = 9.99
print(round(numero,2))

numero1 = int(input('Informe o número 1:'))
numero2 = int(input('Informe o número 2:'))

if numero1 < numero2:
    print(numero1)
else:
    print(numero2)
    
