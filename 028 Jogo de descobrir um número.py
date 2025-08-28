#028 Jogo de descobrir um número
from random import randint as d
n1 = d(0 , 5)
n2 = int(input('Digite um número de 0 a 5: '))
if n1 == n2:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número que eu pensava era: ', n1)