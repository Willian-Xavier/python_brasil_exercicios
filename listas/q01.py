# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

num = []

for n in range(0, 5):
    num.append(int(input(f'Informe o {n + 1}º número: ')))

nova_lista = str(sorted(num))[1:-1]

print(nova_lista, sep=' ')
