from PySide6.QtWidgets import QMainWindow

from views.app_ui import Ui_MainWindow

from utils.constants import SOFTWARE_VERSION

from utils.app_session import AppSession

class View(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Livros")

        self.user = AppSession.current_user()

        self.user_name_label.setText(f"<b>{self.user.name}</b><br>{self.user.role.value.capitalize()}")
        self.version_label.setText(SOFTWARE_VERSION)
    