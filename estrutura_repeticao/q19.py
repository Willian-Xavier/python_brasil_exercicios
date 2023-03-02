valores = []
num = 0
maior = 0
menor = 10000000000000000000000000000000000000000000000000000000000
i = 0

while 0 <= num <= 1000:
    num = int(input(f'Informe um número entre 0 e 1000: Digite outro valor para encerrar: '))

    if 0 <= num <= 1000:
        valores.append(num)
else:
    while i < len(valores):
        if valores[i] > maior:
            maior = valores[i]
        elif valores[i] < menor:
            menor = valores[i]
        
        i += 1
         
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
