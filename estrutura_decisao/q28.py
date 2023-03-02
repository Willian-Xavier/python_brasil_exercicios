op = 0
tipo_carne = ''
qtde = 0
op_pgto = 0
forma_pgto = ''
valor_total = 0
valor_desconto = 0

while op != 1 and op != 2 and op != 3:
    print('================== TABELA DE PREÇOS ==================')
    print('\t\tAté 5Kg\t\t\tAcima de 5Kg\n------------------------------------------------------')
    print('1 - Filé Duplo \tR$4,90/kg\t|\tR$5,80/Kg')
    print('2 - Alcatra \tR$5,90/Kg\t|\tR$6,80/Kg')
    print('3 - Picanha \tR$6,90/Kg\t|\tR$7,80/Kg')
    print('======================================================')
    op = int(input('Informe o tipo de carne desejado: '))
    if op == 1:
        tipo_carne = 'Filé Duplo'
    elif op == 2:
        tipo_carne = 'Alcatra'
    elif op == 3:
        tipo_carne = 'Picanha'
    else:
        print('Opção Inválida!\nDigite Novamente!')

qtde = float(input('Informe a quantidade de carne desejada: '))

while op_pgto != 1 and op_pgto != 2 and op_pgto != 3:
    print('================ OPÇÕES DE PAGAMENTO ================')
    print('1 - Cartão Tabajara')
    print('2 - Dinheiro')
    print('3 - Outros cartões')
    print('=====================================================')
    op_pgto = int(input('Informe o tipo de pagamento desejado: '))
    if op_pgto == 1:
        forma_pgto = 'Cartão Tabajara'
    elif op_pgto == 2:
        forma_pgto = 'Dinheiro'
    elif op_pgto == 3:
        forma_pgto = 'Outros cartões'
    else:
        print('Forma de Pagamento Inválida!\nDigite Novamente!')

if op == 1:
    if qtde <= 5:
        valor_total = 4.90 * qtde
    else:
        valor_total = 5.80 * qtde
elif op == 2:
    if qtde <= 5:
        valor_total = 5.90 * qtde
    else:
        valor_total = 6.80 * qtde
else:
    if qtde <= 5:
        valor_total = 6.90 * qtde
    else:
        valor_total = 7.80 * qtde


print('==================== CUPOM FISCAL ===================')
print(f'Tipo de carne: {tipo_carne}')
print(f'Quantidade: {qtde}/Kg')
print(f'Preço Total: R${valor_total:.2f}')
print(f'Tipo de Pagamento: {forma_pgto}')
if op_pgto == 1:
    valor_desconto = (valor_total * 5) / 100
    print(f'Valor do Desconto: R${valor_desconto:.2f}')
print(f'Valor a Pagar: R${valor_total - valor_desconto:.2f}')
print('=====================================================')
