from unidecode import unidecode
import re


# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palindromo(string):
    nova_frase = ''.join(re.split("""[ .:"'!,-]""", unidecode(string.lower())))
    if nova_frase == nova_frase[::-1]:
        return f'É um palíndromo!'
    else:
        return f'Não é um palíndromo!'


frase_palavra = str(input('Informe a palavra ou frase que deseja identificar como palíndromo: '))
print(palindromo(frase_palavra))
