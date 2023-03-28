'''
Execução do checkpoint 1 do primeiro semestre no qual temos que realizar um sistema de soma de 2 números de 0 a 99, ao passo que precisamos substituir o número 7 pelo número 0 toda vez que ele apareça na tela, seja no número inserido no input ou no resultado.

Feito por Rodrigo Viana, Caique Chagas e Rafael Autieri
'''
print('Realizando uma soma que exclui o numero 7 sempre que aparece:')
#Definindo as variáveis
num1 = int(input('Digite um numero de 0 a 99: '))
num2 = int(input('Digite outro numero de 0 a 99 para realizarmos a soma: '))

#extraindo cada algarismo de cada número para depois verificar qual tem 7
alga1num1 = num1%10
alga2num1 = num1//10

alga1num2 = num2%10
alga2num2 = num2//10


#verificando se há 7 no primeiro algarismo do primeiro número
if alga1num1%7 == 0:
    alga1num1 = 0
else:
    alga1num1 = alga1num1

#verificando se há 7 no segundo algarismo do primeiro número
if alga2num1%7 == 0:
    alga2num1 = 0
else:
    alga2num1 = alga2num1

#verificando se há 7 no primeiro algarismo do segundo número
if alga1num2%7 == 0:
    alga1num2 = 0
else:
    alga1num2 = alga1num2

#verificando se há 7 no segundo algarismo do segundo número
if alga2num2%7 == 0:
    alga2num2 = 0
else:
    alga2num2 = alga2num2

#juntando os algarismos para formar os números novamente já modificados, se necessário
num1 = (alga2num1 *10 + alga1num1)
num2 = (alga2num2*10 + alga1num2)

#somando os números
soma = num1 + num2

#extraindo o terceiro número da soma, se houver
alga3soma = soma//100

#extraindo o segundo número da soma
if soma >= 100:
    alga2soma = (soma//10)%10
else:
    alga2soma = soma//10

#extraindo o primeiro número da soma
alga1soma = soma%10

#extraindo o número 7 dos algarismos, caso haja:
#primeiro algarismo
if alga1soma%7 == 0:
    alga1soma = 0
else:
    alga1soma = alga1soma

#segundo algarismo
if alga2soma%7 == 0:
    alga2soma = 0
else:
    alga2soma = alga2soma

#terceiro algarismo
if alga3soma%7 == 0:
    alga3soma = 0
else:
    alga3soma = alga3soma

alga2soma = alga2soma*10
alga3soma = alga3soma*100

soma = alga1soma + alga2soma + alga3soma

print(soma)