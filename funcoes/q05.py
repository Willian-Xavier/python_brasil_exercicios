def soma_imposto(aliquota, valor):
    return valor + ((valor * aliquota) / 100)


valor_produto = float(input('Informe o valor do produto: '))
aliquota_imposto = float(input('Informe a alíquota do imposto: '))

print(f'Valor total: R${soma_imposto(aliquota_imposto, valor_produto):.2f}')
