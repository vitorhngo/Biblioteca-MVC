from PySide6.QtWidgets import QDialog
from views.login_ui import Ui_Dialog, QIcon  # Arquivo gerado pelo pyside6-uic
#from controllers.user_controller import UserController

from utils.constants import SOFTWARE_VERSION

from controllers.auth_controller import AuthController
from utils.app_session import AppSession

class LoginView(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icons/logo-icon.png"))

        # Configurações iniciais
        self.ui.label_error.setText("")
        self.ui.label_version.setText(SOFTWARE_VERSION)

        # Conectar botões aos métodos
        self.ui.btn_login.clicked.connect(self.handle_login)

        AuthController.create_adm_user()


    def handle_login(self):
        username = self.ui.input_username.text().strip().upper()
        password = self.ui.input_pswd.text().strip()

        if not username or not password:
            self.ui.label_error.setText(
                "Preencha todos os campos obrigatórios."
            )
            return

        result = AuthController.login(username, password)
        
        if result["success"]:
            self.accept()
            AppSession.login(result["data"])
        else:
            self.ui.label_error.setText(result["error"])