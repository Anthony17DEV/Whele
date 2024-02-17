import pygame
import numpy as np
import pytmx
import time

# Inicializa o Pygame
pygame.init()

# Configurações padrão
largura_padrao, altura_padrao = 1920, 1080
tela = pygame.display.set_mode((largura_padrao, altura_padrao), pygame.FULLSCREEN)
pygame.display.set_caption("Whele")

# Função para carregar um vídeo e convertê-lo em uma lista de quadros
fundo_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Tela de fundo.jpg")

# Outras configurações
cor_botao = (255, 165, 0)  # Laranja
tamanho_fonte = int(largura_padrao * 0.03)
fonte = pygame.font.Font(None, tamanho_fonte)

# Carrega a música de fundo
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/sons/Y2meta.app - Batman - Stage 1 (128 kbps).mp3")

# Toca a música de fundo em um loop infinito
pygame.mixer.music.play(-1)

# Carrega imagens dos botões
botao_iniciar_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Start.png")
botao_configuracoes_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/configurações.png")
botao_sair_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Sair.png")
botao_dificuldade_facil_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/FÁCIL.png")
botao_dificuldade_media_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/MÉDIA.png")
botao_dificuldade_dificil_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/DIFÍCIL.png")
botao_continuar_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/continue.png")

# Variável para armazenar a dificuldade selecionada
dificuldade_selecionada = None

# Função para criar botões
def criar_botao(rect, imagem):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Define a quantidade de movimento quando o mouse está sobre o botão
    movimento = 1

    # Verifica se o mouse está sobre o botão
    if rect.collidepoint(mouse_pos):
        # Adiciona destaque quando o mouse está sobre o botão
        destaque_rect = rect.move(np.random.randint(-movimento, movimento + 1),np.random.randint(-movimento, movimento + 1))
        tela.blit(imagem, destaque_rect.topleft)
        if mouse_click[0] == 1:
            # Executa a ação associada ao botão
            return True
    else:
        tela.blit(imagem, rect.topleft)

    return False

def configurar_dificuldade_facil():
    global dificuldade_selecionada
    dificuldade_selecionada = "Fácil"
    print("Dificuldade alterada para Fácil")

def configurar_dificuldade_media():
    global dificuldade_selecionada
    dificuldade_selecionada = "Média"
    print("Dificuldade alterada para Média")

def configurar_dificuldade_dificil():
    global dificuldade_selecionada
    dificuldade_selecionada = "Difícil"
    print("Dificuldade alterada para Difícil")

som_ligado = True

def alternar_som():
    global som_ligado
    if som_ligado:
        pygame.mixer.music.pause()
        som_ligado = False
    else:
        pygame.mixer.music.unpause()
        som_ligado = True


# Função para carregar o mapa TMX
def carregar_mapa(nome_arquivo):
    try:
        mapa = pytmx.load_pygame(nome_arquivo)
        return mapa
    except FileNotFoundError:
        print("Erro: Arquivo do mapa não encontrado.")

def pausar_jogo(pausado):
    global tela_atual  # Declaração para acessar a variável tela_atual globalmente

    # Posição dos botões
    largura_botao_continuar = botao_continuar_img.get_width()
    altura_botao_continuar = botao_continuar_img.get_height()
    x_botao_continuar = (largura_padrao - largura_botao_continuar) // 2
    y_botao_continuar = altura_padrao * 0.4

    largura_botao_sair = botao_sair_img.get_width()
    altura_botao_sair = botao_sair_img.get_height()
    x_botao_sair = (largura_padrao - largura_botao_sair) // 2
    y_botao_sair = altura_padrao * 0.5

    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Clique do mouse detectado!")

                # Obtém a posição do mouse
                mouse_pos = pygame.mouse.get_pos()

                print("Posição do clique do mouse:", mouse_pos)

                # Verifica se o mouse está sobre o botão de continuar
                if x_botao_continuar <= mouse_pos[0] <= x_botao_continuar + largura_botao_continuar and \
                        y_botao_continuar <= mouse_pos[1] <= y_botao_continuar + altura_botao_continuar:
                    print("Botão Continuar clicado!")
                    pausado = False

                # Verifica se o mouse está sobre o botão de sair
                elif x_botao_sair <= mouse_pos[0] <= x_botao_sair + largura_botao_sair and \
                        y_botao_sair <= mouse_pos[1] <= y_botao_sair + altura_botao_sair:
                    print("Botão Sair clicado!")
                    tela_atual = "inicial"
                    pausado = False

        tela.blit(fundo_img, (0, 0))
        tela.blit(botao_continuar_img, (x_botao_continuar, y_botao_continuar))
        tela.blit(botao_sair_img, (x_botao_sair, y_botao_sair))

        pygame.display.update()
        clock.tick(30)

    return pausado

