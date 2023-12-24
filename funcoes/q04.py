def positivo_negativo(numero):
    if numero > 0:
        return 'P'
    return 'N'


num = int(input('Informe um número: '))
print(positivo_negativo(num))
