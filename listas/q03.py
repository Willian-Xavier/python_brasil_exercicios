# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for n in range(0, 4):
    notas.append(float(input(f'Informe a {n + 1}ª nota: ')))

print('=' * 10, 'NOTAS', '=' * 10)
for i in range(len(notas)):
    print(f'{i + 1}ª nota: {notas[i]:.2f}')

print(f'Média: {sum(notas) / 4:.2f}')
# print(f'Média: {sum(notas) / len(notas):.2f}')
print('=' * 27)
