from PySide6.QtWidgets import QMainWindow

from views.app_ui import Ui_MainWindow, QIcon

from utils.constants import SOFTWARE_VERSION

from utils.app_session import AppSession

class View(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Biblioteca Cora Coralina")
        self.setWindowIcon(QIcon(":/icons/icons/logo-icon.png"))

        self.user = AppSession.current_user()

        self.label_user_name.setText(f"<b>{self.user.name}</b><br>{self.user.role.capitalize()}")
        self.label_version.setText(SOFTWARE_VERSION)
    