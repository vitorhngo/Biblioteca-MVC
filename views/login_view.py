from PySide6.QtWidgets import QDialog
from views.login_ui import Ui_Dialog  # Arquivo gerado pelo pyside6-uic
#from controllers.user_controller import UserController

from utils.constants import SOFTWARE_VERSION

from controllers.auth_controller import AuthController
from utils.app_session import AppSession

class LoginView(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Configurações iniciais
        self.ui.label_error.setText("")
        self.ui.label_version.setText(SOFTWARE_VERSION)

        # Conectar botões aos métodos
        self.ui.btn_login.clicked.connect(self.handle_login)


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

        '''
        # Busca a lista de usuários através do UserController
        response = UserController.list_all()

        if response["success"]:
            users = response["data"]
            # Valida se existe algum usuário com nome e password correspondentes
            authenticated_user = next(
                (
                    u
                    for u in users
                    if u.get("name") == username and u.get("password") == password
                ),
                None,
            )

            if authenticated_user:
                self.accept()  # Fecha a tela de login confirmando o acesso (QDialog.Accepted)
            else:
                self.ui.label_error.setText("Usuário ou e-mail incorretos.")
        else:
            self.ui.label_error.setText("Erro ao conectar com a base de dados.")
        '''