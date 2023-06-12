''' O objetivo desse dasafio é: Fazer um programa que leia a largura e a altura de uma parede em metros, calcular a 
    sua  área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''

# Calcular a área da parede
def area_parede(altura, largura):
     area = altura * largura
     return area

# Calcular a quantidade de tinta necessária
def quantidade_tinta(area):
     quant_total = area / 2
     return quant_total

# Exibir informações para o usuário
def informcao_para_usuario(area, quant_total):
    print('A parede tem {}m². '.format(area))
    print('A quantidade de tinta a ser usada, será: {} litros'.format(quant_total))    
    
# Ler a Altura e a Largura da parede em Metros
alturaParede = float(input('Digite a altura da parede: '))
larguraParede = float(input('Digite a largura da parede: '))

# Calcular a área da parede
area = area_parede(alturaParede, larguraParede)

# Calcular a quantidade de tinta necessária
quantidade = quantidade_tinta(area)

# Exibir as informações para o usuário
informcao_para_usuario(area, quantidade)
