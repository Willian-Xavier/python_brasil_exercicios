num_1 = int(input('Informe o primeiro número: '))
num_2 = int(input('Informe o segundo número: '))

print(f'Os números no intervalo entre {num_1} e {num_2} são: ')

soma = 0

for n in range(num_1 + 1, num_2):
    print(n, end=' ')
    soma += n
    
print(f'\nA soma dos números dentro do intevalo é igual a {soma}')
