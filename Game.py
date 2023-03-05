import pygame
from sys import exit

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
GRAY = ((127,127,127))

TELA_JOGO_LARGURA = 500 
TELA_JOGO_ALTURA = 500
TAM_CEDULA = 40
GAME_STATE = True
# Define a matriz de testes
# lab_teste = [
#     [1, 1, 1, 1, 1],
#     [0, 0, 1, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 0, 1, 0, 1],
#     [0, 0, 1, 0, 0]
# ]
# Gera lab.
lab_teste = [
    [2, 2, 2, 2, 2, 2, 2],
    [2 ,1, 1, 1, 1, 1, 2],
    [2 ,0, 0, 0, 0, 1, 2],
    [2 ,0, 1, 1, 1, 1, 2],
    [2 ,0, 0, 1, 0, 1, 2],
    [2 ,0, 0, 1, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2]
]
# Gera qual a saida
coord_saida = (5,3)
# Resolução do lab.
# Coordenadas do jogador
player_x = 1
player_y = 1

pygame.init()
clock = pygame.time.Clock()
janela = pygame.display.set_mode((TELA_JOGO_ALTURA,TELA_JOGO_LARGURA))

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

        #Desenha o jogador
        pygame.draw.circle(janela,(255,0,0),(player_y*TAM_CEDULA+TAM_CEDULA//2, player_x*TAM_CEDULA+TAM_CEDULA//2),TAM_CEDULA//2)
    else:
        janela.fill("gray")
        #print("GAME OVER")

    pygame.display.update()
    clock.tick(60)

    
