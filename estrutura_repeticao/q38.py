aumento = 0
salario = 1000
porc = 1.5
ano = 1996
ano_atual = 2023

while ano <= ano_atual:
    aumento = (salario * porc) / 100
    porc *= 2
    salario += aumento
    ano += 1
    
    print(f'Ano {ano}: R${salario:.2f}')


# for ano in range(1996, 2023+ 1):
#     if ano == 1996:
#         aumento = (1000 * porc) / 100
#         salario += aumento
#     else:
#         aumento = (salario * porc) / 100
#         salario += aumento
#         porc = porc + porc
        
#     print(f'Ano: {ano}: R${salario:.2f}')
        