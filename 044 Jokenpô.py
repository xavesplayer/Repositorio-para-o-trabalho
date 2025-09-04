#044 Jokenpô
from random import randint
from time import sleep
lista = ('pedra', 'papel', 'tesoura')
print ('''Escolha pelo número: 
1) Pedra 
2) Papel 
3) Tesoura ''')
user = int(input('Digite o número: '))
userc = lista[user - 1]
pc = lista[randint(0, 2)]
print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)
if userc == pc:
    print('Empatamos, somos abestados!')
elif(userc == 'pedra' and pc == 'tesoura') or \
    (userc == 'tesoura' and pc == 'papel') or \
    (userc == 'papel' and pc == 'pedra'):
        print(f'Você ganhou abestado! Eu escolhi {pc}, abestado :D')
else:
    print(f'Eu ganhei! escolhi {pc}')

