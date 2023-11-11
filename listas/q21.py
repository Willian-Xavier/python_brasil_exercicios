# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
# litro de combustível. Calcule e mostre:
#
# a - O modelo do carro mais econômico;
# b - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
# quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de
# exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a
# cada execução do programa.

def calcula_consumo(consumo_litros):
    return 1000 / consumo_litros


def calcula_valor_viagem(consumo_litros):
    return (1000 / consumo_litros) * 2.25


# LISTA CARREGADA
carros = ['Volvo XC60', 'BMW X6 M Competition', 'Fusca', 'BYD Song Plus', 'Civic']
consumo = [24.5, 8.4, 11.9, 26, 9]

# LINHAS DE CÓDIGO PARA RECEBER ENTRADAS DO USUÁRIO
# carros = []
# consumo = []
# print('Comparativo de Consumo de Combustível')
# for insere in range(5):
#     carros.append(str(input(f'Informe o nome do {insere + 1}º carro: ')))
#     consumo.append(float(input(f'Informe o consumo do {carros[insere]} em Km/L: ')))

print('Relatório Final')
for exibicao in range(len(carros)):
    print(f'{exibicao + 1} - {carros[exibicao]:20}             - {consumo[exibicao]:>10.1f} - '
          f'{calcula_consumo(consumo[exibicao]):>7.1f} litros - R${calcula_valor_viagem(consumo[exibicao]):>7.2f}')

print(f'O menor consumo é o do {carros[consumo.index(max(consumo))]}.')
