# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
# soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de
# 1 a 9 parece ser mais simples que usar uma matriz 3x3.


def quadrado_magico(vetor):
    if vetor[0] + vetor[1] + vetor[2] == 15 and vetor[3] + vetor[4] + vetor[5] == 15 and vetor[6] + vetor[7] + vetor[
        8] == 15 and vetor[0] + vetor[3] + vetor[6] == 15 and vetor[1] + vetor[4] + vetor[7] == 15 and vetor[2] + vetor[
        5] + vetor[8] == 15 and vetor[0] + vetor[4] + vetor[8] == 15 and vetor[2] + vetor[4] + vetor[6] == 15:
        return True
    else:
        return False


vetor = [8, 3, 5, 1, 5, 9, 6, 7, 2]

print(quadrado_magico(vetor))
