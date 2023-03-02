# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma. 

# Gabarito
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
nome_aluno = []
respostas =[]
qtde_certas = []
menor = 0
acertos = 0
cont = 0
resp = 'S'

for gab in range(1, 11):
    gabarito.append(str(input(f'Informe a resposta da {gab}ª questão: ')))
    # utilizada para que o professor digite o gabarito das questões. Deve-se apagar as resposta do vetor gabarito

while resp == 'S':
    nome_aluno.append(str(input('Informe o nome do Aluno(a): ')))
    
    for quest in range(1, 11):
        respostas.append(str(input(f'Informe a resposta da {quest}ª questão: ')).upper())

    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            acertos += 1
        
    qtde_certas.append(acertos)
    
    # Reinicialização das variáveis
         
    resp = ''
    cont += 1
    acertos = 0
    respostas = []

    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja realizar um novo pedido? S - Sim / N - Não: ')).upper()
        if resp != 'S' and resp != 'N':
            print('Resposta Inválida!\nDigite Novamente!')

           
print('=' * 25, 'RELATÓRIO', '=' * 25)
for exibir in range(cont):
    print(f'Nome do Aluno(a): {nome_aluno[exibir]}')
    print(f'Quantidade de Respostas Certas: {qtde_certas[exibir]}')

print('=' * 61)
print('MAIOR ACERTO')
print(f'Nome do Aluno(a): {nome_aluno[qtde_certas.index(max(qtde_certas))]}')
print(f'Maior Quantidade de Questões Acertadas: {(max(qtde_certas))}')
print('MENOR ACERTO')
print(f'Nome do Aluno(a): {nome_aluno[qtde_certas.index(min(qtde_certas))]}')
print(f'Menor Quantidade de Questões Acertadas: {(min(qtde_certas))}')
print('=' * 61)
print(f'Total de Alunos que Utilizaram o Sistema: {cont}')
print(f'Média das Notas da Turma: {sum(qtde_certas) / cont:.2f}')
print('=' * 61)
