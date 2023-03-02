# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

num = []
par = []
impar = []

for n in range(20):
    num.append(int(input(f'Informe o {n + 1}º número: ')))
    if num[n] % 2 == 0:
        par.append(num[n])
    else:
        impar.append(num[n])

print(f'Números: {sorted(num)}')
print(f'Pares: {sorted(par)}')
print(f'Ímpares: {sorted(impar)}')
