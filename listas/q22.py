# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um
# levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
# encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
# indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a
# zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
import random

lista_defeitos = ['Necessita da esfera', 'Necessita de limpeza', 'Necessita troca do cabo ou conector',
                  'Quebrado ou inutilizado']
contador_defeitos = [0] * 4


def calcula_percentual(frequencia_defeitos, quantidade_entradas):
    if quantidade_entradas > 0:
        return (frequencia_defeitos / quantidade_entradas) * 100

    return 0


# LOOP FOR PARA GERAR ENTRADAS COM VALORES ALEATÓRIOS PARA TESTES
# for aleatorio in range(1, 201):
#     contador_defeitos[random.randrange(1, 5) - 1] += 1
#     print('\n')

while True:
    print('Lista de defeitos')
    for defeito in range(len(lista_defeitos)):
        print(f'{defeito + 1} - {lista_defeitos[defeito]}')

    opcao = int(input('Informe a opção desejada: '))
    if opcao == 0:
        break
    elif opcao < 1 or opcao > 4:
        print('Opção Inválida! Digite novamente!\n')
        continue
    contador_defeitos[opcao - 1] += 1
    print('\n')

print('\n\nSituação                             Defeito                   Percentual')
print('=' * 73)
for exibicao in range(len(lista_defeitos)):
    print(f'{lista_defeitos[exibicao]:<35} {contador_defeitos[exibicao]:>8} '
          f'{calcula_percentual(contador_defeitos[exibicao], sum(contador_defeitos)):>27.0f}%')
print('=' * 73)
