op = 0

print('=================== TABELA DE PREÇOS ===================')
print('\t\tAté 5Kg\t\t\tAcima de 5Kg')
print('1 - Morango\tR$2,50/Kg\t\tR$2,20/Kg')
print('2 - Maçã\tR$1,80/Kg\t\tR$1,50/Kg')
print('========================================================')
while 1 != op != 2:
    op = int(input('Informe a opção desejada: '))
    if 1 != op != 2:
        print('Opção Inválida!\nDigite Novamente!')

peso = float(input('Informe quantos quilos deseja: '))

valor_total = 0

if op == 1:
    if peso <= 5:
        valor_total = 2.50 * peso
    else:
        valor_total = 2.20 * peso
else:
    if peso <= 5:
        valor_total = 1.80 * peso
    else:
        valor_total = 1.50 * peso

if valor_total > 25 or peso > 8:
    valor_total = valor_total - ((valor_total * 10) / 100)

print(f'O valor total das compras foi de R${valor_total:.2f}') 
