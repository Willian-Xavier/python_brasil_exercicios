valor_divida = float(input('Informe o valor da dívida: '))

porc = 0

print('=' * 100)
print('Quantidade de Parcelas\t\t\t% de Juros Sobre o Valor Inicial da Dívida')

for parcelas in range(1, 16, 3):
    if parcelas == 1:
        print(f'{parcelas:>2}\t\t\t\t\t{porc:>2}')
    elif parcelas == 4:
        print(f'{parcelas -1:>2}\t\t\t\t\t{porc}')
    else:
        print(f'{parcelas -1:>2}\t\t\t\t\t{porc - 5}')
        
    porc += 10
    
print('=' * 100)

porc = 5
valor_juros = 0

print('=' * 100)
print('Valor da Dívida|\tValor dos Juros|\tQuantidade de Parcelas|\t\tValor das Parcelas')



for divida in range(0, 15, 3):
    if divida == 0:
        print(f'R${valor_divida + valor_juros:.2f}\t\t\tR${valor_juros:.2f}{divida +1:>32}\t\tR${valor_divida:.2f}')
    else:
        valor_juros = (valor_divida * porc) / 100
        print(f'R${valor_divida + valor_juros:.2f}\t\t\tR${valor_juros:.2f}{(divida):>30}\t\tR${(valor_divida + valor_juros) / (divida):.2f}')
    
    porc += 5
    
    
# for divida in range(1, 16, 3):
#     if divida == 1:
#         print(f'R${valor_divida + valor_juros:.2f}\t\t\tR${valor_juros:.2f}{divida:>32}\t\tR${(valor_divida + valor_juros) / (divida):.2f}')
#     elif divida == 4:
#         valor_juros = (valor_divida * porc) / 100
#         print(f'R${valor_divida + valor_juros:.2f}\t\t\tR${valor_juros:.2f}{divida -1:>30}\t\tR${(valor_divida + valor_juros) / (divida - 1):.2f}')
#     else:
#         valor_juros = (valor_divida * porc) / 100
#         print(f'R${valor_divida + valor_juros:.2f}\t\t\tR${valor_juros:.2f}{(divida -1):>30}\t\tR${(valor_divida + valor_juros) / (divida -1):.2f}')
    
#     porc += 5

      
# print(f'R${valor_divida:.2f}{divida:>30}{divida:>31}\t\tR${valor_divida * divida:.2f}')
# print(f'R${valor_divida + valor_15:.2f}\t\tR${valor_15:>20.2f}{6:>32}\t\tR${(valor_divida + valor_15) / 6:.2f}')
# print(f'R${valor_divida + valor_20:.2f}\t\t\tR${valor_20:.2f}{9:>32}\t\tR${(valor_divida + valor_20) / 9:.2f}')
# print(f'R${valor_divida + valor_25:.2f}\t\t\tR${valor_25:.2f}{12:>32}\t\tR${(valor_divida + valor_25) / 12:.2f}')
