# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

num = []

for n in range(0, 10):
    num.append(int(input(f'Informe o {n + 1}º número: ')))

print(list(reversed(num)))

# o método reversed() não altera a ordem dos valores da variável num

# When using the reversed() method with these objects, we need to use the list() method
# to convert the output from the reversed() method to a list.


# num = []
#
# for n in range(0, 10):
#     num.append(int(input(f'Informe o {n + 1}º número: ')))
#
# num.reverse()
# print(num)

# o método reverse() altera a ordem dos valores dentro da variável
