# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
# from math import prod

num = []
multiplicacao = 1

for n in range(5):
    num.append(int(input(f'Informe o {n + 1}º número: ')))
    multiplicacao *= num[n]

print(f'Números: {num}')
print(f'A soma dos números é igual a {sum(num)}')
print(f'A multiplicação dos números é igual a {multiplicacao}')
# print(f'A multiplicação dos números é igual a {prod(num)}')  # caso esteja utilizando python 3.8 ou superior, pode
# utilizar método prod da biblioteca math
