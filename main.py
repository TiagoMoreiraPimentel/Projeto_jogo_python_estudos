import pygame as pg
#variaveis de posicionamento do objeto circulo verde
x = 250
y = 400
# quantos pixels o objeto vai movimentar ao pressionar o botão
velocidade = 10
fundo = pg.image.load('fundo.png')
personagem = pg.image.load('personagem.png')

# inicia o pygame
pg.init()

# cria uma janela para o jogo
janela = pg.display.set_mode((430,600))

# adiciona um titulo ao jogo
pg.display.set_caption("Criando um jogo com Python")

# variavel boleana para definir que a janela esta aberta
janela_aberta = True

# loping para manter a janela aberta
while janela_aberta:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            janela_aberta = False

    # movimentar objeto ao pressionar os botões
    comandos = pg.key.get_pressed()
    if comandos[pg.K_UP]:
        y-= velocidade
    if comandos[pg.K_DOWN]:
        y+= velocidade
    if comandos[pg.K_RIGHT]:
        x+= velocidade
    if comandos[pg.K_LEFT]:
        x-= velocidade

    # função para alterar o tamanho de uma imagem
    def diminuir_imagem(imagem, novo_tamanho):
        imagem_diminuida = pg.transform.scale(imagem, novo_tamanho)
        return imagem_diminuida
    # Definição do novo tamanho
    novo_tamanho = (150, 150)
    # Diminuir a imagem
    imagem_diminuida = diminuir_imagem(personagem, novo_tamanho)

    # atualizar tela com cor preta
    janela.blit(fundo,(0,0))
    # cria um objeto personagem na tela
    janela.blit(imagem_diminuida,(x,y))
    # atualiza a tela
    pg.display.update()

pg.quit()







