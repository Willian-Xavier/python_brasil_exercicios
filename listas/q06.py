# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

media = []
qtde_alunos_maior_7 = 0

for a in range(10):
    notas = []

    for n in range(4):
        notas.append(float(input(f'Informe a {n + 1}ª nota do {a + 1}º aluno(a): ')))

    media.append(sum(notas) / 4)
    # media.append(sum(notas) / len(notas))

for m in range(10):
    print(f'Média do {m + 1}º aluno(a): {media[m]:.2f}')
    if media[m] >= 7:
        qtde_alunos_maior_7 += 1

print(f'Quantidade de alunos com média maior ou igual a 7: {qtde_alunos_maior_7} Aluno(s)')
