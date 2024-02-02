import pygame
import sys
import os
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


# Lista de opções
opcao_resolucao = ["800600", "1280720", "19201080"]
opcao_dificuldade = ["FÁCIL", "MÉDIA", "DIFÍCIL"]
opcao_som = ["LIGADO", "DESLIGADO"]

# Outras configurações
cor_botao = (255, 165, 0)  # Laranja
tamanho_fonte = int(largura * 0.03)
fonte = pygame.font.Font(None, tamanho_fonte)


# Carrega imagens dos botões
botao_iniciar_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Start (1).png")
botao_configuracoes_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/configurações (1).png")
botao_sair_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Sair (1).png")

# Carrega imagens dos títulos
titulo_resolucao_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/Resolução.png")
titulo_dificuldade_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/DIFICULDADE.png")
titulo_som_img = pygame.image.load("C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/SOM.png")

# Função para criar botões
def criar_botao(rect, imagem, cor_destaque):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Ajuste para centralizar o botão
    rect.x = (largura - rect.width) // 2
    rect.y = rect.y  # Mantenha a posição Y original

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

# Loop principal
rodando = True
indice_frame = 0  # Índice para controlar os frames do fundo
configuracoes_abertas = False  # Adiciona essa linha antes do loop principal
clock = pygame.time.Clock()
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Desenha a imagem de fundo
    tela.blit(fundo_img, (0, 0))

    # Criação de botões
    largura_botao, altura_botao = largura * 0.2, altura * 0.1

    # Botão Iniciar
    iniciar_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.2, largura_botao, altura_botao)
    if criar_botao(iniciar_rect, botao_iniciar_img, (255, 200, 0)):
        # Ação ao clicar em Iniciar (por enquanto, apenas imprime uma mensagem)
        print("Iniciar jogo!")

    # Botão Configurações
    configuracoes_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.35, largura_botao, altura_botao)
    if criar_botao(configuracoes_rect, botao_configuracoes_img, (255, 200, 0)):
        # Ação ao clicar em Configurações (abrir tela de configurações)
        configuracoes_abertas = True
        while configuracoes_abertas:
            for evento_config in pygame.event.get():
                if evento_config.type == pygame.QUIT:
                    configuracoes_abertas = False

            # Seção de desenho e interação na tela de configurações
            tela.blit(titulo_resolucao_img, (largura * 0.1, altura * 0.1))
            # Adiciona botões para escolher a resolução
            for i, opcao_resolucao in enumerate(opcao_resolucao):
                # Gera o caminho da imagem com base na opção de resolução
                nome_arquivo = ''.join(c if c.isalnum() or c.isspace() else '' for c in opcao_resolucao)

                # Verifica se o nome do arquivo não está vazio
                if nome_arquivo:
                    caminho_imagem_resolucao = os.path.join(
                        "C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens", f"{nome_arquivo}.png")

                    # Carrega a imagem se ela existir
                    try:
                        img_resolucao = pygame.image.load(caminho_imagem_resolucao)
                    except pygame.error:
                        print(f"Erro ao carregar a imagem: {caminho_imagem_resolucao}")
                        continue

                    rect_opcao_resolucao = pygame.Rect(
                        largura * 0.1 + (largura * 0.3) * i,
                        altura * 0.2,
                        largura * 0.25,
                        altura * 0.1
                    )

                    if criar_botao(rect_opcao_resolucao, img_resolucao, (255, 200, 0)):
                        largura, altura = map(int, opcao_resolucao.split('X'))
                        tela = pygame.display.set_mode((largura, altura))
                        print(f"Tamanho da tela alterado para {largura}x{altura}")

            tela.blit(titulo_dificuldade_img, (largura * 0.1, altura * 0.4))
            # Adiciona botões para escolher a dificuldade
            for i, opcao_dificuldade in enumerate(opcao_dificuldade):
                caminho_imagem_dificuldade = f"C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/{opcao_dificuldade}.png"
                img_dificuldade = pygame.image.load(caminho_imagem_dificuldade)

                rect_opcao_dificuldade = pygame.Rect(
                    largura * 0.1 + (largura * 0.3) * i,
                    altura * 0.5,
                    largura * 0.25,
                    altura * 0.1
                )

                if criar_botao(rect_opcao_dificuldade, img_dificuldade, (255, 200, 0)):
                    print(f"Dificuldade alterada para {opcao_dificuldade}")

            tela.blit(titulo_som_img, (largura * 0.1, altura * 0.7))
            # Adiciona botões para ligar/desligar o som
            for i, opcao_som in enumerate(opcao_som):
                caminho_imagem_som = f"C:/Users/antho/Desktop/Meus programas/pythonProject3/imagens/{opcao_som}.png"
                img_som = pygame.image.load(caminho_imagem_som)

                rect_opcao_som = pygame.Rect(
                    largura * 0.1 + (largura * 0.3) * i,
                    altura * 0.75,
                    largura * 0.25,
                    altura * 0.1
                )

                if criar_botao(rect_opcao_som, img_som, (255, 200, 0)):
                    print(f"Som alterado para {opcao_som}")

            voltar_rect = pygame.Rect(largura * 0.1, altura * 0.9, largura_botao, altura_botao)
            if criar_botao(voltar_rect, botao_sair_img, (255, 200, 0)):
                configuracoes_abertas = False

            pygame.display.flip()

    # Botão Sair
    sair_rect = pygame.Rect((largura - largura_botao) // 2, altura * 0.5, largura_botao, altura_botao)
    if criar_botao(sair_rect, botao_sair_img, (255, 200, 0)):
        # Ação ao clicar em Sair (por enquanto, apenas fecha o jogo)
        rodando = False

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)  # Ajuste a taxa de quadros conforme necessár

    if configuracoes_abertas:
        pygame.display.set_mode((largura, altura))  # Mova esta linha para fora do loop de configurações

# Finaliza o Pygame
pygame.quit()
