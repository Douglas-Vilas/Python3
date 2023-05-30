# Objetivo desse desafio é ler um número e mostrar o seu dobro, triplo e a raiz quadrada. 


import math

# Desenvolvimento do Código
usuário = int(input('Digite um número: '))
dobro = usuário * 2
triplo = usuário * 3
raizQuadrada = math.isqrt(usuário) # ou int(usuário ** (1/2))

# Resultado do Código
print('O número digitado foi {}.'.format(usuário), end=' ')
print('O dobro desse número é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(dobro, triplo, raizQuadrada))