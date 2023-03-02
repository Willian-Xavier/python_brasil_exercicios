import math

num = int(input('Informe um número inteiro: '))

divisoes = 0
# raiz = num ** (0.5)
raiz = int(math.sqrt(num))

# for i in range(2, num // 2 + 1):  # reduz pela metade o número de cálculos feitos, já que não existe nenhum divisor que seja maior do que a metade do número e menor do que ele mesmo
for i in range(2, raiz + 1):
    if (num % i == 0):
        divisoes += 1
        
if divisoes == 0 and num > 1:
    print(f'{num} é um número primo!')
else:
    print(f'{num} não é um número primo!')
        