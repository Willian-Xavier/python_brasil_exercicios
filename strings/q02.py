# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
# nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
# usuário pode digitar letras maiúsculas ou minúsculas.

def nome_contrario(nome):
    return nome[::-1].upper()


palavra = str(input('Infome o nome a ser convertido: '))
print(nome_contrario(palavra))
