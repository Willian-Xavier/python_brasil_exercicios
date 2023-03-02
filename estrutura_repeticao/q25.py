idade = 0
cont = 0
soma_idade = 0

while idade >= 0:
    idade = int(input('Informe a idade: Digite um valor negativo para encerrar: '))
    
    if (idade >= 0):
        soma_idade += idade
        cont += 1
    
media_idade = soma_idade / cont

if 0 < media_idade <= 25:
    print(f'A média de idade da turma é de {media_idade:.2f} anos.')
    print('Turma Jovem')
elif 26 <= media_idade <= 60:
    print(f'A média de idade da turma é de {media_idade:.2f} anos.')
    print('Turma Adulta')
else:
    print(f'A média de idade da turma é de {media_idade:.2f} anos.')
    print('Turma Idosa')
