resp = 'S'

while resp == 'S':
    cont = 0
    total_compra = 0
    preco_prod = 1
    lista = []
    nr_produto = []
    total_compra = 0

    print('=' * 20, ' Lojas Tabajara ', '=' * 20)

    while preco_prod != 0:
        preco_prod = float(input(f'Informe o preço do {cont + 1}º produto: '))
        if preco_prod > 0:
            nr_produto.append(cont)
            lista.append(preco_prod)
            cont += 1

    total_compra = sum(lista)
    dinheiro = 0

    while dinheiro < total_compra:
        dinheiro = float(input('Informe o valor fornecido pelo cliente: '))

        if dinheiro < total_compra:
            print('O valor fornecido é menor do que o valor total da compra!')

    print('=' * 19, ' Lista de Produtos ', '=' * 19)
    for li in range(cont):
        print(f'Produto {nr_produto[li] + 1}: R${lista[li]:.2f}')
    print(f'Quantidade de produtos: {cont}')
    print(f'Preço Total: R${total_compra:.2f}')
    print(f'Dinheiro: R${dinheiro:.2f}')
    print(f'Troco: R${dinheiro - total_compra:.2f}')
    print('=' * 58)
