prod_1 = str(input('Informe o nome do primeiro produto: '))
pre_prod_1 = float(input('Informe o preço do primeiro produto: '))
prod_2 = str(input('Informe o nome do segundo produto: '))
pre_prod_2 = float(input('Informe o preço do segundo produto: '))
prod_3 = str(input('Informe o nome do terceiro produto: '))
pre_prod_3 = float(input('Informe o preço do terceiro produto: '))

if pre_prod_1 < pre_prod_2 and pre_prod_1 < pre_prod_3:
    print(f'O produto mais barato é o {prod_1}, que custa R${pre_prod_1:.2f}')
elif pre_prod_2 < pre_prod_1 and pre_prod_2 < pre_prod_3:
    print(f'O produto mais barato é o {prod_2}, que custa R${pre_prod_2:.2f}')
else:
    print(f'O produto mais barato é o {prod_3}, que custa R${pre_prod_3:.2f}')
