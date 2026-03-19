x = input('Digite uma data no formato dd/mm/aaaa: ')

data = x.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

bissexto = ano % 4 == 0 and ano % 100 != 0

dias_m = 31
if mes in [4, 6, 9, 11]:
    dias_m = 30
elif mes == 2:
    if bissexto == True:
        dias_m = 29
    else:
        dias_m = 28

if dia >= 1 and dia <= dias_m and mes <= 12 and ano >= 1900 and ano <= 2100:
    print('A data informada é válida')
else:
    print('A data informada é inválida')