num = (32, 33, 39, 44, 51, 53, 55, 17, 22, 4, 20, 60)
# A lista pode ser feita tanto utilizando uma matriz quanto tuples

print(f'O menor número da lista é o {min(num)}')
print(f'O maior número da lista é o {max(num)}')
print(f'A soma dos números é igual a {sum(num)}')

# maior = 0
# menor = 10000000000000000000000000000000000000000000000000000000000
# i = 0

# while i < len(num):
#     if num[i] > maior:
#         maior = num[i]
#     elif num[i] < menor:
#         menor = num[i]

#     i += 1
    
# print(f'O maior número é o {maior}')
# print(f'O menor número é o {menor}')

# Repetição com entrada de dados pelo usuário

# valores = []
# num = 0
# maior = 0
# menor = 10000000000000000000000000000000000000000000000000000000000
# i = 0

# while num != -1:
#     num = int(input(f'Informe um número: '))
#     valores.append(num)
    
# while i < len(valores):
#     if valores[i] > maior:
#         maior = valores[i]
#     elif valores[i] < menor and valores[i] > 0:
#         menor = valores[i]
    
#     i += 1
        
# print(f'O maior número é o {maior}')
# print(f'O menor número é o {menor}')
