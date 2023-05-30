# Esse desafio, tem como objetivo mostrar o número antecessor e sucessor de um outro número, escolhido pelo usuário.

#Desenvolvimento do Código
usuário = int(input('Digite um número '))
antecessor = usuário - 1
sucessor = usuário + 1

# Mostrará o resultado do código.
print('O número digitado é {}.'.format(usuário), end=" ")
print('O antecessor do número digitado é {}, e o seu sucessor é o número {}.'.format(antecessor, sucessor))