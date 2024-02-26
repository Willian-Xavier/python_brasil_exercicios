# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando
# outros símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do leet
# reflete uma subcultura relacionada ao mundo dos jogos de computador e
# internet, sendo muito usada para confundir os iniciantes e afirmar-se como
# parte de um grupo. Pesquise sobre as principais formas de traduzir as letras.
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet
# speak.
import random

from unidecode import unidecode


def leet_speak_generator(texto):
    dicionario_leet = {
        'A': ['4', '/\\', '@', '/-\\', '^', 'ä', 'ª', 'aye'],
        'B': ['8', '6', '|3', 'ß', 'P>', '|:'],
        'C': ['[', '¢', '<', '('],
        'D': ['|))', 'o|', '[)', 'I>', '|>', '?'],
        'E': ['3', '&', '£', 'ë', '[-', '€', 'ê', '|=-'],
        'F': ['|=', 'ph', '|#'],
        'G': ['6', '&', '(_+', '9', 'C-', 'gee (,'],
        'H': ['#', '/-/', '[-]', '{=}', '|-|', ']~[', '}{', ']-[', '}-{'],
        'I': ['1', '!', '|', '&', 'eye', '3y3', 'ï', '][', '[]'],
        'J': ['j', ';', '_/'],
        'K': ['X', '|<', '|{', ']{', '}<', '|('],
        'L': ['1', '7', '1_', '|', '|_', '#', 'l'],
        'M': ['^^', '|v|', '|\\/|', '/\\/\\', '(u)', '[]V[]', '(V)', '/|\\'],
        'N': ['//', '^/', '|\\|', '/\\/', '[\\]', '[]\\[]', 'n', '/V', '₪'],
        'O': ['0', '()', '?p,', ',', '*', 'ö'],
        'P': ['|^', '|*', '|o', '|^(o)', '|>', '|"', '9', '[]D', '|̊', '|7'],
        'Q': ['q', '(_,)'],
        'R': ['|2', 'P\\', '|?', '|^', 'lz', '[z', '12', 'Я'],
        'S': ['5', '$', 'z', '§', 'ehs'],
        'T': ['7', '+', '-|-', '1', ']['],
        'U': ['(_)', '|_|', 'v', 'ü'],
        'V': ['\\/'],
        'W': ['\\/', '\\/', 'vv', '//', '\\^/', '\\V/', '\\//', '\\X/',
              '\\|/'],
        'X': ['><', 'Ж', 'ecks ou )('],
        'Y': ['Y', 'j', '`/'],
        'Z': ['2', 'z', '~\\_', '~/_', '%']
    }

    palavra_convertida = ''

    for indice, item in enumerate(texto):
        if item in dicionario_leet:
            indice = random.randint(0, len(dicionario_leet[item]) - 1)
            palavra_convertida += dicionario_leet[item][indice]
        else:
            palavra_convertida += item

    return palavra_convertida


palavra = str(input('Informe a palavra a ser convertida para Leet Speak: '))
print(f'Palavra em Leet: {leet_speak_generator(unidecode(palavra.upper()))}')
