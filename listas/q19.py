# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
# organizações:
#
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
#
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
# aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
# armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
# cada um dos concorrentes e informar o vencedor da enquete.
import random

opcoes = [0] * 6
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']


def calcula_porcentagem(quantidade_votos, votos_total):
    if votos_total > 0:
        return (quantidade_votos / votos_total) * 100

    return 0


# LOOP FOR PARA GERAR ENTRADAS COM VALORES ALEATÓRIOS PARA TESTES
# for aleatorio in range(1, 501):
#     opcoes[random.randrange(1, 7) - 1] += 1

while True:
    print('Qual o melhor Sistema Operacional para uso em servidores?\n')
    print('As possíveis respostas são:\n')
    for i in range(len(sistemas)):
        print(f'{i + 1} - {sistemas[i]}')

    print('0 - Sair')

    voto = int(input('Informe a opção desejada: '))
    print('\n')

    if 1 <= voto <= 6:
        opcoes[voto - 1] += 1
        continue
    elif voto != 0:
        print('Opção inválida! Digite Novamente!\n\n')
        continue

    break

total_votos = sum(opcoes)

print('Sistema Operacional      Votos       %')
print('-------------------      -----       ---')
print(f'Windows Server{opcoes[0]:>16}{calcula_porcentagem(opcoes[0], total_votos):11.1f}%')
print(f'Unix{opcoes[1]:>26}{calcula_porcentagem(opcoes[1], total_votos):11.1f}%')
print(f'Linux{opcoes[2]:>25}{calcula_porcentagem(opcoes[2], total_votos):11.1f}%')
print(f'Netware{opcoes[3]:>23}{calcula_porcentagem(opcoes[3], total_votos):11.1f}%')
print(f'Mac OS{opcoes[4]:>24}{calcula_porcentagem(opcoes[4], total_votos):11.1f}%')
print(f'Outro{opcoes[5]:>25}{calcula_porcentagem(opcoes[5], total_votos):11.1f}%')
print('-------------------      -----       ---')
print(f'Total{total_votos:>25}\n')
print(f'O Sistema Operacional mais votado foi o {sistemas[opcoes.index(max(opcoes))]}, '
      f'com {opcoes[opcoes.index(max(opcoes))]} votos, correspondendo '
      f'a {calcula_porcentagem(opcoes[opcoes.index(max(opcoes))], total_votos):.1f}% dos votos.')
