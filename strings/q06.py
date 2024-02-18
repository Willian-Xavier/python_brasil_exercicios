# Data por extenso. Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

def data_por_extenso(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    if int(data[0:2]) <= 31 and int(data[3:5]) <= 12 and int(data[6:10]) > 0:
        return (f'Você nasceu em {data[0:2]} de {meses[int(data[3:5]) - 1]}'
                f' de {data[6:10]}')
    else:
        return 'Data de nascimento inválida!'


data_nascimento = str(input('Informe a data DD/MM/AAAA: '))
print(data_por_extenso(data_nascimento))
