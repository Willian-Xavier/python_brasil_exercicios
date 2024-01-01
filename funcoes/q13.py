# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
# receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo
# é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma
# elegante.

def desenha_moldura(linhas, colunas):
    if linhas <= 0:
        linhas = 1

    if colunas > 20:
        colunas = 20

    for linha in range(linhas):
        for coluna in range(colunas):
            print('+', end=' ')
        print()


linha = int(input('Informe a quantidade de linhas do retângulo: '))
coluna = int(input('Informe a quantidade de colunas do retângulo: '))
desenha_moldura(linha, coluna)
