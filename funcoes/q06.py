# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve
# converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
# a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que
# permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converter_notacao_hora(horas, minutos):
    if 0 <= horas < 12:
        if 0 < horas < 10 or horas == 0:
            return f'0{horas}:{minutos}A.M.'

        return f'{horas}:{minutos}A.M.'
    elif horas == 12:
        return f'{horas}:{minutos}P.M.'
    else:
        return f'{horas - 12}:{minutos}P.M.'


while True:
    hora = int(input('Informe a hora ou digite um valor negativo para encerrar: '))
    if hora < 0:
        break
    minuto = int(input('Informe os minutos: '))
    print(converter_notacao_hora(hora, minuto))
