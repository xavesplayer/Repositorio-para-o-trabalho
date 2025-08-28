#051 10 primeiros termos de uma progressão aritimetica
primeiro = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão: '))
for c in range(10):
    termo = primeiro + c * razao
    print(termo)