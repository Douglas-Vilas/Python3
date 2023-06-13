'''
    ----------------------------------------------------------------------
        Objetivo desse desafio é: Fazer um algoritimo que leia o preço 
        de um produto e mostre seu novo preço, com 5% de desconto.
    ----------------------------------------------------------------------
'''

# Exibe o nome da loja e coleta o nome do cliente
print('Lojas DVS Sport')
cliente = input('Olá! Por favor, digite o seu nome: ')
print('Seja bem-vindo à Loja DVS Sport, {}!'.format(cliente))
print('No dia de hoje, alguns produtos estão em promoção. Segue o catálago de promoções:')

# Lista dos produtos
produto_promocao = ["Camisa", "Tênis", "Calça", "Short"]


# Mostrar opções de produtos numeradas
for i in range(len(produto_promocao)):
    print("{}. {}".format(i+1, produto_promocao[i]))


# Solicita ao cliente que faça uma escolha
escolha = int(input('Digite o número do produto desejado: '))


# Verifica se a escolha é válida
if escolha < 1 or escolha > len(produto_promocao):
    print('Opção inválida. Por favork escolha um número da lista.')
else:
    # Obter o produto escolhido pelo cliente
    produto_escolhido = produto_promocao[escolha-1]


# Exibir o produto escolhido
print('Você escolheu: {}.'.format(produto_escolhido))
print('O produto escolhido, está com 5% de desconto. Qual é o preço que você está pagando?')


# Inserindo o desconto de 5% no produto escolhido
preco = float(input('Digite o preço do produto: '))
desconto_percentual = 5
desconto = preco * (desconto_percentual / 100)  # Cálculo do valor do desconto
novo_preco = preco - desconto  # Cálculo do valor com desconto


# Exibir o novo preço do produto após o desconto de 5%
print('Você pagará pelo(a) {}, R$ {:.2f}.'.format(produto_escolhido, novo_preco))
