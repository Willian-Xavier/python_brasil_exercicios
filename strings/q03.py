# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

def nome_vertical(nome):
    for letra in nome:
        print(letra.upper())


palavra = str(input('Informe a palavra a ser impressa na vertical: '))
nome_vertical(palavra)
