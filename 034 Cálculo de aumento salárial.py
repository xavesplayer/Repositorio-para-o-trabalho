#034 Cálculo de aumento salárial
salario = float(input(f'Digite seu salário atual: '))
if salario > 1250.00:
    print(f'Seu aumento será de: R${salario * 0.1:.2f} \nSeu novo salário será de R${salario + (salario * 0.1):.2f}')
else:
    print(f'Seu aumento será de: R${salario * 0.15:.2f} \nSeu novo salário será de R${salario + (salario * 0.15)}')