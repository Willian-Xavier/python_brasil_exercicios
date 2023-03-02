# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes 

cod = 1
alt = 0
peso = 0
maior_alt = 0
menor_alt = 5000
maior_peso = 0
menor_peso = 10000
cod_maior_alt = 0
cod_menor_alt = 0
cod_maior_peso = 0
cod_menor_peso = 0
qtde_clientes = 0
soma_peso = 0
soma_alt = 0

while cod != 0:
    cod = int(input('Informe o seu código: '))
    if cod == 0:
        break
    alt = float(input('Informe sua altura: '))
    peso = float(input('Informe o seu peso: '))
    
    soma_peso += peso
    soma_alt += alt
    qtde_clientes += 1

    if alt > maior_alt:
        maior_alt = alt
        cod_maior_alt = cod
    
    if alt < menor_alt:
        menor_alt = alt
        cod_menor_alt = cod
        
    if peso > maior_peso:
        maior_peso = peso
        cod_maior_peso = cod
    
    if peso < menor_peso:
        menor_peso = peso
        cod_menor_peso = cod
        
print(f'Maior Altura: {maior_alt}')
print(f'Código Maior Altura: {cod_maior_alt}')
print(f'Menor Altura: {menor_alt}')
print(f'Código Menor Altura: {cod_menor_alt}')
print(f'Maior Peso: {maior_peso}')
print(f'Código Maior Peso: {cod_maior_peso}')
print(f'Menor Peso: {menor_peso}')
print(f'Código Menor Peso: {cod_menor_peso}')
print(f'Média de Altura: {soma_alt / qtde_clientes:.2f}')
print(f'Média de Peso: {soma_peso / qtde_clientes:.2f}')
