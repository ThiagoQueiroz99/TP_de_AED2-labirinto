import random

class GeraLabirinto:
    def __init__(self, linhas, colunas):
        self.labirinto = [[0] * colunas for _ in range(linhas)]
        for i in range (linhas):
            for j in range (colunas):
                if(i == 0 or j == 0 or i == linhas-1 or j == colunas-1):
                    self.labirinto[i][j] = 2

    def cava_na_posicao(self, i, j):
        final_alcancado = False
        if(self.labirinto[i][j] == 2):          #chegou na borda (possui saida)
            self.labirinto[i][j] = 3
            final_alcancado = True
            return final_alcancado
        self.labirinto[i][j] = 1
        return final_alcancado

    def busca_elemento(self, lista):
        primeira_coord = None
        segunda_coord = None
        metade_esq = lista[:len(lista)//2]
        metade_dir = lista[len(lista)//2:] 
        """print("coord 1 : ", metade_esq)
        print("coord 2 : ", metade_dir)
        print("coords 1 : ", metade_esq[0])
        print("coords 2 : ", metade_esq[1])"""
        #print("valor da coord 1: ", self.labirinto[metade_esq[0]][metade_esq[1]])
        #print("valor da coord 2: ", self.labirinto[metade_dir[0]][metade_dir[1]])
        
        if(self.labirinto[metade_dir[0]][metade_dir[1]] == 0 or self.labirinto[metade_dir[0]][metade_dir[1]] == 2):
            primeira_coord = self.labirinto[metade_esq[0]][metade_esq[1]]
            segunda_coord = self.labirinto[metade_dir[0]][metade_dir[1]]
        return primeira_coord, segunda_coord
    
    def imprime_matriz(self, linhas, colunas):
        for i in range(linhas):
            for j in range(colunas):
                print("%s " % self.labirinto[i][j], end = " ")
            print()
        
    def insere_e_verifica_coords_na_lista(lista, i, j):
        area_valida = True
        lista = [(i, j - 1, i, j - 2),          #esquerda
                (i - 1 , j, i - 2, j),          #cima
                (i, j + 1, i, j + 2),           #direita 
                (i + 1, j, i + 2, j)]           #baixo
        for i in range(len(lista)):
            x, y = matriz.busca_elemento(lista[i])
            if(x == 1 or y == 1):               #posicao nao e uma parede
                area_valida = False
            for j in range(len(lista)):
                if(lista[i][j] < 0):            #coordenada fora do mapa
                    area_valida = False     
            if(area_valida == True):            #coordenada valida adicionada na lista
                lista_coords.append(lista[i])
            area_valida = True
        escavacao = random.randint(0, len(lista)-1)
        return lista_coords, lista_coords[escavacao], escavacao 

if __name__ == "__main__":
    print("Escolha o número de linhas >= 3 para o labirinto:")
    linhas = int(input()) + 2
    print("Escolha o número de colunas >= 3 para o labirinto:")
    colunas = int(input()) + 2
    print(linhas, colunas)
    #linhas = 9 + 2                              #teste de entrada #+2 para preencher as bordas a fim ajudar na validacao de posicao
    #colunas = 11 + 2                            #teste de entrada #+2 para preencher as bordas a fim ajudar na validacao de posicao
    i = random.randrange(3, linhas, 2) + 1                                   #teste coord inicial de entrada #+1 por causa da adicao da borda
    j = random.randrange(3, colunas, 2) + 1                                   #teste coord inicial de entrada #+1 por causa da adicao da borda
    print(linhas, colunas, i, j)
    lista_coords = []
    matriz = GeraLabirinto(linhas, colunas) 
    matriz.cava_na_posicao(i, j)                #Gera o primeiro ponto
    print("Matriz com a primeira parte escavada:")
    matriz.imprime_matriz(linhas, colunas)
    lista_coords, local_aleatorio_escolhido, area_escavada = matriz.insere_e_verifica_coords_na_lista(i,j)
    print("lista completa: ", lista_coords)
    print("local aleatorio para cavar: ",local_aleatorio_escolhido)
    i = local_aleatorio_escolhido[0]            #Insere os quatro primeiros corredores em lista_coords (inicio)
    j = local_aleatorio_escolhido[1]
    matriz.cava_na_posicao(i, j)
    i = local_aleatorio_escolhido[2]
    j = local_aleatorio_escolhido[3]
    matriz.cava_na_posicao(i, j)                #Insere os quatro primeiros corredores em lista_coords (fim)
    print("Matriz com a primeira fase de escavacao completada:")
    matriz.imprime_matriz(linhas, colunas)
    ######
    repete = 2
    while(lista_coords != []):
        lista_coords.remove(lista_coords[area_escavada])
        lista_coords, local_aleatorio_escolhido, area_escavada = matriz.insere_e_verifica_coords_na_lista(i,j)
        print("lista completa versão ", repete)
        print(lista_coords)
        print("local aleatorio para cavar ", repete)
        print(local_aleatorio_escolhido)
        i = local_aleatorio_escolhido[0]        #Insere os proximos corredores potenciais em lista_coords (inicio)
        j = local_aleatorio_escolhido[1]
        flag = matriz.cava_na_posicao(i, j)
        if(flag == True):
            break
        i = local_aleatorio_escolhido[2]
        j = local_aleatorio_escolhido[3]
        flag = matriz.cava_na_posicao(i, j)     #Insere os proximos corredores potenciais em lista_coords (fim)
        if(flag == True):
            break
        print("Matriz com a fase %s de escavacao completada:" % repete)
        #matriz.imprime_matriz(linhas, colunas)
        repete += 1
    print("Labirinto gerado aleatoriamente com uma unica saida:")
    matriz.imprime_matriz(linhas, colunas)
