num = int(input('Informe um número inteiro: '))

mult = 0

for count in range(2, num):
    if num % count == 0:
        print(f'Múltiplo de {count}')
        
        mult += 1
        
if mult == 0 and num > 1:
    print(f'{num} é um número primo!')
else:
    print(f'{num} tem {mult} múltiplos acima de 2 e abaixo dele mesmo!')
