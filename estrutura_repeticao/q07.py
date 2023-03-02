numeros = []

for num in range(1, 6):
    numeros.append(int(input(f'Informe o {num}º número: ')))

maior_numero = numeros[0]
i = 0

while i < len(numeros):
    if numeros[i] > maior_numero:
        maior_numero = numeros[i]
    i += 1
        
print(f'O maior entre os números {numeros} é o {maior_numero}')    
    