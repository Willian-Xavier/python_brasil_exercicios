# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# Lógica 1

vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for i in range(10):
    vetor_1.append(int(input(f'Informe o {i + 1}º número do Vetor 1: ')))

for j in range(10):
    vetor_2.append(int(input(f'Informe o {j + 1}º número do Vetor 2: ')))

for y in range(10):
    vetor_3.append(int(input(f'Informe o {y + 1}º número do Vetor 3: ')))

for j, y, z in zip(vetor_1, vetor_2, vetor_3):
    vetor_4.append(j)
    vetor_4.append(y)
    vetor_4.append(z)

print('Números intercalados: ', end='')
print(*vetor_4, sep=' - ')

# Lógica 2

# vetor_1 = []
# vetor_2 = []
# vetor_3 = []
# vetor_4 = []
#
# def vetores(vetor, nome):
#     for i in range(10):
#         vetor.append(int(input(f'Informe o {i + 1}º número do {nome}: ')))
#
#     for j, y, z in zip(vetor_1, vetor_2, vetor_3):
#         vetor_4.append(j)
#         vetor_4.append(y)
#         vetor_4.append(z)
#
#
# vetores(vetor_1, 'Vetor 1')
# vetores(vetor_2, 'Vetor 2')
# vetores(vetor_3, 'Vetor 3')
# print('Números intercalados: ', end='')
# print(*vetor_4, sep=' - ')
