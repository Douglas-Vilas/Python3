# Objetivo desse desafio é: Escrever um programa que leia um valor em metros e o exiba
# convertindo em centímetros e milímetros.

# Função para converter de metros em centímetros
def conversao_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

# Função para converter de metros em milímetros.
def conversao_para_milimetros(metros):
    milimetros = metros * 1000
    return milimetros

# Função para exibir os resultados
def exibir_resultado(metros, centimetros, milimetros):
    print('A metragem informada, convertida em centimetos, é {}.'.format(centimetros))
    print('A metragem informada, convertida para milímetros, é {}.'.format(milimetros))

# Colher as informações do usuário
metros = float(input('Digite a metragem desejada: '))

# Fazer os cálculo cálculos de conversão
centimetros = conversao_para_centimetros(metros)
milimetros = conversao_para_milimetros(metros)

# Exibir o resultado na tela. 
exibir_resultado(metros, centimetros, milimetros)
