letra = str(input('Informe o sexo: M - Masculino / F - Feminino: ')).upper()

# Lógica 1

if letra == 'M':
    print('Sexo Masculino!')
elif letra == 'F':
    print('Sexo Feminino!')
else:
    print('Sexo Inválido!')
    

# Lógica 2 OBS: Nesse caso, não é necessário utilizar o upper() na entrada de dados

# if letra == 'M' or letra == 'm':
#     print('Sexo Masculino!')
# elif letra == 'F' or letra == 'f':
#     print('Sexo Feminino!')
# else:
#     print('Sexo Inválido!')
