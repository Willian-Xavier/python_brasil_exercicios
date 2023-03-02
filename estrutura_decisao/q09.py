num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

if num_1 > num_2 > num_3:
    print(f'{num_1}, {num_2}, {num_3}')
elif num_2 > num_1 > num_3:
    print(f'{num_2}, {num_1}, {num_3}')
elif num_3 > num_1 > num_2:
    print(f'{num_3}, {num_1}, {num_2}')
elif num_2 > num_3 > num_1:
    print(f'{num_2}, {num_3}, {num_1}')
elif num_1 > num_3 > num_2:
    print(f'{num_1}, {num_3}, {num_2}')
