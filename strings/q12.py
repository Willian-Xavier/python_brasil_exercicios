# Valida e corrige número de telefone. Faça um programa que leia um número de
# telefone, e corrija o número no caso deste conter somente 7 dígitos,
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem o
# traço separador.
#
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

def corrige_numero(numero):
    num = [item for item in numero]
    if len(num) <= 7 and '-' not in num:
        num.insert(0, '3')
        num.insert(4, '-')
    elif len(num) == 8 and '-' not in num:
        num.insert(4, '-')
    elif len(num) == 8 and '-' in num:
        num.insert(0, '3')
    else:
        return ''.join(num)

    return ''.join(num)


print(corrige_numero(str(input('Informe o número do telefone: '))))
