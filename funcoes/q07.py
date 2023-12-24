# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para
# a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro
# valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o
# programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
# pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor
# da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valor_pagamento(prestacao, atraso):
    multa_atraso = 3
    juros_atraso = 0.01
    if not atraso:
        return prestacao

    return prestacao + (prestacao * multa_atraso * juros_atraso * atraso)


valor_total_dia = 0
quantidade_prestacoes = 0

while True:
    valor_prestacao = float(input('Informe o valor da prestação ou digite 0 para sair: '))
    if not valor_prestacao:
        break
    dias_atraso = int(input('Informe a quantidade de dias de atraso: '))
    valor_parcela = valor_pagamento(valor_prestacao, dias_atraso)
    valor_total_dia += valor_parcela
    print(f'Valor da parcela com os juros é de R${valor_parcela:.2f}')
    quantidade_prestacoes += 1

print('-' * 55)
print(f'Quantidade de prestações pagas no dia: {quantidade_prestacoes}')
print(f'Valor total das prestações pagas: R${valor_total_dia:.2f}')
print('-' * 55)
