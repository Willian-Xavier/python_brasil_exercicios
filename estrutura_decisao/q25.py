resp_1 = ''
resp_2 = ''
resp_3 = ''
resp_4 = ''
resp_5 = ''
cont_sim = 0

# Pergunta 1
while 'S' != resp_1 != 'N':
    resp_1 = str(input('Telefonou para a vítima? S - Sim / N - Não: ')).upper()
    
    if resp_1 == 'S':
        cont_sim += 1
    elif resp_1 != 'N':
        print('Resposta Inválida!\nDigite Novamente!')
        
# Pergunta 2
while 'S' != resp_2 != 'N':
    resp_2 = str(input('Esteve no local do crime? S - Sim / N - Não: ')).upper()
    
    if resp_2 == 'S':
        cont_sim += 1
    elif resp_2 != 'N':
        print('Resposta Inválida!\nDigite Novamente!')

# Pergunta 3        
while 'S' != resp_3 != 'N':
    resp_3 = str(input('Mora perto da vítima? S - Sim / N - Não: ')).upper()
    
    if resp_3 == 'S':
        cont_sim += 1
    elif resp_3 != 'N':
        print('Resposta Inválida!\nDigite Novamente!')

# Pergunta 4       
while 'S' != resp_4 != 'N':
    resp_4 = str(input('Devia para a vítima? S - Sim / N - Não: ')).upper()
    
    if resp_4 == 'S':
        cont_sim += 1
    elif resp_4 != 'N':
        print('Resposta Inválida!\nDigite Novamente!')

# Pergunta 5        
while 'S' != resp_5 != 'N':
    resp_5 = str(input('Já trabalhou com a vítima? S - Sim / N - Não: ')).upper()
    
    if resp_5 == 'S':
        cont_sim += 1
    elif resp_5 != 'N':
        print('Resposta Inválida!\nDigite Novamente!')
        
print('============ CLASSIFICAÇÃO ============')
if cont_sim == 1:
    print('Inocente!')
elif cont_sim == 2:
    print('Suspeito(a)!')
elif 3 <= cont_sim <=4:
    print('Cúmplice!')
else:
    print('Assassino(a)!')
        