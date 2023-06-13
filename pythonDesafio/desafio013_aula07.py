'''
    -----------------------------------------------------------------
        O objetivo deste desafio é fazer um algoritimo que leia o
        salário de um funcionário e mostre seu novo salário, com 
        15% de aumento.
    -----------------------------------------------------------------
'''

# Solicitar o salário do funcionário
salario = float(input('Qual é o seu salário: '))

# Cálcuolo do aumento de 15% 
percentual_aumento = 15
aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

# Exibir o novo salário formatado
print('O seu novo salário é R$ {:.2f}'.format(novo_salario))

