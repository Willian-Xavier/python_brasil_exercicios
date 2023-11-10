# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

num = 0
valores = []
qtde_valores_acima_media = 0
qtde_valores_abaixo_sete = 0

while num != -1:
    num = int(input('Informe um número positivo ou digite -1 para encerrar: '))
    if num != -1:
        valores.append(num)

print(f'Quantidade de valores lidos: {len(valores)}')
print(f'Valores lidos na ordem informada: {valores}')
print(f'Valores lidos na ordem inversa: {valores[::-1]}')
print(f'Soma dos valores: {sum(valores)}')

media = sum(valores) / len(valores)

print(f'Média dos valores: {media:.2f}')

for valor_ind in valores:
    if valor_ind > media:
        qtde_valores_acima_media += 1
    if valor_ind < 7:
        qtde_valores_abaixo_sete += 1

print(f'Quantidade de valores acima da média: {qtde_valores_acima_media}')
print(f'Quantidade de valores abaixo de 7: {qtde_valores_abaixo_sete}')
print('Programa encerrado!')
