# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def numero_reverso(numero):
    return numero[::-1]


num = str(input('Informe um número: '))
print(f'O número {num} invertido é igual a {numero_reverso(num)}.')
