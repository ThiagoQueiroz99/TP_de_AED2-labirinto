class Pares:
    def __init__(self, chave, carga):
        self.chave = chave
        self.carga = carga 
            
    def __lt__(self,outro):
        return self.chave < outro.chave
    
    def __repr__(self):
            return self.carga
        
def min_heapify(vetor,tam,i):
    menor=i
    filhoEsq=(2*i)+1
    filhoDir=(2*i)+2
    if filhoEsq < tam and vetor[filhoEsq]<vetor[menor]:
        menor = filhoEsq
    if filhoDir < tam and vetor[filhoDir]<vetor[menor]:
        menor = filhoDir
    if menor!=i:
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
        min_heapify(vetor,tam,menor)


def inserir(vetor, valor):
    if len(vetor) == 0:
        vetor.append(valor)
    else:
        vetor.append(valor)
        for i in range((len(vetor) // 2) - 1, -1, -1):
            min_heapify(vetor, len(vetor), i)


def deletar(vetor, num):
    i = 0
    for i in range(0, len(vetor)):
        if num == vetor[i]:
            break
    vetor[i], vetor[len(vetor) - 1] = vetor[len(vetor) - 1], vetor[i]

    vetor.remove(len(vetor) - 1)

    for i in range((len(vetor) // 2) - 1, -1, -1):
        min_heapify(vetor, len(vetor), i)


fila = []
paresLista=[Pares(3,'resistance'),Pares(2,'are'),Pares(3,'futile'),Pares(1,'we'),Pares(2,'is'),Pares(2,'borg')]

for i in range(len(paresLista)):
    inserir(fila,paresLista[i])
for i in range(len(fila)):
    print(fila[i])
