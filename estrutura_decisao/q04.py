letra = str(input('Digite uma letra: ')).upper()


# Variável opcional, que pode ser utilizada como lista para a estrutura de decisão "if"
# vogais = ['A', 'E', 'I', 'O', 'U']

if letra in ('A', 'E', 'I', 'O', 'U'):
    print(f'''A letra '{letra}' é uma vogal!''')
else:
    print(f'''A letra '{letra}' é uma consoante!''')