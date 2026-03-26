print('Digite dois valores inteiros')
x = int(input('Valor 1: '))
y = int(input('Valor 2: '))

maior = max(x, y)

if x == y:
    print('Números iguais')
else:
    print(f'Maior: {maior}')