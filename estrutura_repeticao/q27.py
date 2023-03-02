total_alunos = 0
qtde_alunos_turma = 41

qtde_turmas = int(input('Informe a quantidade de turmas: '))

for n in range(1, qtde_turmas + 1):
    while qtde_alunos_turma > 40:
        qtde_alunos_turma = int(input(f'Informe a quantidade de alunos da {n}ª turma: '))
        
        if qtde_alunos_turma <= 40:
            total_alunos += qtde_alunos_turma
        else:
            print('Quantidade de alunos excede o limite da turma!\nDigite Novamente!')
            
    qtde_alunos_turma = 41
    
media_alunos = total_alunos / qtde_turmas

print(f'A média de alunos por turma é de {media_alunos:.2f} discentes.')
