print('================ PANIFICADORA PÃO DE ONTEM ================')
print('==================== TABELA DE PREÇOS =====================')

preco_pao = float(input('Informe o preço do pão por unidade: '))

for n in range(1, 51):
    print(f'{n:>2} - R${preco_pao * n:.2f}')

# i = 1

# while i <= 50:
#     print(f'{i:>2} - R${preco_pao * i:.2f}')
    
#     i += 1
