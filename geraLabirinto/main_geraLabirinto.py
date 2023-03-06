import geraLabirinto_13x15 as labirinto

if __name__ == "__main__":
    matriz = labirinto.GeraLabirinto()
    matriz.campos_iniciais(matriz.i_random, matriz.j_random, matriz.lista_coords)   #insere o primeiro ponto ma matriz #e insere os quatro primeiros corredores na lista
    matriz.escavacao_loop(matriz.i_random, matriz.j_random, matriz.lista_coords)    #enquanto lista nao estiver vazia fica em loop
    matriz.imprime_matriz(matriz.linhas, matriz.colunas)                            #matriz de um labirinto gerado aleatoriamente com uma unica saida