num_1 = int(input('Informe um número: '))
num_2 = int(input('Informe outro número: '))

# Lógica 1
if num_1 > num_2:
    print(f'O número {num_1} é maior do que o número {num_2}')
else:
    print(f'O número {num_2} é maior do que o número {num_1}')

# Lógica 2
print(f'O número {max(num_1, num_2)} é maior do que o número {min(num_1, num_2)}')
