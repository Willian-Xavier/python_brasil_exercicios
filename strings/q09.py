import re


# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de
# formatação.


def valida_cpf(cpf):
    if len(cpf) < 14 or len(cpf) > 14 and cpf[3:4] != '.' and cpf[7:8] != '.' and cpf[11:12] != '-':
        return f'CPF inválido!'
    else:
        cpf_numeros = ''.join(re.split("""[ .-]""", cpf))
        fator = 10
        total_soma_digitos = 0
        for digito in cpf_numeros[:9]:
            total_soma_digitos += int(digito) * fator
            fator -= 1

        digito_verificador_1 = (total_soma_digitos * 10) % 11

        if digito_verificador_1 == 10:
            digito_verificador_1 = 0

        if digito_verificador_1 == int(cpf[12:13]):
            fator = 11
            total_soma_digitos = 0
            for digito in cpf_numeros[:10]:
                total_soma_digitos += int(digito) * fator
                fator -= 1

            digito_verificador_2 = (total_soma_digitos * 10) % 11

            if digito_verificador_2 == int(cpf[13:]):
                return f'CPF Válido!'
            else:
                return f'CPF Inválido!'
        else:
            return f'CPF Inválido!'


numero_cpf = str(input('Informe o número do CPF em formato XXX.XXX.XXX-XX: '))
print(valida_cpf(numero_cpf))
