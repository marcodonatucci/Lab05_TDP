class Corso:
    def __init__(self, codice, nome, crediti, pd):
        self.nome = nome
        self.codice = codice
        self.crediti = crediti
        self.pd = pd

    def __str__(self):
        return f"{self.nome} ({self.codice})"
