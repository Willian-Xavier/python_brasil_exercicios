# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
# a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

for i in range(12):
    temperaturas.append(float(input(f'Informe a temperatura média do {i + 1}º mês: ')))

media_anual = sum(temperaturas) / 12
print(f'Temperatura Média Anual: {media_anual:.1f}°')

for j in temperaturas:
    if j > media_anual:
        print(j, '°', sep='', end=' - ')
        print(meses[temperaturas.index(j)])
