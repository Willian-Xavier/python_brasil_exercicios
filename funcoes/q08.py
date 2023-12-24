# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contador_digitos(numero):
    qnt_digitos = 0
    for _ in str(numero):
        qnt_digitos += 1

    return qnt_digitos
    # return len(str(numero))


num = int(input('Informe um número inteiro: '))
print(f'Quantidade de dígitos: {contador_digitos(num)}')
