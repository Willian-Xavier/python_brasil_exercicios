# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo. 

num = 0
inter_0_25 = 0
inter_26_50 = 0
inter_51_75 = 0
inter_76_100 = 0

while num >= 0:
    num = int(input('Informe um número: Digite um número negativo para encerrar: '))

    if 0 <= num <= 25:
        inter_0_25 += 1
    elif 26 <= num <= 50:
        inter_26_50 += 1
    elif 51 <= num <= 75:
        inter_51_75 += 1
    elif 76 <= num <= 100:
        inter_76_100 += 1

print(f'Números no intervalor de 0 a 25: {inter_0_25}')
print(f'Números no intervalor de 26 a 50: {inter_26_50}')
print(f'Números no intervalor de 51 a 75: {inter_51_75}')
print(f'Números no intervalor de 76 a 100: {inter_76_100}')
