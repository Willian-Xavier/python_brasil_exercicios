nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

media = (nota_1 + nota_2) / 2

# Lógica 1

print('=========================')
print(f'Nota 1 = {nota_1:.2f}')
print(f'Nota 2 = {nota_2:.2f}')
print(f'Média = {media:.2f}')
print('=========================')

if 9 <= media <= 10:
    print('''Conceito 'A' ''')
    print('APROVADO')
elif 7.5 <= media < 9:
    print('''Conceito 'B' ''')
    print('APROVADO')
elif 6 <= media < 7.5:
    print('''Conceito 'C' ''')
    print('APROVADO')
elif 4 <= media < 6:
    print('''Conceito 'D' ''')
    print('REPROVADO')
elif 0 <= media < 4:
    print('''Conceito 'E' ''')
    print('REPROVADO')

# Lógica 2

# if 9 <= media < 10:
#     conceito = 'A'
# elif 7.5 <= media < 9:
#     conceito = 'B'
# elif 6 <= media < 7.5:
#     conceito = 'C'
# elif 4 <= media < 6:
#     conceito = 'D'
# elif 0 <= media < 4:
#     conceito = 'E'
#
# print(f'Média = {media:.2f}')
# print(f'Conceito {conceito}')

# Lógica 3

# if 9 <= media < 10:
#     print(f'Média = {media:.2f}')
#     print('''Conceito 'A' ''')
# elif 7.5 <= media < 9:
#     print(f'Média = {media:.2f}')
#     print('''Conceito 'B' ''')
# elif 6 <= media < 7.5:
#     print(f'Média = {media:.2f}')
#     print('''Conceito 'C' ''')
# elif 4 <= media < 6:
#     print(f'Média = {media:.2f}')
#     print('''Conceito 'D' ''')
# elif 0 <= media < 4:
#     print(f'Média = {media:.2f}')
#     print('''Conceito 'E' ''')
