class FilaDePrioridade:
    def __init__(self):
        self.fila = []
        
    def inserir(self, elemento):
        if len(self.fila) == 0:
            self.fila.append(elemento)
        else:
            self.fila.append(elemento)
            for i in range((len(self.fila) // 2) - 1, -1, -1):
                self.min_heapify(self.fila, len(self.fila), i)

    def min_heapify(self, vetor, tam, i):
        menor = i
        filhoEsq = (2*i)+1
        filhoDir = (2*i)+2
        if filhoEsq < tam and vetor[filhoEsq] < vetor[menor]:
            menor = filhoEsq
        if filhoDir < tam and vetor[filhoDir] < vetor[menor]:
            menor = filhoDir
        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            self.min_heapify(vetor, tam, menor)

    def retiraPrimeiro(self):
        primeiro = self.fila[0]
        self.fila.remove(self.fila[0])
        return primeiro

    def aumentar_chave(self, pos, novo):
        if (pos == len(self.fila)):
            self.fila.append(novo)
        else:
            novo,self.fila[pos]=self.fila[pos],novo

