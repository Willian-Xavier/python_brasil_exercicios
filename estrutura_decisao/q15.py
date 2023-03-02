lado_1 = int(input('Informe o valor do lado 1 do triângulo: '))
lado_2 = int(input('Informe o valor do lado 2 do triângulo: '))
lado_3 = int(input('Informe o valor do lado 3 do triângulo: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print('Os lados formam um triângulo!')
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('TRIÂNGULO EQUILÁTERO')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('TRIÂNGULO ISÓSCELES')
    else:
        print('TRIÂNGULO ESCALENO')
else:
    print('A soma dos três lados não formam um triângulo!')
