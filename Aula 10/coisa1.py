from datetime import datetime

d = datetime.strptime(input('Informe uma data: '), '%d/%m/%Y')
print(d)
print(d.strftime('%d/%m/%Y'))