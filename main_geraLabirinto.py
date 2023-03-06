import geraLabirinto_13x15 as labirinto

if __name__ == "__main__":
    matriz = labirinto.GeraLabirinto()
    #armazena a posicao inicial como sendo a posicao que o jogador vai comecar (auxilia no codigo da interface)
    pos_jogador = matriz.campos_iniciais(matriz.i_random, matriz.j_random, matriz.lista_coords)     #insere o primeiro ponto ma matriz #e insere os quatro primeiros corredores na lista
    #armazena a posicao da saida (auxilia no codigo da interface)
    pos_saida = matriz.escavacao_loop(matriz.i_random, matriz.j_random, matriz.lista_coords)        #enquanto lista nao estiver vazia fica em loop
    #armazena a matriz que vai ser passada para o codigo da interface, para entao gerar o visual do labirinto
    armazena_matriz = matriz.pega_matriz()
    matriz.imprime_matriz(matriz.linhas, matriz.colunas)                                            #matriz de um labirinto gerado aleatoriamente com uma unica saida
    print("coords do primeiro campo cavado: ", pos_jogador)                                         
    print("coords da saida: ", pos_saida)                                                           
    print("conteudo matriz armazenada: ", armazena_matriz)      