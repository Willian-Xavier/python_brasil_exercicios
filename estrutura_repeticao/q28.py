valor_investido = 0
cont = 0

qtde_cds = int(input('Informe a quantidade de CD\'s que possui: '))

for i in range(1, qtde_cds + 1):
    valor_cd = float(input(f'Informe o valor do {i}º CD: '))
    
    valor_investido += valor_cd
    cont += 1
    
valor_medio = valor_investido / cont

print(f'O valor médio de cada CD é igual a R${valor_medio:.2f}')
