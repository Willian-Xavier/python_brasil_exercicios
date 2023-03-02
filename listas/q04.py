# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

carac = []
consoante = []
cont_cons = 0

for c in range(10):
    carac.append(str(input(f'Informe o {c + 1}º caractere: ')))
    if carac[c] not in 'aeiou':
        cont_cons += 1
        consoante.append(carac[c])

print(consoante)
print(f'Quantidade de Consoantes: {cont_cons}')
