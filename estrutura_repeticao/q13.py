num_1 = int(input('Informe o primeiro número: '))
num_2 = int(input('Informe o segundo número: '))

total = 1

for n in range(1, num_2 + 1):
    total = total * num_1
    
print(f'O valor total é igual a {total}')
