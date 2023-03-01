from FilaPrioridade import FilaDePrioridade

def algoritiomoA(matrizLab, comeco, objetivo):
    agenda = FilaDePrioridade()
    estadosPassados = []
    estado = (comeco)
    agenda.inserir(estado)
    estadosPassados.append(estado)

    while len(agenda) > 0:
        estado = agenda.retiraPrimeiro()
        if estado == objetivo:
            return estado

def heuristica (atual, objetivo):
    x1=atual[0]
    y1=atual[1]
    x2=objetivo[0]
    y2=objetivo[1]

    dist = abs((x1-x2)) + abs((y1-y2))
    
    return dist
