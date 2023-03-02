fatorial = 1

num = int(input('Informe um número: '))

for n in range(1, num + 1):
    fatorial = fatorial * n
    
print(f'O fatorial de {num} é igual a {fatorial}')
