#022   
nome = input("Digite seu nome completo: ")
n0 = nome.title()
print(f"Seu nome é: \n{nome.title()}")
print(f'Seu nome em letras maiusculas é: \n{nome.upper()}')
print(f'Seu nome em letras minusculas é: \n{nome.lower()}')
# Número de letras
n2 = (nome.replace(' ',''))
print(f"Seu nome tem: \n{len(n2)} letras")
# Primeiro nome
n3 = (nome.split()[0]) #.split divide a str e a posição [0] é a primeira
n4 = n0.lower()
print(f"Seu primeiro nome é: \n{n3} e tem {len(n3)} letras!")
print(f'Pulando de duas em duas letras:\n{nome[::2]}')
print(f'De três em três:\n{nome[::3]}')
print(f'trocando a por e: {n4.replace('a','e')}')
print(f'trocando e por a: {n4.replace('e','a')}')
print(f'Trocando a por u: {n4.replace('a','u')}')
print(f'Trocando s por t: {n4.replace('s','t')}')
# Tocador de mp3
if n0 == 'Arthur Ribeiro Salvador' or 'Arthur' or 'Tutui':
    import pygame
    pygame.init()
    pygame.mixer.music.load('Ninar.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
#elif n0 == 'Jefferson Pereira Salvador' or 'Jefferson' or 'Jeff':
    import pygame
    pygame.init()
    pygame.mixer.music.load('room409.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
#elif n0 == 'Bruna Caroline Ribeiro Melo' or 'Bruna':