# O objetivo desse desafio é: Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Realizar o cálculo da média, com as notas fornecidas pelo usuário.
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Verificar o resultado e mostrar as informações na tela ao usuário.
def exibir_resultado(nota1, nota2, resultado, media):
    if media >= 7:
        print('Aluno Aprovado!')
    else:
        print('Aluno Reprovado')
    
    print('A nota do 1º Bimestre é {} e a nota do 2º Bimestre é {}.'.format(nota1, nota2))
    print('A soma das notas do 1º e 2º Bimestre é {}.'.format(resultado))
    print('A média do aluno é {}.'.format(media))

# Colher as informações do usuário.
nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))

# Fazer o cálculo da média.
resultado = nota1 + nota2
media = calcular_media(nota1, nota2)

# Mostrar o resultado do cálculo ao usuário.
exibir_resultado(nota1, nota2, resultado, media)
