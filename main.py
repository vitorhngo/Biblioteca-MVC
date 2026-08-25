"""
Ponto de entrada da aplicação Biblioteca (MVC em Python).

Executa:
    python main.py
"""
import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication

# Garante que os arquivos gerados pelo Qt Designer (app_ui.py, icons_rc.py, etc.)
# sejam sempre encontrados, não importa de onde o main.py for executado.
sys.path.insert(0, str(Path(__file__).parent / "views"))
sys.path.insert(0, str(Path(__file__).parent / "views" / "icons"))
sys.path.insert(0, os.path.dirname(__file__))

from database.db import initialize_db

from views.app_view import View
from views.login_view import LoginView

def main() -> None:
    initialize_db()

    app = QApplication(sys.argv)

    login_dialog = LoginView()

    if login_dialog.exec() == LoginView.Accepted: #ignore error "Accepted" is unknown
        view = View()
        view.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
