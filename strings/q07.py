from unidecode import unidecode


# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

def conta_espaco_vogais(string):
    palavra = unidecode(string.lower())
    print(f"Espaços em branco = {palavra.count(' ')}")
    print(f"Letra A = {palavra.count('a')}")
    print(f"Letra E = {palavra.count('e')}")
    print(f"Letra I = {palavra.count('i')}")
    print(f"Letra O = {palavra.count('o')}")
    print(f"Letra U = {palavra.count('u')}")


frase = str(input('Informe a string desejada: '))
conta_espaco_vogais(frase)
