salario = float(input('Informe o salário do colaborador: '))

# Lógica 1

if salario <= 280:
    perc_aument = 20
    # valor_aumento = (salario * perc_aument) / 100
elif 280 < salario <= 700:
    perc_aument = 15
    # valor_aumento = (salario * perc_aument) / 100
elif 700 < salario <= 1500:
    perc_aument = 10
    # valor_aumento = (salario * perc_aument) / 100
else:
    perc_aument = 5
    # valor_aumento = (salario * perc_aument) / 100

valor_aumento = (salario * perc_aument) / 100
novo_sal = salario + valor_aumento

print('================= ORGANIZAÇÕES TABAJARA =================')
print(f'Salário antes do reajuste R${salario:.2f}')
print(f'O percentual de aumento aplicado foi de {perc_aument}%')
print(f'O valor do aumento foi de R${valor_aumento:.2f}')
print(f'O valor do novo salário é de R${novo_sal:.2f}')
print('=========================================================')

# Lógica 2

# if salario <= 280:
#     perc_aument = 20
#     valor_aumento = (salario * perc_aument) / 100
#     novo_sal = salario + valor_aumento
# elif 280 < salario <= 700:
#     perc_aument = 15
#     valor_aumento = (salario * perc_aument) / 100
#     novo_sal = salario + valor_aumento
# elif 700 < salario <= 1500:
#     perc_aument = 10
#     valor_aumento = (salario * perc_aument) / 100
#     novo_sal = salario + valor_aumento
# else:
#     perc_aument = 5
#     valor_aumento = (salario * perc_aument) / 100
#     novo_sal = salario + valor_aumento
