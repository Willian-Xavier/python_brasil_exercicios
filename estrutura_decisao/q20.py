nota_1 = float(input('Informe a primeira nota do aluno(a): '))
nota_2 = float(input('Informe a segunda nota do aluno(a): '))
nota_3 = float(input('Informe a terceira nota do aluno(a): '))

media = (nota_1 + nota_2 + nota_3) / 3

print(f'Média: {media:.2f}')

if media == 10:
    print('Aprovado com distinção!')
elif media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
    