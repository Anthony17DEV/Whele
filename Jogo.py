import pygame
import numpy as np

# Inicializa o Pygame
pygame.init()

# Configurações padrão
largura_padrao, altura_padrao = 800, 600
largura, altura = largura_padrao, altura_padrao
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Whele")

# Função para carregar um vídeo e convertê-lo em uma lista de quadros
fundo_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/depositphotos_324257814-stock-illustration-computer-graphic-of-pixel-game.jpg")

# Outras configurações
cor_botao = (255, 165, 0)  # Laranja
tamanho_fonte = int(largura * 0.03)
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

# Função para criar botões
def criar_botao(rect, imagem):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Define a quantidade de movimento quando o mouse está sobre o botão
    movimento = 1

    # Verifica se o mouse está sobre o botão
    if rect.collidepoint(mouse_pos):
        # Adiciona destaque quando o mouse está sobre o botão
        destaque_rect = rect.move(np.random.randint(-movimento, movimento + 1), np.random.randint(-movimento, movimento + 1))
        tela.blit(imagem, destaque_rect.topleft)
        if mouse_click[0] == 1:
            # Executa a ação associada ao botão
            return True
    else:
        tela.blit(imagem, rect.topleft)

    return False

def redimensionar_tela(nova_largura, nova_altura):
    global largura, altura
    largura, altura = nova_largura, nova_altura
    tela = pygame.display.set_mode((largura, altura))

def configurar_resolucao_800x600():
    redimensionar_tela(800, 600)

def configurar_resolucao_1280x720():
    redimensionar_tela(1280, 720)

def configurar_resolucao_1920x1080():
    redimensionar_tela(1920, 1080)

tela_atual = "inicial"

# Loop principal
rodando = True
indice_frame = 0
configuracoes_abertas = False
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(fundo_img, (0, 0))

    largura_botao, altura_botao = largura * 0.2, altura * 0.1

    # Botão iniciar
    iniciar_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.2, largura_botao, altura_botao)
    if tela_atual == "inicial" and criar_botao(iniciar_rect, botao_iniciar_img):
        # Para a música de fundo ao clicar em "Iniciar"
        pygame.mixer.music.stop()
        print("Iniciar jogo!")

    # Botão Configurações
    configuracoes_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.35, largura_botao, altura_botao)
    if tela_atual == "inicial" and criar_botao(configuracoes_rect, botao_configuracoes_img):
        tela_atual = "configuracoes"
        print("Ir para configurações")

    # Botão Sair
    sair_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.5, largura_botao, altura_botao)
    if tela_atual == "inicial" and criar_botao(sair_rect, botao_sair_img):
        # Ação ao clicar em Sair (por enquanto, apenas fecha o jogo)
        rodando = False

    elif tela_atual == "configuracoes":
        tela.blit(fundo_img, (0, 0))  # Mantém a imagem de fundo
        imagem_resolucao = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Resolução.jpg")
        largura_imagem, altura_imagem = imagem_resolucao.get_size()
        tela.blit(imagem_resolucao, ((largura - largura_imagem) // 2, altura * 0.1))

        # Adiciona os botões
        botao_resolucao_800x600 = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/800x600.png")
        botao_resolucao_1280x720 = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/1280x720.png")
        botao_resolucao_1920x1080 = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/1920x1080.png")

        largura_botao, altura_botao = largura * 0.1, altura * 0.05
        espacamento = largura * 0.2

        # Posições dos botões em relação à imagem de resolução
        x_botao_800x600 = ((largura - largura_botao * 3 - espacamento * 2) // 2) + ((largura_imagem - largura_botao * 0.77 - espacamento * 2) // 2)
        x_botao_1280x720 = x_botao_800x600 + largura_botao + espacamento
        x_botao_1920x1080 = x_botao_1280x720 + largura_botao + espacamento
        y_botao = altura * 0.3

        # Blit dos botões
        tela.blit(botao_resolucao_800x600, (x_botao_800x600, y_botao))
        tela.blit(botao_resolucao_1280x720, (x_botao_1280x720, y_botao))
        tela.blit(botao_resolucao_1920x1080, (x_botao_1920x1080, y_botao))

        # Tratamento de eventos para os botões
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Verifica se o clique foi nos botões
                if x_botao_800x600 <= mouse_pos[0] <= x_botao_800x600 + largura_botao and \
                        y_botao <= mouse_pos[1] <= y_botao + altura_botao:
                    configurar_resolucao_800x600()
                    print("Resolução alterada para 800x600")

                elif x_botao_1280x720 <= mouse_pos[0] <= x_botao_1280x720 + largura_botao and \
                        y_botao <= mouse_pos[1] <= y_botao + altura_botao:
                    configurar_resolucao_1280x720()
                    print("Resolução alterada para 1280x720")

                elif x_botao_1920x1080 <= mouse_pos[0] <= x_botao_1920x1080 + largura_botao and \
                        y_botao <= mouse_pos[1] <= y_botao + altura_botao:
                    configurar_resolucao_1920x1080()
                    print("Resolução alterada para 1920x1080")

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)

# Finaliza o Pygame
pygame.quit()
