import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddCorsi = ft.Dropdown(label="Corso", hint_text="Seleziona un corso", width=600)
        self.controller.optionsDdCorso()
        self.btn_hello = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.ddCorsi, self.btn_hello], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            read_only=True
        )
        self.txt_surname = ft.TextField(
            label="surname",
            width=200,
            read_only=True
        )
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="Insert your matricola"
        )

        row2 = ft.Row([self.txt_matricola, self.txt_name, self.txt_surname],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cercaStudente)
        self.btn_cercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handle_cercaCorsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        row3 = ft.Row([self.btn_cercaStudente, self.btn_cercaCorsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

