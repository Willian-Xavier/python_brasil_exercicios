nota_1 = float(input('Informe a primeira nota do aluno: '))
nota_2 = float(input('Informe a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

if 7 <= media < 10:
    print('Aluno APROVADO!')
elif media < 7:
    print('Aluno REPROVADO!')
else:
    print('Aluno APROVADO COM DISTINÇÃO!')
