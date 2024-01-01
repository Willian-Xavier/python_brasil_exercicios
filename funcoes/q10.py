# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
# entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
# primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
# este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,
# no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random


def lancador_dados():
    dado_1 = sum(random.sample(range(1, 7), 1))
    dado_2 = sum(random.sample(range(1, 7), 1))

    print(f'Dados lançados na rodada: {dado_1} + {dado_2} = {dado_1 + dado_2}')
    return dado_1 + dado_2


primeiro_lancamento = lancador_dados()

if primeiro_lancamento == 7 or primeiro_lancamento == 11:
    print('Você ganhou!')
elif primeiro_lancamento == 2 or primeiro_lancamento == 3 or primeiro_lancamento == 12:
    print('Você perdeu!')
else:
    print(f'A pontuação de referência é {primeiro_lancamento}.')
    while True:
        lancamento = lancador_dados()
        if lancamento == 7:
            print('Você perdeu!')
            break
        elif lancamento == primeiro_lancamento:
            print('Você ganhou!')
            break
