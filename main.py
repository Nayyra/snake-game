#configurações inicias

import pygame
import random
pygame.init()
pygame.display.set_caption("Snake.py")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (225, 0, 0)
verde = (0, 225, 0)
#parametros da cobra
tam_quadrado = 10
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tam_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tam_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tam_quadrado, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tam_quadrado, tam_quadrado])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontos(pontuacao):
    fonte = pygame.font.SysFont("Arial", 35)
    texto = fonte.render("Pontos: {}".format(pontuacao), True, branca)
    tela.blit(texto, [1, 1])

def selecionar_velo(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tam_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tam_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tam_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tam_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura /2
    y = altura/2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()


    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velo(evento.key)

        #desenhar a comida
        desenhar_comida(tam_quadrado, comida_x, comida_y)

        #atualizar posicao da cobra
        if x < 0 or x >= largura or y < 0 or y == altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        #desenhar a cobrinha
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #se a cobrinha bateu no seu corpo, menos a cabeça
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tam_quadrado, pixels)
        desenhar_pontos(tamanho_cobra - 1)

        #atualizar tela
        pygame.display.update()

        #criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_y, comida_x = gerar_comida()

        relogio.tick(velocidade_jogo)



#criar um loop infinito

# dentro do loop deve desenhar os objetos do jogo na tela
#pontuação/cobrinha/comida

#criar a logica de terminar o jogo
#o que acontece:
#bateu na parede, ou em si mesma

#pegar a interações do usuario
#fechar a tela e appertar as teclas pra mexer o bixo

rodar_jogo()