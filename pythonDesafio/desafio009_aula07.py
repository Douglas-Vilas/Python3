# O objetivo desse desafio é: Fazer um programa que leia seu número inteiro qualquer e mostre na tela a sua tabuada.

# Obtém um número inteiro digitado pelo usuário
numInt = int(input('Digite um número Inteiro: '))

# Calcula e exibe a tabuada do número
for i in range(1, 11):
    resultado = numInt * i
    print(f'{numInt} x {i} = {resultado}')
