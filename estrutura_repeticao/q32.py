p = 0
num = []

while p <= 10:
    num.append(int(input('Digite um número: ')))
    p += 1

maior_valor_1 = 0
maior_valor_2 = 0

for n in range(len(num)):
    if num[n] >= maior_valor_1:
        maior_valor_1 = num[n]
        
    if num[n] >= maior_valor_2 and num[n] < maior_valor_1:
        maior_valor_2 = num[n]

print(f'Primeiro maior valor: {maior_valor_1}')
print(f'Segundo maior valor: {maior_valor_2}')
