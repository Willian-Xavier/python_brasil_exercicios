# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    vetor_1.append(int(input(f'Informe o {i + 1}º número do Vetor 1: ')))

for n in range(10):
    vetor_2.append(int(input(f'Informe o {n + 1}º número do Vetor 2: ')))

for j, y in zip(vetor_1, vetor_2):
    vetor_3.append(j)
    vetor_3.append(y)

print('Números intercalados: ', end='')
print(*vetor_3, sep=' - ')
