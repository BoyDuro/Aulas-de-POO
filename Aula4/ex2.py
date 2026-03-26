print('Digite dois valores inteiros separados por um operador +, -, * ou /')
valores = input('Escreva: ')

for b in valores:
    if b == '+' or b == '-' or b == '*' or b == '/':
        calc = b
pos = valores.find(calc)
numero1 = int(valores[:pos])
numero2 = int(valores[pos:])

match calc:
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        resultado = numero1 / numero2

print(f'O resultado da operação é {resultado}')