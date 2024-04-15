import flet as ft
from model import model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        self._view.txt_result.clean()
        corso = self._view.ddCorsi.value
        if corso is None or corso == "":
            self._view.create_alert("Selezionare un corso")
            return
        for iscrizione in self._model.iscrizioni:
            if corso == iscrizione.codice:
                studente = self._model.searchStudente(iscrizione.matricola)
                self._view.txt_result.controls.append(ft.Text(f"{studente.cognome} {studente.nome} ({studente.matricola})"))
        self._view.update_page()

    def optionsDdCorso(self):
        for corso in self._model.corsi:
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=corso.codice, text=corso.__str__()))
        self._view.update_page()

    def handle_cercaStudente(self, e):
        self._view.txt_name.value = ""
        self._view.txt_surname.value = ""
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        studente = self._model.searchStudente(matricola)
        self._view.txt_name.value = studente.nome
        self._view.txt_surname.value = studente.cognome
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        self._view.txt_name.value = ""
        self._view.txt_surname.value = ""
        self._view.txt_result.clean()
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        studente = self._model.searchStudente(matricola)
        if studente is None:
            self._view.create_alert("Studente inesistente")
            return
        self._view.txt_name.value = studente.nome
        self._view.txt_surname.value = studente.cognome
        self._view.update_page()
        for iscrizione in self._model.iscrizioni:
            if int(matricola) == int(iscrizione.matricola):
                corso = self._model.searchCorso(iscrizione.codice)
                self._view.txt_result.controls.append(ft.Text(f"{corso.nome} ({corso.codice})"))
        self._view.update_page()

    def handle_iscrivi(self, e):
        self._view.txt_name.value = ""
        self._view.txt_surname.value = ""
        self._view.txt_result.clean()
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        studente = self._model.searchStudente(matricola)
        if studente is None:
            self._view.create_alert("Studente inesistente")
            return
        corso = self._view.ddCorsi.value
        if corso is None or corso == "":
            self._view.create_alert("Selezionare un corso")
            return
        self._view.txt_name.value = studente.nome
        self._view.txt_surname.value = studente.cognome
        self._view.update_page()
        iscrizione = self._model.iscrivi(matricola, corso)
        self._view.txt_result.controls.append(ft.Text(iscrizione))
        self._view.update_page()
