x = int(input('Escreva num 1: '))
y = int(input('Escreva num 2: '))
z = int(input('Escreva num 3: '))
a = int(input('Escreva num 4: '))

lista = [x, y, z, a]

soma_pares = 0
soma_impares = 0

for coisa in lista:
    if coisa % 2 == 0:
        soma_pares = soma_pares + coisa
    if coisa % 2 != 0:
        soma_impares = soma_impares + coisa

print(soma_pares, soma_impares)