# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.O resultado do atleta será determinado
# pela média dos cinco valores restantes.Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.O programa deve ser encerrado
# quando não for informado o nome do atleta.A saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5m
# Segundo Salto: 6.1m
# Terceiro Salto: 6.2m
# Quarto Salto: 5.4m
# Quinto Salto: 5.3m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9m

nome_atleta = []
notas_atletas = []
notas = []

while True:
    nome = str(input('Informe o nome do atleta: '))
    if len(nome) == 0:
        break
    nome_atleta.append(nome)
    for i in range(5):
        notas.append(float(input(f'Informe a {i + 1}ª nota do atleta: \n')))
    notas_atletas.append(notas.copy())
    notas.clear()

print('\n\n\n')

for nome in range(len(nome_atleta)):
    print(f'Atleta: {nome_atleta[nome]}\n')

    print(f'Primeiro salto: {notas_atletas[nome][0]}m')
    print(f'Segundo salto: {notas_atletas[nome][1]}m')
    print(f'Terceiro salto: {notas_atletas[nome][2]}m')
    print(f'Quarto salto: {notas_atletas[nome][3]}m')
    print(f'Quinto salto: {notas_atletas[nome][4]}m\n\n')
    print('Resultado final: ')
    print(f'Atleta: {nome}')
    print(f'Saltos: {notas_atletas[nome][0]} - {notas_atletas[nome][1]} - {notas_atletas[nome][2]} - '
          f'{notas_atletas[nome][3]} - {notas_atletas[nome][4]}')
    media_saltos = sum(notas_atletas[nome]) / 5
    print(f'Média dos saltos: {media_saltos:.2f}m\n')
    print('---------------------------------------------\n\n')
