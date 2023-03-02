# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

num = -1
fatorial = 1
resp = 'S'

while resp == 'S':
    num = -1
    
    while num < 0 or num > 16:
        num = int(input('Informe um número: '))
        
        if num < 0 or num > 16:
            print('Número Inválido!\nDigite Novamente!')
    
    fatorial = 1
    
    for n in range(1, num + 1):
        fatorial = fatorial * n
        
    print(f'O fatorial de {num} é igual a {fatorial}')
    
    resp = ''
    
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja realizar um novo cálculo? S - Sim / N - Não: ')).upper()
        if resp != 'S' and resp != 'N':
            print('Resposta Inválida!\nDigite Novamente!')
    