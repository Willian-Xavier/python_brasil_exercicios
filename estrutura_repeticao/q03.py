nome = ''
idade = -1
salario = 0
sexo = ''
est_civil = ''

while len(nome) < 3:
    nome = str(input('Informe o nome do usuário: '))
    
    if len(nome) < 3:
        print('Tamanho do nome inválido!\nDigite Novamente!')

while idade < 0 or idade > 150:
    idade = int(input('Informe a idade: '))

    if idade < 0 or idade > 150:
        print('Idade Inválida!\nDigite Novamente!')

while salario == 0:
    salario = float(input('Informe o salário: '))

    if salario == 0:
        print('Salário Inválido!\nDigite Novamente!')

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo: ')).upper()

    if sexo != 'M' and sexo != 'F':
        print('Sexo Inválido!\nDigite Novamente!')

while est_civil != 'S' and est_civil != 'C' and est_civil != 'V' and est_civil != 'D':
    est_civil = str(input('Informe o estado civil: S - Solteiro / C - Casado / V - Viúvo(a) / D - Divorciado: ')).upper()

    if est_civil != 'S' and est_civil != 'C' and est_civil != 'V' and est_civil != 'D':
        print('Estado Civil Inválido!\nDigite Novamente!')
        