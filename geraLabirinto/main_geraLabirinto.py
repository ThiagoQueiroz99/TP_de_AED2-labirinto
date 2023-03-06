import geraLabirinto_13x15 as labirinto

if __name__ == "__main__":
    matriz = labirinto.GeraLabirinto()
    pos_jogador = matriz.campos_iniciais(matriz.i_random, matriz.j_random, matriz.lista_coords)     #insere o primeiro ponto ma matriz #e insere os quatro primeiros corredores na lista
    pos_saida = matriz.escavacao_loop(matriz.i_random, matriz.j_random, matriz.lista_coords)        #enquanto lista nao estiver vazia fica em loop
    matriz.imprime_matriz(matriz.linhas, matriz.colunas)                                            #matriz de um labirinto gerado aleatoriamente com uma unica saida
    armazena_matriz = matriz.pega_matriz()
    print("coords do primeiro campo cavado: ", pos_jogador)                                         #armazena a posicao inicial como sendo a posicao que o jogador vai comecar (auxilia no codigo da interface)
    print("coords da saida: ", pos_saida)                                                           #armazena a posicao da saida (auxilia no codigo da interface)
    print("conteudo matriz armazenada: ", armazena_matriz)                                          #armazena a matriz que vai ser passada para o codigo da interface, para entao gerar o visual do labirinto