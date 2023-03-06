import random

class GeraLabirinto:
    def __init__(self):
        self.lista_coords = []                                                          #guarda as posicoes validas para cavar os campos
        self.linhas = 11 + 2                                                            #+2 sao as bordas, que fazem parte da matriz e limitam o conteudo  #as bordas ajudam na validacao de posicao
        self.colunas = 13 + 2                                                           #+2 sao as bordas, que fazem parte da matriz e limitam o conteudo  #as bordas ajudam na validacao de posicao
        self.i_random = random.randrange(3, (self.linhas - 2), 2) + 1                   #coordenada impar entre 3 e (linhas - 2)  #+1 por causa da adicao da borda
        self.j_random = random.randrange(3, (self.colunas - 2), 2) + 1                  #coordenada impar entre 3 e (colunas - 2)  #+1 por causa da adicao da borda
        self.labirinto = [[0] * self.colunas for _ in range(self.linhas)]
        for i in range (self.linhas):
            for j in range (self.colunas):
                if(i == 0 or j == 0 or i == self.linhas-1 or j == self.colunas-1):      #criacao das bordas
                    self.labirinto[i][j] = 2

    def cava_na_posicao(self, i, j):
        guarda_pos_saida = False
        final_alcancado = False
        if(self.labirinto[i][j] == 2):                                                  #chegou na borda (possui saida)
            self.labirinto[i][j] = 1
            final_alcancado = True
            guarda_pos_saida = (i,j)
            return final_alcancado, guarda_pos_saida
        self.labirinto[i][j] = 1
        return final_alcancado, guarda_pos_saida
    
    def cava_primeiro_campo(self, i, j, lista_coords):
        lista_coords.append((i,j))                                                      #armazenar a posicao inicial para posiocionar o jogador
        self.labirinto[i][j] = 1
        return lista_coords[0]
    
    def cava_na_posicao_apos_encontrar_saida(self, i, j):                               #funcao utilizada apos a saida ser feita
        final_alcancado = False
        if(self.labirinto[i][j] == 2):                                                  #chegou na borda, e impede de criar uma nova saida)
            final_alcancado = True
        if(final_alcancado == False):
            self.labirinto[i][j] = 1

    def campos_iniciais(self, i_random, j_random, lista_coords):
        pos_jogador = self.cava_primeiro_campo(i_random, j_random, lista_coords)        #gera o primeiro ponto
        lista_coords.remove(lista_coords[0])
        lista_coords, local_aleatorio_escolhido, area_escavada = self.insere_e_verifica_coords_na_lista(self, i_random, j_random, True)
        i_random = local_aleatorio_escolhido[0]                                         #insere os quatro primeiros corredores em lista_coords (parte inicial)
        j_random = local_aleatorio_escolhido[1]
        self.cava_na_posicao(i_random, j_random)
        i_random = local_aleatorio_escolhido[2]
        j_random = local_aleatorio_escolhido[3]
        self.cava_na_posicao(i_random, j_random)                                        #insere os quatro primeiros corredores em lista_coords (parte final)
        return pos_jogador

    def escavacao_loop(self, i_random, j_random, lista_coords):
        lista_coords, local_aleatorio_escolhido, area_escavada = self.insere_e_verifica_coords_na_lista(self, i_random, j_random, True)
        while(lista_coords != []):
            lista_coords.remove(lista_coords[area_escavada])
            lista_coords, local_aleatorio_escolhido, area_escavada = self.insere_e_verifica_coords_na_lista(self, i_random, j_random, True)
            i_random = local_aleatorio_escolhido[0]                                     #insere os proximos corredores potenciais em lista_coords (parte inicial)
            j_random = local_aleatorio_escolhido[1]
            possui_saida, pos_saida = self.cava_na_posicao(i_random, j_random)
            if(possui_saida == True):                                                   #saida encontrada = sai do loop
                return pos_saida
            i_random = local_aleatorio_escolhido[2]
            j_random = local_aleatorio_escolhido[3]
            possui_saida, pos_saida = self.cava_na_posicao(i_random, j_random)          #insere os proximos corredores potenciais em lista_coords (parte final)
            if(possui_saida == True):                                                   #saida encontrada = sai do loop
                return pos_saida

        while(lista_coords != []):                                                      #apos encontrar a saida, as posicoes validas restantes sao cavadas ate o conteudo da lista esvaziar
            i_random = lista_coords[0][0]                                               #cava os proximos corredores restantes (parte inicial)
            j_random = lista_coords[0][1]
            self.cava_na_posicao_apos_encontrar_saida(i_random, j_random)
            i_random = lista_coords[0][2]
            j_random = lista_coords[0][3]
            self.cava_na_posicao_apos_encontrar_saida(i_random, j_random)               #cava os proximos corredores restantes (parte final)
            lista_coords.remove(lista_coords[0])

    def busca_elemento(self, lista):
        primeira_coord = None
        segunda_coord = None
        metade_esq = lista[:len(lista)//2]
        metade_dir = lista[len(lista)//2:]
        
        if(self.labirinto[metade_dir[0]][metade_dir[1]] == 0 or self.labirinto[metade_dir[0]][metade_dir[1]] == 2):
            primeira_coord = self.labirinto[metade_esq[0]][metade_esq[1]]
            segunda_coord = self.labirinto[metade_dir[0]][metade_dir[1]]
        return primeira_coord, segunda_coord
        
    def insere_e_verifica_coords_na_lista(self, lista, i, j, x):
        area_valida = x
        lista = [(i, j - 1, i, j - 2),                                                  #esquerda
                (i - 1 , j, i - 2, j),                                                  #cima
                (i, j + 1, i, j + 2),                                                   #direita 
                (i + 1, j, i + 2, j)]                                                   #baixo
        for i in range(len(lista)):
            x, y = self.busca_elemento(lista[i])
            if(x == 1 or y == 1):                                                       #posicao nao e uma parede
                area_valida = False
            for j in range(len(lista)):
                if(lista[i][j] < 0):                                                    #coordenada fora do mapa
                    area_valida = False     
            if(area_valida == True):                                                    #coordenada valida adicionada na lista
                self.lista_coords.append(lista[i])
            area_valida = True
        escavacao = random.randint(0, len(lista)-1)
        return self.lista_coords, self.lista_coords[escavacao], escavacao

    def imprime_matriz(self, linhas, colunas):
        for i in range(linhas):
            for j in range(colunas):
                print("%s " % self.labirinto[i][j], end = " ")
            print()
        
    def pega_matriz(self):
        return self.labirinto