def iniciar_jogo():
    global tela_atual
    mapa = carregar_mapa("C:/Users/antho/Desktop/Meus programas/pythonProject3/Mapa/Mapa Whele.tmx")
    tela_atual = "jogo"
    posicao_camera = (0, 0)
    rodando = True
    pausado = False

    tempo_atraso = 0

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pausado = not pausado
                    pausado = pausar_jogo(pausado)

        if not pausado:
            renderizar_mapa(mapa, tela, posicao_camera)
            pygame.display.flip()
            clock.tick(30)

        if tela_atual == "inicial":
            if tempo_atraso == 0:
                tempo_atraso = time.time()
            elif time.time() - tempo_atraso > 0.00000000000000000001:
                rodando = False

# Define as dimensões da tela
largura_tela, altura_tela = largura_padrao, altura_padrao

# Função para renderizar o mapa considerando a posição da câmera
def renderizar_mapa(mapa, tela, posicao_camera):
    # Calcula a escala necessária para preencher a tela com o mapa
    escala_x = tela.get_width() / (mapa.width * mapa.tilewidth)
    escala_y = tela.get_height() / (mapa.height * mapa.tileheight)
    escala = max(escala_x, escala_y)

    # Define a largura e a altura do mapa após a escala
    largura_mapa = int(mapa.width * mapa.tilewidth * escala)
    altura_mapa = int(mapa.height * mapa.tileheight * escala)

    # Calcula o deslocamento da câmera para centralizar o mapa na tela
    deslocamento_x = (tela.get_width() - largura_mapa) // 2
    deslocamento_y = (tela.get_height() - altura_mapa) // 2

    # Renderiza o mapa
    for layer in mapa.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x in range(0, mapa.width):
                for y in range(0, mapa.height):
                    gid = layer.data[y][x]
                    if gid:
                        tile = mapa.get_tile_image_by_gid(gid)
                        if tile:
                            tela.blit(pygame.transform.scale(tile, (int(mapa.tilewidth * escala), int(mapa.tileheight * escala))),
                                      (x * mapa.tilewidth * escala - posicao_camera[0] + deslocamento_x,
                                       y * mapa.tileheight * escala - posicao_camera[1] + deslocamento_y))

tela_atual = "inicial"

