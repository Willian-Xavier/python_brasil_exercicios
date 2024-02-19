# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O
# programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
# aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou
# ou perdeu o jogo.
import random
from random import choice


def escolhe_palavra():
    with open('palavras.txt', mode='r') as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras


def advinhar_palavra():
    palavra_sorteada = choice(escolhe_palavra())
    palavra_embaralhada = "".join(
        random.sample(palavra_sorteada, len(palavra_sorteada)))

    tentativas = 6

    while tentativas > 0:
        print(f'Palavra embaralhada: {palavra_embaralhada}')
        palavra = str(input('Informe a palavra: '))
        if palavra == palavra_sorteada:
            return 'Parabéns, você ganhou!'
        else:
            tentativas -= 1
            print(f'Você errou pela {6 - tentativas}ª vez. Tente de novo!\n')

    return f'Você perdeu. A palavra era {palavra_sorteada}'


print(advinhar_palavra())
