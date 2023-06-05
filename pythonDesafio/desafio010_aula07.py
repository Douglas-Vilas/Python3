''' O objetivo desse dasafio é: Criar um programa que leia quanto dinheiro uma pessoa
    tem na carteira e mostre quantos Dólares ela pode comprar. 
'''

def converter_para_dolar(valor_reais, taxa_cambio):
    '''
    -----------------------------------------------------------------------
    Converte um valor em reais, para dólares, com base na taxa de câmbio.
    -----------------------------------------------------------------------
    '''
    valor_dolar = valor_reais / taxa_cambio
    return valor_dolar

def main():
    '''
    -------------------------------
    Função principal do programa.
    -------------------------------
    '''
    # Obtém a informação digitada pelo usuário
    valor_reais = float(input("Digite o valor em reais: "))

    # Define a taxa de câmbio atual
    taxa_cambio = 4.96

    # Converter o valor para dólares
    valor_dolar = converter_para_dolar(valor_reais, taxa_cambio)

    # Exibe o resultado
    print(f'Com R$ {valor_reais:.2f}, você pode comprar US$ {round(valor_dolar, 2):.2f}')

# Executa o programa
if __name__ == '__main__':
    main()
