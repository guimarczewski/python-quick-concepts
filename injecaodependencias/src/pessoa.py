class Pessoa:
    def __init__(self, comportamento):
        self.comportamento = comportamento

    def realizarAcao(self):
        self.comportamento.acao()