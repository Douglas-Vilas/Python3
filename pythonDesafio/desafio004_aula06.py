""" Esse programa tem como objetivo, ler algo pelo teclado
    e mostrar na tela, o seu tipo primitivo e todas as informações
    possíveis sobre ele.
"""
# Entrada de dados.
teclado = input('Digite algo: ')
tipo = type(teclado)

# Impressão de dados.
print('A informação digitada é: {}'.format(teclado))

# Mostrará todas as informações e o seu tipo primitivo.
print('A informação digitada é um {}?'.format(tipo))
print('A informação digitada é Alfanumérico?', teclado.isalnum())
print('A informação digitada é Numérico?', teclado.isnumeric())
print('A informação digitada é um Método String?', teclado.isascii())
print('A informação digitada é um Dígito?', teclado.isdigit())
print('A informação digitada é Alfabético?', teclado.isalpha())
print('A informação digitada é um Decimal?', teclado.isdecimal())
print('A informação digitada é um Identificador?', teclado.isidentifier())
print('A informação digitada está digitada em letras minúsculas?', teclado.islower())
print('A informação digitada é imprimível?', teclado.isprintable())
print('A informação digitada, tem algum espaço?', teclado.isspace())
print('A informação digitada é um título?', teclado.istitle())
print('A informação digitada, está em caixa alta?', teclado.isupper())

