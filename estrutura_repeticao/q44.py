# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero

voto = -1
jose = 0
joao = 0
maria = 0
ana = 0
voto_nulo = 0
voto_branco = 0
cont = 0

print('=' * 20, 'CANDIDATOS', '=' * 20)
print('1 - Jose')
print('2 - João')
print('3 - Maria')
print('4 - Ana')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('0 - Encerrar')
print('=' * 52)

while voto < 0 or voto > 6:
    voto = int(input('Informe o número do candidato que deseja votar: '))
    if voto < 0 or voto > 6:
        print('Voto Inválido\nDigite Novamente!')
    elif voto == 0:
        print('Votação Encerrada!')
        
    if voto == 1:
        jose += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        ana += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1
    
    if voto != 0:
        cont += 1
        voto = -1
               
print('=' * 23, 'TOTAL DE VOTOS', '=' * 23)
print(f'Votos José = {jose}')
print(f'Votos João = {joao}')
print(f'Maria = {maria}')
print(f'Ana = {ana}')
print(f'Nulos = {voto_nulo}')
print(f'Brancos = {voto_branco}')
print(f'Porcentagem de votos nulos sobre o total de votos = {(voto_nulo / cont) * 100:.2f}%')
print(f'Porcentagem de votos brancos sobre o total de votos = {(voto_branco / cont) * 100:.2f}%')
print('=' * 62)  

# while voto != 1 and voto != 2 or voto != 3 or voto != 4 or voto != 5 or voto != 6 or voto != 0:
#     voto = int(input('Informe o número do candidato que deseja votar: '))
#     if voto != 1 or voto != 2 or voto != 3 or voto != 4 or voto != 5 or voto != 6 or voto != 0: