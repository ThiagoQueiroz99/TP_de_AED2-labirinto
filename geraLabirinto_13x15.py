import random

class GeraLabirinto:
    def __init__(self, linhas, colunas):
        self.labirinto = [[0] * colunas for _ in range(linhas)]
        for i in range (linhas):
            for j in range (colunas):
                if(i == 0 or j == 0 or i == linhas-1 or j == colunas-1):    #criacao das bordas
                    self.labirinto[i][j] = 2

    def cava_na_posicao(self, i, j):
        final_alcancado = False
        if(self.labirinto[i][j] == 2):                                      #chegou na borda (possui saida)
            self.labirinto[i][j] = "S"
            final_alcancado = True
            return final_alcancado
        self.labirinto[i][j] = 1
        return final_alcancado
    
    def cava_na_posicao_apos_encontrar_saida(self, i, j):                   #funcao utilizada apos a saida ser feita
        final_alcancado = False
        if(self.labirinto[i][j] == 2):                                      #chegou na borda, e impede de criar uma nova saida)
            final_alcancado = True
        if(final_alcancado == False):
            self.labirinto[i][j] = 1

    def busca_elemento(self, lista):
        primeira_coord = None
        segunda_coord = None
        metade_esq = lista[:len(lista)//2]
        metade_dir = lista[len(lista)//2:]
        
        if(self.labirinto[metade_dir[0]][metade_dir[1]] == 0 or self.labirinto[metade_dir[0]][metade_dir[1]] == 2):
            primeira_coord = self.labirinto[metade_esq[0]][metade_esq[1]]
            segunda_coord = self.labirinto[metade_dir[0]][metade_dir[1]]
        return primeira_coord, segunda_coord
        
    def insere_e_verifica_coords_na_lista(lista, i, j, x):
        area_valida = x
        lista = [(i, j - 1, i, j - 2),                                      #esquerda
                (i - 1 , j, i - 2, j),                                      #cima
                (i, j + 1, i, j + 2),                                       #direita 
                (i + 1, j, i + 2, j)]                                       #baixo
        for i in range(len(lista)):
            x, y = matriz.busca_elemento(lista[i])
            if(x == 1 or y == 1):                                           #posicao nao e uma parede
                area_valida = False
            for j in range(len(lista)):
                if(lista[i][j] < 0):                                        #coordenada fora do mapa
                    area_valida = False     
            if(area_valida == True):                                        #coordenada valida adicionada na lista
                lista_coords.append(lista[i])
            area_valida = True
        escavacao = random.randint(0, len(lista)-1)
        return lista_coords, lista_coords[escavacao], escavacao
    
    def imprime_matriz(self, linhas, colunas):
        for i in range(linhas):
            for j in range(colunas):
                print("%s " % self.labirinto[i][j], end = " ")
            print()

if __name__ == "__main__":
    linhas = 11 + 2   #+2 sao as bordas, que fazem parte da matriz e limitam o conteudo      #as bordas ajudam na validacao de posicao
    colunas = 13 + 2  #+2 sao as bordas, que fazem parte da matriz e limitam o conteudo      #as bordas ajudam na validacao de posicao
    i = random.randrange(3, (linhas - 2), 2) + 1                            #coordenada impar entre 3 e (linhas - 2)   #+1 por causa da adicao da borda
    j = random.randrange(3, (colunas - 2), 2) + 1                           #coordenada impar entre 3 e (colunas - 2)  #+1 por causa da adicao da borda
    lista_coords = []
    matriz = GeraLabirinto(linhas, colunas) 
    matriz.cava_na_posicao(i, j)                                            #gera o primeiro ponto
    lista_coords, local_aleatorio_escolhido, area_escavada = matriz.insere_e_verifica_coords_na_lista(i,j, True)
    i = local_aleatorio_escolhido[0]                                        #insere os quatro primeiros corredores em lista_coords (parte inicial)
    j = local_aleatorio_escolhido[1]
    matriz.cava_na_posicao(i, j)
    i = local_aleatorio_escolhido[2]
    j = local_aleatorio_escolhido[3]
    matriz.cava_na_posicao(i, j)                                            #insere os quatro primeiros corredores em lista_coords (parte final)
    while(lista_coords != []):
        lista_coords.remove(lista_coords[area_escavada])
        lista_coords, local_aleatorio_escolhido, area_escavada = matriz.insere_e_verifica_coords_na_lista(i,j, True)
        i = local_aleatorio_escolhido[0]                                    #insere os proximos corredores potenciais em lista_coords (parte inicial)
        j = local_aleatorio_escolhido[1]
        possui_saida = matriz.cava_na_posicao(i, j)
        if(possui_saida == True):                                           #saida encontrada = sai do loop
            break
        i = local_aleatorio_escolhido[2]
        j = local_aleatorio_escolhido[3]
        possui_saida = matriz.cava_na_posicao(i, j)                         #insere os proximos corredores potenciais em lista_coords (parte final)
        if(possui_saida == True):                                           #saida encontrada = sai do loop
            break

    while(lista_coords != []):                                              #apos encontrar a saida, as posicoes validas restantes sao cavadas ate o conteudo da lista esvaziar
        i = lista_coords[0][0]                                              #cava os proximos corredores restantes (parte inicial)
        j = lista_coords[0][1]
        matriz.cava_na_posicao_apos_encontrar_saida(i, j)
        i = lista_coords[0][2]
        j = lista_coords[0][3]
        matriz.cava_na_posicao_apos_encontrar_saida(i, j)                   #cava os proximos corredores restantes (parte final)
        lista_coords.remove(lista_coords[0])
    matriz.imprime_matriz(linhas, colunas)                                  #matriz de um labirinto gerado aleatoriamente com uma unica saida
