temp = 99
maior = 0
menor = 2000
soma_temp = 0
cont = 0

while temp <= 100:
    temp = float(input('Informe a temperatura: Digite um valor acima de 100 para encerrar: '))

    if temp > maior and temp <= 100:
        maior = temp
    elif temp < menor:
        menor = temp
    
    if temp <= 100:
        soma_temp += temp
        cont += 1
    
print(f'Maior temperatura: {maior:.2f}°')
print(f'Menor temperatura: {menor:.2f}°')
print(f'A média das temperaturas é de {soma_temp / (cont):.2f}°')
    