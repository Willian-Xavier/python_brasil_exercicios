nota = []
melhor_nota = 0
pior_nota = 0
media_notas = 0

# Entrada de dados
nome_atleta = str(input('Informe o nome do(a) atleta: '))

for n in range(1, 8):
    nota.append(float(input(f'Infome a {n}ª nota: ')))

# Processamento de dados
melhor_nota = max(nota)
pior_nota = min(nota)
media_notas = ((sum(nota)) - (melhor_nota + pior_nota)) / 5

# Saída de dados
print('=' * 50)
print(f'Atleta: {nome_atleta}')
for n in range(len(nota)):
    print(f'Nota: {nota[n]:.2f}')
print('Resultado Final:')
print(f'Atleta: {nome_atleta}')  
print(f'Melhor Nota: {melhor_nota:.2f}')
print(f'Pior Nota: {pior_nota:.2f}')
print(f'Média: {media_notas:.2f}')
print('=' * 50)
