nome_usuario = ''
senha = ''

while nome_usuario == senha:
    nome_usuario = str(input('Informe o nome do usuário: '))
    senha = str(input('Informe a senha: '))
    
    if nome_usuario == senha:
        print('O nome de usuário não pode ser igual a senha!\nDigite Novamente!')
