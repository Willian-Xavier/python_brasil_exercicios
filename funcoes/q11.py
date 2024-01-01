# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


def retornar_mes_extenso(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']

    mes = data[3:5]

    if (1 > int(data[0:2]) > 31) or (1 > int(data[3:5]) > 12) or (int(data[6:10]) < 1):
        return None
    return f'{data[0:2]} de {meses[int(mes) - 1]} de {data[6:10]}.'


data = str(input('Informe uma data no formato DD/MM/AAAA: '))
print(retornar_mes_extenso(data))
