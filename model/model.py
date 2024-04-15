from database import corso_DAO
from database import studente_DAO
from database import iscrizioni_DAO


class Model:
    def __init__(self):
        self.corsi = corso_DAO.getCorsi()
        self.studenti = studente_DAO.getStudenti()
        self.iscrizioni = iscrizioni_DAO.getIscrizioni()

    def searchStudente(self, matricola):
        for studente in self.studenti:
            if int(matricola) == int(studente.matricola):
                return studente

    def searchCorso(self, codice):
        for corso in self.corsi:
            if str(codice) == str(corso.codice):
                return corso

    def iscrivi(self, matricola, codice):
        iscrizione = iscrizioni_DAO.setIscrizione(matricola, codice)
        self.iscrizioni = iscrizioni_DAO.getIscrizioni()
        if iscrizione:
            return (f"studente {self.searchStudente(matricola).nome} {self.searchStudente(matricola).cognome} iscritto "
                    f"al corso {self.searchCorso(codice).nome}")
