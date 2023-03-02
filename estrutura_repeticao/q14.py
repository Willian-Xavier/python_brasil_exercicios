num = 0
par = 0
impar = 0

for n in range(1, 11):
    num = int(input(f'Informe o {n}º número: '))
    
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
     
print(f'Quantidade números pares: {par}')
print(f'Quantidade números ímpares: {impar}')

# Armazenar números pares e ímpares

# num = []
# par = []
# impar = []
# i = 0

# for n in range(1, 11):
#     num.append(int(input(f'Informe o {n}º número: ')))
    
# while i < len(num): 
#     if num[i] % 2 == 0:
#         par.append(num[i])
#     else:
#         impar.append(num[i])

#     i += 1
    
# Utilizando for
    
# for i in range (len(num)): 
#     if num[i] % 2 == 0:
#         par.append(num[i])
#     else:
#         impar.append(num[i])
     
# print(f'Números pares: {sorted(par)}')
# print(f'Números ímpares: {sorted(impar)}')