# Loop principal
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(fundo_img, (0, 0))

    # Dimensões dos botões
    largura_botao, altura_botao = botao_iniciar_img.get_width(), botao_iniciar_img.get_height()

    # Posições dos botões
    x_botao_iniciar = (largura_padrao - largura_botao) // 2
    y_botao_iniciar = altura_padrao * 0.33

    x_botao_configuracoes = (largura_padrao - largura_botao) // 2
    y_botao_configuracoes = altura_padrao * 0.42

    x_botao_sair = (largura_padrao - largura_botao) // 2
    y_botao_sair = altura_padrao * 0.51

    # Criar retângulos para os botões
    iniciar_rect = pygame.Rect(x_botao_iniciar, y_botao_iniciar, largura_botao, altura_botao)
    configuracoes_rect = pygame.Rect(x_botao_configuracoes, y_botao_configuracoes, largura_botao, altura_botao)
    sair_rect = pygame.Rect(x_botao_sair, y_botao_sair, largura_botao, altura_botao)

    # Se a tela atual for "inicial" e o botão "Iniciar" for clicado, carrega o mapa
    if tela_atual == "inicial" and criar_botao(iniciar_rect, botao_iniciar_img):
        iniciar_jogo()
        print("Mapa carregado")

    # Botão iniciar
    if tela_atual == "inicial" and criar_botao(iniciar_rect, botao_iniciar_img):
        # Para a música de fundo ao clicar em "Iniciar"
        pygame.mixer.music.stop()
        print("Iniciar jogo!")

    # Botão Configurações
    if tela_atual == "inicial" and criar_botao(configuracoes_rect, botao_configuracoes_img):
        tela_atual = "configuracoes"
        print("Ir para configurações")

    # Botão Sair
    if tela_atual == "inicial" and criar_botao(sair_rect, botao_sair_img):
        rodando = False

    elif tela_atual == "configuracoes":
        tela.blit(fundo_img, (0, 0))  # Mantém a imagem de fundo
        imagem_dificuldade = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/DIFICULDADE.png")
        largura_imagem_dificuldade, altura_imagem_dificuldade = imagem_dificuldade.get_size()
        posicao_imagem_dificuldade = ((largura_padrao - largura_imagem_dificuldade) // 2, altura_padrao * 0.15)
        tela.blit(imagem_dificuldade, posicao_imagem_dificuldade)

        # Carrega botões de dificuldade e calcula suas posições
        largura_botao_dificuldade, altura_botao_dificuldade = botao_dificuldade_facil_img.get_size()
        espacamento_dificuldade = largura_padrao * 0.05

        x_botao_dificuldade_facil = (largura_padrao - largura_botao_dificuldade * 3 - espacamento_dificuldade * 2) // 2
        x_botao_dificuldade_media = x_botao_dificuldade_facil + largura_botao_dificuldade + espacamento_dificuldade
        x_botao_dificuldade_dificil = x_botao_dificuldade_media + largura_botao_dificuldade + espacamento_dificuldade
        y_botao_dificuldade = altura_padrao * 0.30

        tela.blit(botao_dificuldade_facil_img, (x_botao_dificuldade_facil, y_botao_dificuldade))
        tela.blit(botao_dificuldade_media_img, (x_botao_dificuldade_media, y_botao_dificuldade))
        tela.blit(botao_dificuldade_dificil_img, (x_botao_dificuldade_dificil, y_botao_dificuldade))

        # Tratamento de eventos para os botões de dificuldade
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Verifica se o clique foi nos botões de dificuldade
                if x_botao_dificuldade_facil <= mouse_pos[
                    0] <= x_botao_dificuldade_facil + largura_botao_dificuldade and \
                        y_botao_dificuldade <= mouse_pos[1] <= y_botao_dificuldade + altura_botao_dificuldade:
                    configurar_dificuldade_facil()

                elif x_botao_dificuldade_media <= mouse_pos[
                    0] <= x_botao_dificuldade_media + largura_botao_dificuldade and \
                        y_botao_dificuldade <= mouse_pos[1] <= y_botao_dificuldade + altura_botao_dificuldade:
                    configurar_dificuldade_media()

                elif x_botao_dificuldade_dificil <= mouse_pos[
                    0] <= x_botao_dificuldade_dificil + largura_botao_dificuldade and \
                        y_botao_dificuldade <= mouse_pos[1] <= y_botao_dificuldade + altura_botao_dificuldade:
                    configurar_dificuldade_dificil()

        # Carrega imagem de som e calcula sua posição
        imagem_dificuldade = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/SOM.png")
        largura_imagem_dificuldade, altura_imagem_dificuldade = imagem_dificuldade.get_size()
        posicao_imagem_dificuldade = ((largura_padrao - largura_imagem_dificuldade) // 2, altura_padrao * 0.45)
        tela.blit(imagem_dificuldade, posicao_imagem_dificuldade)

        # Carrega imagens dos botões de ligar e desligar o som
        botao_som_ligado_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/LIGADO.png")
        botao_som_desligado_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/DESLIGADO.png")

        # Dimensões dos botões de ligar e desligar o som
        largura_botao_som = botao_som_ligado_img.get_width()
        altura_botao_som = botao_som_ligado_img.get_height()

        # Calcula a posição e as dimensões do botão de ligar o som
        x_botao_som_ligado = (largura_padrao - largura_botao_som) // 2.1
        y_botao_som_ligado = int(altura_padrao * 0.57)
        botao_som_ligado_rect = pygame.Rect(x_botao_som_ligado, y_botao_som_ligado, largura_botao_som, altura_botao_som)

        # Calcula a posição e as dimensões do botão de desligar o som
        x_botao_som_desligado = x_botao_som_ligado + largura_botao_som + 10  # 10 pixels de espaçamento
        y_botao_som_desligado = y_botao_som_ligado
        botao_som_desligado_rect = pygame.Rect(x_botao_som_desligado, y_botao_som_desligado, largura_botao_som,altura_botao_som)

        # Verifica se o botão de ligar o som foi clicado
        if tela_atual == "configuracoes" and criar_botao(botao_som_ligado_rect,botao_som_ligado_img) and not som_ligado:
            alternar_som()
            print("Som ligado")

        # Verifica se o botão de desligar o som foi clicado
        if tela_atual == "configuracoes" and criar_botao(botao_som_desligado_rect,botao_som_desligado_img) and som_ligado:
            alternar_som()
            print("Som desligado")

        # Adiciona esta parte do código onde são definidas as dimensões e posições dos botões na tela de configurações
        # Posições dos botões
        x_botao_sair_configuracoes = (largura_padrao - largura_botao) // 2
        y_botao_sair_configuracoes = altura_padrao * 0.70

        # Criar retângulo para o botão "Sair" nas configurações
        sair_configuracoes_rect = pygame.Rect(x_botao_sair_configuracoes, y_botao_sair_configuracoes, largura_botao,altura_botao)

        # Carrega imagem do botão "Sair"
        botao_sair_configuracoes_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Sair.png")

        # Botão "Sair" nas configurações
        if tela_atual == "configuracoes" and criar_botao(sair_configuracoes_rect, botao_sair_configuracoes_img):
            tela_atual = "inicial"
            print("Voltar para tela inicial")

    # Se a tela atual for "inicial" e o botão "Iniciar" for clicado, carrega o mapa
    if tela_atual == "inicial" and criar_botao(iniciar_rect, botao_iniciar_img):
        # Carrega o mapa
        mapa = carregar_mapa("C:/Users/antho/Desktop/Meus programas/pythonProject3/Mapa/Mapa Whele.tmx")
        print("Mapa carregado")

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)

# Finaliza o Pygame
pygame.quit()
