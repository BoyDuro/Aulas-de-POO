print('Digite 3 valores:')
x = int(input('Valor 1: '))
y = int(input('Valor 2: '))
z = int(input('Valor 3: '))

Valores = [x, y, z]
MaiorValor = max(Valores)
MenorValor = min(Valores)
if Valores[0] > MenorValor and Valores[0] < MaiorValor:
    Valores[0] = Valores[1]
elif Valores[1] > MenorValor and Valores[1] < MaiorValor:
    Valores[1] = Valores[1]
elif Valores[2] > MenorValor and Valores[2] < MaiorValor:
    Valores[2] = Valores[1]

Valores[0] = MenorValor
Valores[2] = MaiorValor

print(Valores)