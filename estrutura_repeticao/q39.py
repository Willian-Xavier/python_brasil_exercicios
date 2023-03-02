# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

num = 0
alt = 0
num_mais_alto = 0
num_mais_baixo = 0
mais_alto = 0
mais_baixo = 50000

for pesq in range(1, 6):
    num = int(input('Informe o número do aluno: '))
    alt = int(input('Informe a altura do aluno em centímetros: '))

    if alt > mais_alto:
        mais_alto = alt
        num_mais_alto = num
    
    if alt < mais_baixo:
        mais_baixo = alt
        num_mais_baixo = num
        
print('=' * 40)
print(f'Número do aluno mais alto: {num_mais_alto}cm')
print(f'Altura do aluno mais alto: {mais_alto}')
print('=' * 30)
print(f'Número do aluno mais baixo: {num_mais_baixo}cm')
print(f'Altura do aluno mais baixo: {mais_baixo}')
