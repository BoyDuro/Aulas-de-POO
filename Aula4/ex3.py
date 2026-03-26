print('Digite uma frase:')
frase = input('Frase: ')

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

soma = 0

for coisa in frase:
    if coisa in numeros:
        coisa2 = int(coisa)
        soma = soma + coisa2
print(soma)