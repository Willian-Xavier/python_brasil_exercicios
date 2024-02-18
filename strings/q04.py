# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
# o nome em formato de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

def nome_vertical_escada(nome):
    for cont in range(1, (len(nome) + 1)):
        for letra in range(cont):
            print(nome[letra].upper(), end='')
        print()


palavra = str(input('Informe a palavra a ser exibida: '))
nome_vertical_escada(palavra)
