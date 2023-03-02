# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
# por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
# ser encerrado.

op = 0
qtde_100 = 0
qtde_101 = 0
qtde_102 = 0
qtde_103 = 0
qtde_104 = 0
qtde_105 = 0
preco_100 = 0
preco_101 = 0
preco_102 = 0
preco_103 = 0
preco_104 = 0
preco_105 = 0
resp = 'S'

while resp == 'S':
    print('=' * 25, 'CARDÁPIO', '=' * 25)
    print('Especificação\t\tCódigo\t\tPreço')
    print('Cachorro Quente\t\t100\t\t\tR$1,20')
    print('Bauru Simples\t\t101\t\t\tR$1,30')
    print('Bauru Com Ovo\t\t102\t\t\tR$1,50')
    print('Hambúrguer\t\t\t103\t\t\tR$1,20')
    print('Cheeseburguer\t\t104\t\t\tR$1,30')
    print('Refrigerante\t\t105\t\t\tR$1,00')
    print('=' * 60)

    while op != 100 and op != 101 and op != 102 and op != 103 and op != 104 and op != 105:
        op = int(input('Informe o código do seu pedido ou Digite 0 (zero) para sair: '))
        if op == 100 or op == 101 or op == 102 or op == 103 or op == 104 or op == 105:
            qtde = int(input('Informe a quantidade de itens: '))
            if op == 100:
                qtde_100 += qtde
                preco_100 += qtde_100 * 1.20
            elif op == 101:
                qtde_101 += qtde
                preco_101 += qtde_101 * 1.30
            elif op == 102:
                qtde_102 += qtde
                preco_102 += qtde_102 * 1.50
            elif op == 103:
                qtde_103 += qtde
                preco_103 += qtde_103 * 1.20
            elif op == 104:
                qtde_104 += qtde
                preco_104 += qtde_104 * 1.30
            elif op == 105:
                qtde_105 += qtde
                preco_105 += qtde_105 * 1.00
        elif op == 0:
            break
        else:
            print('Código do pedido inválido!\nDigite Novamente!')
        
    resp = ''
    
    while resp != 'S' and resp != 'N' and op != 0:
        resp = str(input('Deseja realizar um novo pedido? S - Sim / N - Não: ')).upper()
        if resp != 'S' and resp != 'N':
            print('Resposta Inválida!\nDigite Novamente!')
            
    op = -1
    qtde = 0

if (qtde_100 + qtde_101 + qtde_102 + qtde_103 + qtde_104 + qtde_105) > 0:
    
    print('=' * 25, 'PEDIDOS', '=' * 25)     

    if qtde_100 > 0:
        print(f'Cachorro Quente: R$1,20 x {qtde_100} = R${preco_100:.2f}')

    if qtde_101 > 0:
        print(f'Bauru Simples: R$1,30 x {qtde_101} = R${preco_101:.2f}')

    if qtde_102 > 0:
        print(f'Bauru Com Ovo: R$1,50 x {qtde_102} = R${preco_102:.2f}') 
        
    if qtde_103 > 0:
        print(f'Hambúrguer: R$1,20 x {qtde_103} = R${preco_103:.2f}') 

    if qtde_104 > 0:
        print(f'Cheeseburguer: R$1,30 x {qtde_104} = R${preco_104:.2f}')

    if qtde_105 > 0:
        print(f'Refrigerante: R$1,00 x {qtde_105} = R${preco_105:.2f}')

    print('=' * 59)
    print(f'Valor Total: R${preco_100 + preco_101 + preco_102 + preco_103 + preco_104 + preco_105:.2f}')
else:
    print('Programa Encerrado Pelo Usuário!')
