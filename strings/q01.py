# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

def compara_strings(string_1, string_2):
    print(f'String 1: {string_1}')
    print(f'String 2: {string_2}')
    print(f'Tamanho da String 1: {len(string_1)} caracteres.')
    print(f'Tamanho da String 2: {len(string_2)} caracteres.')
    if len(string_1) == len(string_2):
        print('As duas strings possuem tamanhos iguais.')
    else:
        print('As duas strings possuem tamanhos diferentes.')

    if string_1.lower() == string_2.lower():
        print('As duas strings possuem conteúdos iguais.')
    else:
        print('As duas strings possuem conteúdos diferentes.')


frase_1 = str(input('Infome a primeira string: '))
frase_2 = str(input('Informe a segunda string: '))
compara_strings(frase_1, frase_2)
