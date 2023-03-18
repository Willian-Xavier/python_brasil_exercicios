import math

a = []
soma = 0

for i in range(10):
    a.append(int(input(f'Informe o {i + 1}º número: ')))
    soma += math.pow(a[i], 2)

print(int(soma))
