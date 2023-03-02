nome_atleta = 'a'
saltos = []
melhor_salto = 0
pior_salto = 0
media_saltos = 0

while nome_atleta != '':
    nome_atleta = str(input('Informe o nome do atleta: '))
    
    if nome_atleta != '':
        for sal in range(1, 6):
            saltos.append(float(input(f'Infome a distância do {sal}º salto: ')))

        melhor_salto = max(saltos)
        pior_salto = min(saltos)
        media_saltos = ((sum(saltos)) - (melhor_salto + pior_salto)) / 3

        print('=' * 50)
        print(f'Atleta: {nome_atleta}')
        for sal in range(len(saltos)):
            print(f'{sal + 1}º Salto: {saltos[sal]:.2f} m')
            
        print(f'Melhor Salto: {melhor_salto:.2f} m')
        print(f'Pior Salto: {pior_salto:.2f} m')
        print(f'Média dos Demais Saltos: {media_saltos:.2f} m\n')
        print(f'Resultado Final:\n{nome_atleta}: {media_saltos:.2f} m')
    else:
        print('Programa Encerrado!')
