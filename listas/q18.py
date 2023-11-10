# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
# após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
# para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
# programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
# camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
# digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
# Após o final da votação, o programa deverá exibir:
#
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
# votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
# número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada
# jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de
# votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição
# das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
# programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no
# disco, obedecendo a mesma disposição apresentada na tela.


numero_jogador = list(range(1, 24))
qtde_votos_jogador = [0] * 23
melhor_jogador = [numero_jogador[0], qtde_votos_jogador[0]]


def calcula_percentual(num_votos_jogador, votos_total):
    return (num_votos_jogador / votos_total) * 100


print('Enquete: Quem foi o melhor jogador?\n')

while True:
    voto = int(input('Informe um número entre 1 e 23 ou digite 0 para sair: '))
    if 1 <= voto <= 23:
        qtde_votos_jogador[voto - 1] += 1
        continue
    elif voto != 0:
        print('Voto inválido! Digite novamente.')
        continue

    break

total_votos = sum(qtde_votos_jogador)

print('\n')
print('Resultado da votação:\n')
print(f'Foram computados {total_votos} votos.\n')
print('Jogador        Votos           %')
for i in range(len(numero_jogador)):
    if qtde_votos_jogador[i] > 0:
        print(f'{numero_jogador[i]:>4}{qtde_votos_jogador[i]:>14}'
              f'{calcula_percentual(qtde_votos_jogador[i], total_votos):16.2f}%')
    if qtde_votos_jogador[i] > melhor_jogador[1]:
        melhor_jogador[0] = numero_jogador[i]
        melhor_jogador[1] = qtde_votos_jogador[i]

print(f'O melhor jogador foi o número {melhor_jogador[0]}, com {melhor_jogador[1]} votos, correspondendo a '
      f'{calcula_percentual(melhor_jogador[1], total_votos):.2f}% do total de votos.')
