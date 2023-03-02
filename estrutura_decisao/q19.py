separador_1 = ''
separador_2 = ''

num = input('Informe um número: ')

c = int(num) // 100 % 10
d = int(num) // 10 % 10
u = int(num) // 1 % 10

if int(num) < 1000:
    if c > 0 and d > 0 and u > 0:
        separador_1 = ', '
        separador_2 = ' e '
    elif c > 0 and d > 0:
        separador_1 = ' e '
        separador_2 = ''
    elif (c > 0 and u > 0) or (d > 0 and u > 0):
        separador_1 = ''
        separador_2 = ' e '

    if c > 0:
        if c == 1:
            c = '1 centena'
        else:
            c = (f'{c} centenas')
    else:
        c = ''
    
    if d > 0:
        if d == 1:
            d = '1 dezena'
        else:
            d = (f'{d} dezenas')
    else:
        d = ''
    
    if u > 0:
        if u == 1:
            u = '1 unidade'
        else:
            u = (f'{u} unidades') 
    else:
        u = ''
else:
    print('Número Inválido!')
    
print(f'{c}{separador_1}{d}{separador_2}{u}')


# if num < 1000:
#     if len(str(num)) == 3:
#         print(f'{num // 100 % 10} centena(s), {num // 10 % 10} dezena(s) e {num // 1 % 10} unidade(s)')
#     elif len(str(num)) == 2:
#         print(f'{num // 10 % 10} dezena(s) e {num // 1 % 10} unidade(s)')
#     else:
#         print(f'{num // 1 % 10} unidade(s)')
# else:
#     print('Número Inválido!')
