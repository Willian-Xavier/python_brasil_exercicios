# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

idade = [
    10, 11, 13, 11, 13, 12, 11, 15, 12, 9, 13, 14, 15, 11, 12, 15, 16, 14, 15, 13, 13, 12, 11, 10, 7, 8, 9, 10, 11, 12]
altura = [1.69, 1.57, 1.65, 1.58, 1.78, 1.45, 1.69, 1.54, 1.52, 1.45, 1.36, 1.66, 1.39, 1.45, 1.77, 1.56, 1.45, 1.78,
          1.63, 1.47, 1.24, 1.45, 1.46, 1.59, 1.56, 1.67, 1.45, 1.62, 1.59, 1.66]
qtde_alunos_acima_13_abaixo_media = 0

# CÓDIGO PARA RECEBER A ENTRADA DO USUÁRIO
# for i in range(30):
#     idade.append(int(input(f'Informe a idade do {i + 1}º aluno: ')))
#     altura.append(float(input(f'Informe a altura do {i + 1}º aluno: ')))

media_altura = sum(altura) / len(idade)

for y in range(len(altura)):
    if idade[y] == 13 and altura[y] < media_altura:
        qtde_alunos_acima_13_abaixo_media += 1

print(f'A quantidade de alunos com mais de 13 anos e altura acima da média foi de {qtde_alunos_acima_13_abaixo_media}.')
