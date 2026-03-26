print('Digite uma sequência de números separados por vírgula:')
numeros = input('Digite: ')

valores = numeros.split(',')
soma = 0

for b in valores:
    valor = int(b)
    soma = soma + valor

print(f'Soma = {soma}')