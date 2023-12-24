# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
# gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

ocorrencias = [0] * 6

for lancamentos in range(100):
    ocorrencias[random.randrange(1, 7) - 1] += 1

for valores in range(len(ocorrencias)):
    print(f'{valores + 1} = {ocorrencias[valores]} ocorrências')
