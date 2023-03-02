nota = 0
soma_nota = 0
cont = 0

while nota >= 0:
    nota = float(input('Informe a primeira nota: Digite uma nota negativa para encerrar: '))

    if (nota >= 0):
        soma_nota += nota
        
        cont += 1
    
print(f'A média aritmética da turma é de {soma_nota / cont:.2f}')
