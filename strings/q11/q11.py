# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!
from random import choice


def extrai_palavras():
    with open('palavras.txt', mode='r') as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras
    # Esta função lê um arquivo chamado ‘palavras.txt’ e retorna uma lista de palavras. A função splitlines()
    # é usada para dividir o conteúdo do arquivo em linhas, criando uma lista onde cada palavra é um item separado.


def jogo_forca():
    palavra_sorteada = choice(extrai_palavras())
    palavra_oculta = ['_' for _ in palavra_sorteada]
    tentativas = 6

    # Primeiro, é escolhida uma palavra aleatória da lista de palavras usando a função choice().Em seguida, cria-se uma
    # versão oculta da palavra, substituindo todas as letras por ‘_’.A variável tentativas é inicializada com 6,
    # representando o número de tentativas que o jogador tem antes de ser “enforcado”.

    while tentativas > 0 and '_' in palavra_oculta:
        print(' '.join(palavra_oculta))
        letra = input('\nDigite uma letra: ')
        if letra in palavra_sorteada:
            for indice, letra_palavra in enumerate(palavra_sorteada):
                if letra_palavra == letra:
                    palavra_oculta[indice] = letra
        else:
            tentativas -= 1
            print(f'Você errou pela {6 - tentativas}ª vez. Tente de novo!\n')
            # Se a letra adivinhada estiver na palavra, todas as ocorrências dessa letra na palavra_oculta são
            # reveladas.Se a letra não estiver na palavra, será exibida mensagens informando a quantidade de tentativas
            # restantes

    # No loop while, enquanto o jogador ainda tem tentativas e a palavra não foi completamente advinhada, o jogo
    # continua

    if '_' not in palavra_oculta:
        return f'Parabéns, você ganhou!'
    else:
        return f'Você perdeu. A palavra era {palavra_sorteada}'


print(jogo_forca())
