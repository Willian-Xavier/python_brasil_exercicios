idade = [13, 12, 11, 15]
altura = [1.69, 1.57, 1.65, 1.58]
qtde_alunos_men_media = 0

# for i in range(4):
#     idade.append(int(input(f'Informe a idade do {i + 1}º aluno: ')))
#     altura.append(float(input(f'Informe a altura do {i + 1}º aluno: ')))

media_altura = sum(altura) / 30

for y in enumerate(altura):
    if idade == 13 and altura < media_altura:
        qtde_alunos_men_media += 1

print(qtde_alunos_men_media)
