cand_1 = 0
cand_2 = 0
cand_3 = 0
voto = 0

num_total_elei = int(input('Informe o número total de eleitores: '))

for n in range(1, num_total_elei + 1):
    print('============= CANDIDATOS =============')
    print('1 - Candidato 1')
    print('2 - Candidato 2')
    print('3 - Candidato 3')
    print('======================================')
    while 1 != voto != 2 and voto != 3: 
        voto = int(input(f'Informe o voto do {n}º eleitor: '))
        
        if voto == 1:
            cand_1 += 1
        elif voto == 2:
            cand_2 += 1
        elif voto == 3:
            cand_3 += 1
        else:
            print('Candidato inexistente!\nDigite Novamente!') 
        
    voto = 0

print(f'Candidato 1: {cand_1} votos')
print(f'Candidato 2: {cand_2} votos')
print(f'Candidato 3: {cand_3} votos')
