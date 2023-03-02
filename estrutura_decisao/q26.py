tipo = 0
litros = 0
desconto = 0
preco_total = 0

while 1 != tipo != 2:
    print('=============== TIPOS DE COMBUSTÍVEIS ===============')
    print('1 - Álcool - Preço R$1,90/litro')
    print('2 - Gasolina - Preço R$2,50/litro')
    print('=====================================================')
    tipo = int(input('Informe o tipo de combustível desejado: '))
    if 1 != tipo != 2:
        print('Tipo Inválido!\nDigite Novamente!')
    
litros = int(input('Informe a quantidade de litros desejados: '))

if tipo == 1 and litros <= 20:
    desconto = ((1.90 * litros) * 3) / 100
elif tipo == 1 and litros > 20:
    desconto = ((1.90 * litros) * 5) / 100
elif tipo == 2 and litros <= 20:
    desconto = ((2.50 * litros) * 4) / 100
else:
    desconto = ((2.50 * litros) * 6) / 100

if tipo == 1:
    print(f'Preço Total: R${1.90 * litros - desconto:.2f}')
else:
    print(f'Preço Total: R${2.50 * litros - desconto:.2f}')
    