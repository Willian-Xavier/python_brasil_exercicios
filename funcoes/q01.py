# Faça um programa para imprimir:
# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
#
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprime_numeros(numero):
    for num in range(1, numero + 1):
        for j in range(1, num + 1):
            print(num, end=' ')
        print()


# def imprime_numeros(numero):
#     for num in range(1, numero + 1):
#         print(str(num) * num)

valor = int(input('Informe um número: '))
imprime_numeros(valor)
