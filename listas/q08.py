# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for info in range(5):
    idade.append(int(input(f'Informe a idade da {info + 1}ª pessoa: ')))
    altura.append(float(input(f'Informea altura da {info + 1}ª pessoa: ')))

for ida, alt in zip(reversed(idade), reversed(altura)):
    print(f'{ida} - {alt}')

# idade.reverse()
# altura.reverse()
#
# for i in range(len(idade)):
#     print(f'{idade[i]} - {altura[i]}')
