# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado
# durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de
# quanto será gasto com o pagamento deste abono.
#
# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
# chegou-se a seguinte forma de cálculo:
#
# a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais,
# isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter
# nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
# salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do
# abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
# Os valores podem mudar a cada execução do programa.

salario = []
abono = []
qtde_colab_valor_min = 0


def calcula_abono(salarios):
    valores_abono = []

    for vlr_salario in salarios:
        valor = (vlr_salario * 20) / 100

        if valor > 100:
            valores_abono.append(valor)
        else:
            valores_abono.append(100)

    return valores_abono


print('Projeção de Gastos com Abono')
print('============================')
while True:
    valor_salario = int(input('Informe o valor do salário ou digite 0 para encerrar: '))
    if valor_salario > 0:
        salario.append(valor_salario)
        continue
    elif valor_salario < 0:
        print('Salário inválido! Digite novamente!')
    else:
        break

abono = calcula_abono(salario)

print('Salário   -   Abono\n')
for qtde in range(len(salario)):
    print(f'R${salario[qtde]:>7.2f} - R${abono[qtde]:.2f}')
    if abono[qtde] <= 100:
        qtde_colab_valor_min += 1

print(f'\n\nForam processados {len(salario)} colaboradores')
print(f'Total gasto com abonos: R${sum(abono):.2f}')
print(f'Valor mínimo pago a {qtde_colab_valor_min} colaboradores')
print(f'Maior valor de abono pago: R${max(abono):.2f}')
