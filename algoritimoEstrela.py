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
