valor_hora = float(input('Informe o valor da hora trabalhada: '))
qtde_horas_trab = float(input('Informe a quantidade de horas trabalhadas no mês: '))

sal_bruto = valor_hora * qtde_horas_trab

if 900 < sal_bruto <= 1500:
    per_imp_renda = 5
    # desc_imp_renda = (sal_bruto * per_imp_renda) / 100
elif 1500 < sal_bruto <= 2500:
    per_imp_renda = 10
    # desc_imp_renda = (sal_bruto * per_imp_renda) / 100
else:
    per_imp_renda = 20
    # desc_imp_renda = (sal_bruto * per_imp_renda) / 100

imp_sind = (sal_bruto * 3) / 100
fgts = (sal_bruto * 11) / 100
inss = (sal_bruto * 10) / 100
desc_imp_renda = (sal_bruto * per_imp_renda) / 100

print('============================= CONTRACHEQUE =============================')
print(f'Salário bruto = {valor_hora:.2f} * {qtde_horas_trab:.2f} = R${sal_bruto:.2f}')
if sal_bruto <= 900:
    print('IR = ISENTO')
else:
    print(f'Percentual de desconto do IR {per_imp_renda}%. Valor do desconto = R${desc_imp_renda:.2f}')
print(f'Desconto do INSS (10%) = R${inss:.2f}')
print(f'FGTS (11%) = R${fgts:.2f}')
print(f'Imposto Sindical = R${imp_sind:.2f}')
if sal_bruto <= 900:
    print(f'Total de descontos = R${imp_sind + inss:.2f}')
    print(f'Salário líquido = R${sal_bruto - imp_sind - inss:.2f}')
else:
    print(f'Total de descontos = R${desc_imp_renda + imp_sind + inss:.2f}')
    print(f'Salário líquido = R${sal_bruto - desc_imp_renda - imp_sind - inss:.2f}')
print('========================================================================')
