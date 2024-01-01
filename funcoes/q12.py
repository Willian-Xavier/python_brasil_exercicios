# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres
# embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra
# combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa
# alta ou caixa baixa, independentemente de como foram digitados.
import random


def embaralha_palavras(palavra):
    nova_palavra = ''
    indices = random.sample(range(0, len(palavra)), len(palavra))

    for i in range(len(palavra)):
        nova_palavra = nova_palavra + palavra[indices[i]].lower()

    return nova_palavra
    # palavra_embaralhada = list(palavra)
    # random.shuffle(palavra_embaralhada)
    # return ''.join(palavra_embaralhada).lower()


palavra = str(input('Digite a palavra a ser embaralhada: '))
print(f'Palavra embaralhada: {embaralha_palavras(palavra)}')
