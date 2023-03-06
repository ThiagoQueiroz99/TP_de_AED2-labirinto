import pygame
from sys import exit
import botao
import geraLabirinto_13x15 as lab

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
GRAY = ((127,127,127))

TELA_JOGO_LARGURA = 800
TELA_JOGO_ALTURA = 600
TAM_CEDULA = 40
GAME_STATE = True

# Gera lab.
matriz = lab.GeraLabirinto()
coords = matriz.campos_iniciais(matriz.i_random, matriz.j_random, matriz.lista_coords)   #insere o primeiro ponto ma matriz #e insere os quatro primeiros corredores na lista
# Gera qual a saida
coord_saida = matriz.escavacao_loop(matriz.i_random, matriz.j_random, matriz.lista_coords)    #enquanto lista nao estiver vazia fica em loop
lab_teste = matriz.pega_matriz()

# Resolução do lab.
# Coordenadas do jogador
player_x = coords[0]
player_y = coords[1]

pygame.init()
clock = pygame.time.Clock()
janela = pygame.display.set_mode((TELA_JOGO_LARGURA,TELA_JOGO_ALTURA))
test_font = pygame.font.Font(None,50) # Fontes args(font type, font size)
text_surface = test_font.render("GAME OVER", False, 'black').convert_alpha() # Cria uma superfice texto args(texto,antialiasing, cor)
botao_restart = botao.Botao(600, 0, 100, 100, 'blue', 'Desistir')
while True: # Fica rodando 
    # Processa eventos Verificar essa parte.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # === Movimento do jogador ===
        if GAME_STATE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if player_y > 0 and lab_teste[player_x][player_y-1] == 1:
                        player_y -= 1
                elif event.key == pygame.K_RIGHT:
                    if player_y < len(lab_teste[0])-1 and lab_teste[player_x][player_y+1] == 1:
                        player_y += 1
                elif event.key == pygame.K_UP:
                    if player_x > 0 and lab_teste[player_x-1][player_y] == 1:
                        player_x -= 1
                elif event.key == pygame.K_DOWN:
                    if player_x < len(lab_teste)-1 and lab_teste[player_x+1][player_y] == 1:
                        player_x += 1
            # ==========
            # Condição de vitoria
            if player_x == coord_saida[0] and player_y == coord_saida[1]:
                print("GAME OVER")
                GAME_STATE = False

    # Posição do mouse na tela
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if GAME_STATE:    
        janela.fill(PRETO)

        for eventos in pygame.event.get(): # Procura por eventos que o jogador possa fazer.
            if(eventos.type == pygame.QUIT):
                pygame.quit()
                exit() # Vai sair do programa
        
        # Desenha o labirinto
        for linha in range(len(lab_teste)):
            for coluna in range(len(lab_teste[linha])):
                if lab_teste[linha][coluna] == 1:
                    pygame.draw.rect(janela, BRANCO, (coluna*TAM_CEDULA, linha*TAM_CEDULA,TAM_CEDULA,TAM_CEDULA))
                if lab_teste[linha][coluna] == 2:
                    pygame.draw.rect(janela, GRAY, (coluna*TAM_CEDULA, linha*TAM_CEDULA,TAM_CEDULA,TAM_CEDULA))

        # Desenha o jogador
        pygame.draw.circle(janela,(255,0,0),(player_y*TAM_CEDULA+TAM_CEDULA//2, player_x*TAM_CEDULA+TAM_CEDULA//2),TAM_CEDULA//2)
        # Desenha o botao
        botao_restart.cria(janela)
        # Verifica se foi clicado
        if botao_restart.click(mouse_pos, mouse_click):
            print("Algo")
    else:
        janela.fill("gray")
        janela.blit(text_surface,(TELA_JOGO_LARGURA//2,TELA_JOGO_ALTURA//2))
        #print("GAME OVER")

    pygame.display.update()
    clock.tick(60)

    
