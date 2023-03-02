resp = 'S'

while resp == 'S':
    pop_a = 0
    pop_b = 0
    tax_cresc_a = 0
    tax_cresc_b = 0
    anos_nec = 0
    
    pop_a = int(input('Informe a população do país \'A\': '))
    tax_cresc_a = float(input('Informe a taxa de crescimento do país \'A\': '))
    pop_b = int(input('Informe a população do país \'B\': '))
    tax_cresc_b = float(input('Informe a taxa de crescimento do país \'B\': '))
    
    while pop_a < pop_b:
        pop_a += ((pop_a * tax_cresc_a) / 100)
        pop_b += ((pop_b * tax_cresc_b) / 100)
        anos_nec += 1

    print(f'Anos necessários para que população do país \'A\' alcance a população do país \'B\' = {anos_nec}')
    
    resp = ''
    
    while 'S' != resp != 'N':
        resp = str(input('Deseja realizar novo cálculo? S - Sim / N - Não: ')).upper()
        
        if 'S' != resp != 'N':
            print('Resposta Inválida!\nDigite Novamente!')
