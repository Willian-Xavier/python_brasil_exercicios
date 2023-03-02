turno = str(input('Informe em qual turno você estuda: M - Matutino / V - Vespertino / N - Noturno: ')).upper()

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

# Lógica 2 (Nesse caso, a entrada do dado sobre o turno não possui a função .upper()

# if turno == 'M' or turno == 'm':
#     print('Bom Dia!')
# elif turno == 'V' or turno == 'v':
#     print('Boa Tarde!')
# elif turno == 'N' or turno == 'n':
#     print('Boa Noite!')
# else:
#     print('Valor Inválido!')
