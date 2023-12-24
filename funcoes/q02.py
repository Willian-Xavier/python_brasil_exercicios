# Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
#
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprime_numeros(numero):
    for num in range(1, numero + 1):
        for j in range(1, num + 1):
            print(j, end=' ')
        print()


valor = int(input('Informe um número: '))
imprime_numeros(valor)
