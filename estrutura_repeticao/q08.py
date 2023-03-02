a = []

for n in range(1, 6):
    a.append(int(input(f'informe o {n}º número: ')))

print(f'A soma de {a} é igual a {sum(a)}')
print(f'A média da soma de {a} é igual a {sum(a) / 5:.0f}')
