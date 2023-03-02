num = int(input('Informe um número: '))

print(f'========= TABUADA DE {num} =========')
for n in range(1, 11):
    print(f'{num:>1}  X {n:>2} ={num * n:>3}')
