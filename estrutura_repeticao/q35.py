num = int(input('Informe um número inteiro: '))

# lista_numeros = list(range(2, num + 1)) # list recebe como parâmetro um valor inicial e outro final e utiliza os números nesse alcance
lista = []
divisoes = 0

for n in range(2, num):
    for i in lista:
        if (n % i == 0):
            divisoes += 1
            
    if divisoes == 0:
        lista.append(n)
        
    divisoes = 0
        
print(f'Primos: {lista}')
