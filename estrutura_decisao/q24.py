num_1 = float(input('Informe um número: '))
num_2 = float(input('Informe outro número: '))

print('================ MENU DE OPÇÕES ================')
print('||  1 - Par ou ímpar                          ||')
print('||  2 - Positivo ou negativo                  ||')
print('||  3 - Inteiro ou decimal                    ||')
print('================================================')
op = int(input('Escolha uma das opções acima: '))

if op == 1 or op == 2 or op == 3:
    if op == 1:    #verificador de opção
        if num_1 % 2 == 0:
            print(f'{num_1:.0f} é um número par!')
        elif num_1 % 2 == 1:
            print(f'{num_1:.0f} é um número ímpar!')
        else:
            print('Não é possível determinar se um número decimal é par ou ímpar!')
            
        if num_2 % 2 == 0:
            print(f'{num_2:.0f} é um número par!')
        elif num_2 % 2 == 1:
            print(f'{num_2:.0f} é um número ímpar!')
        else:
            print('Não é possível determinar se um número decimal é par ou ímpar!')
    elif op == 2:  #verificador de opção
        if num_1 >= 0:
            print(f'O número {num_1} é um número positivo!')
        else:
            print(f'O número {num_1} é um número negativo!')
            
        if num_2 >= 0:
            print(f'O número {num_2} é um número positivo!')
        else:
            print(f'O número {num_2} é um número negativo!')       
    elif op == 3:  #verificador de opção
        if num_1 == round(num_1):
            print(f'O número {num_1:.0f} é um número inteiro!')
        else:
            print(f'O número {num_1} é um número decimal!')
            
        if num_2 == round(num_2):
            print(f'O número {num_2:.0f} é um número inteiro!')
        else:
            print(f'O número {num_2} é um número decimal!')
else:
    print('Opção Inválida!')
    