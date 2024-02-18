# Nome na vertical em escada invertida. Altere o programa anterior de modo
# que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

def nome_vertical_invertido(nome):
    for cont in range((len(nome)), 0, - 1):
        for letra in range(cont):
            print(nome[letra].upper(), end='')
        print()


palavra = str(input('Informe a palavra a ser exibida: '))
nome_vertical_invertido(palavra)
