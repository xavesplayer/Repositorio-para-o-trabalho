#018 Sen, Cos, Tang, Rad
import math
a1 = float(input("Digite um ângulo: "))
sn = math.sin(a1)
cs = math.cos(a1)
tg = math.tan(a1)
rs = math.radians(a1)
print ("--" * 22)
print (f"O seno é: \033[31m{sn:.2f}\033[m\nO cosseno é: \033[32m{cs:.2f}\033[m\nSua tangente é: \033[33m{tg:.2f}\033[m\nE seus graus em radiano são: \033[34m{rs:.2f}\033[m")
print ("--" * 8 + "Bons estudos!" + "--" * 8)