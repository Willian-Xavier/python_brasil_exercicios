data = str(input('Informe uma data no formato DD/MM/AAAA: '))

# Lógica 1

if data[2] == '/' and data[5] == '/' and data[:2].isnumeric() and data[3:5].isnumeric() and data[6:].isnumeric() and \
        len(data) == 10:
    print('Data válida!')
else:
    print('Data Inválida!')

# Lógica 2

# indexador_1 = data.find('/', 0, 3)
# indexador_2 = data.find('/', 5, 6)

# if indexador_1 == 2 and indexador_2 == 5:
#     print('Data válida!')
# else:
#     print('Data Inválida!')

# Lógica 3

# if data.find('/', 0, 3) == 2 and data.find('/', 5, 6) == 5:
#     print('Data válida!')
# else:
#     print('Data Inválida!')
