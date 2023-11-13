# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
# identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
# o seguinte arquivo, chamado "usuarios.txt":
#
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
# um relatório, chamado "relatório.txt", no seguinte formato:
#
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
# a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
# através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também
# deverá ser feito através de uma função, que será chamada pelo programa principal.
import math

usuarios = ['Alexandre', 'Anderson', 'Antonio', 'Carlos', 'Cesar', 'Rosemary']
uso_disco = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]


def converter_mebibyte(bytes):
    return bytes * (1 / math.pow(1024, 2))


def calcula_porcentagem_uso(uso, espaco_total_ocupado):
    if uso > 0:
        return (uso / espaco_total_ocupado) * 100

    return 0


uso_total_disco = sum(uso_disco) * (1 / math.pow(1024, 2))

print('ACME Inc.            Uso do espaço em disco pelos usuários')
print('-' * 58)
print('Nr.   Usuário        Espaço Utilizado        % do Uso')
for itera in range(len(usuarios)):
    tamanho_uso = converter_mebibyte(uso_disco[itera])
    print(f'{itera + 1:<6}{usuarios[itera]:<15} {tamanho_uso:>12.2f} MB '
          f'{calcula_porcentagem_uso(tamanho_uso, uso_total_disco):>14.2f}%')

print('-' * 58)
print(f'Espaço total ocupado: {uso_total_disco:.2f} MB')
print(f'Espaço médio ocupado: {uso_total_disco / 6:.2f} MB')
