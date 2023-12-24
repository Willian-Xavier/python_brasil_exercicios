situacao = []
valores = []

with open('planilha.csv', mode='r') as usuario:
    for dados in usuario:
        situacao_atual = dados.split(',', 2)[1]
        salario = dados.split(',', 3)[2]
        situacao.append(situacao_atual)
        valores.append(salario)

with open('relatorio.txt', mode='w') as dado:
    for itera in range(len(valores)):
        dado.write(f'{valores[itera]}')

