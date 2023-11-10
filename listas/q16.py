# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
salarios = [254, 325, 469, 386, 785, 452, 399, 415, 559, 617, 335, 400, 1000, 1200, 5000, 999]
faixas = [0] * 9

print(sorted(salarios))

for i in range(len(salarios)):
    if salarios[i] > 999:
        faixas[8] += 1
        continue
    faixas[salarios[i] // 100 - 2] += 1

print(f'Entre $200 - $299 = {faixas[0]}')
print(f'Entre $300 - $399 = {faixas[1]}')
print(f'Entre $400 - $499 = {faixas[2]}')
print(f'Entre $500 - $599 = {faixas[3]}')
print(f'Entre $600 - $699 = {faixas[4]}')
print(f'Entre $700 - $799 = {faixas[5]}')
print(f'Entre $800 - $899 = {faixas[6]}')
print(f'Entre $900 - $999 = {faixas[7]}')
print(f'Entre $1000 em diante = {faixas[8]}')
