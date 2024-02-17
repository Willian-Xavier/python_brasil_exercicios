# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela
# por extenso.

def numero_extenso(numero):
    numeros = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
               'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte', 'Trinta',
               'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa']

    if numero <= 20:
        return numeros[numero]
    elif str(numero)[1:2] == '0':
        return f'{numeros[20 + (int(str(numero)[0:1]) - 2)]}'
    else:
        return f'{numeros[20 + (int(str(numero)[0:1]) - 2)]} e {numeros[int(str(numero)[1:2])]}'


num = -1

while num < 0 or num > 99:
    num = int(input('Informe um número de 0 a 99: '))

print(numero_extenso(num))
