num_inicial = 0
num_final = 0

num = int(input('Informe o número que deseja multiplicar: '))

while num_inicial >= num_final:
    num_inicial = int(input('Informe por qual valor deseja iniciar a multiplicação: '))
    num_final = int(input(f'Informe até qual valor deseja multiplicar {num}: '))
    if num_inicial >= num_final:
        print('Impossível realizar multiplicação!\nNúmero Inicial maior do que número final!')

for m in range(num_inicial, num_final + 1):
    print(f'{num:>1} x {m:>2} = {num * m:>3}')
