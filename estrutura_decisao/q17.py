ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Ano Bissexto!')
        else:
            print(f'{ano} não corresponde a um ano bissexto!')
    else:
        print('Ano Bissexto!')
else:
    print(f'{ano} não corresponde a um ano bissexto!')
