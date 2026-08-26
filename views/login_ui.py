# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        Dialog.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"font: 75 8pt \"Arial\";\n"
"")
        Dialog.setModal(True)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_top = QFrame(Dialog)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy1)
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_logo = QLabel(self.frame_top)
        self.img_logo.setObjectName(u"img_logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.img_logo.sizePolicy().hasHeightForWidth())
        self.img_logo.setSizePolicy(sizePolicy2)
        self.img_logo.setMaximumSize(QSize(50, 50))
        self.img_logo.setStyleSheet(u"")
        self.img_logo.setPixmap(QPixmap(u":/icons/icons/logo-icon.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setWordWrap(False)

        self.horizontalLayout.addWidget(self.img_logo)

        self.label_title = QLabel(self.frame_top)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(0, 0))
        self.label_title.setTextFormat(Qt.RichText)
        self.label_title.setScaledContents(True)
        self.label_title.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_title)


        self.gridLayout.addWidget(self.frame_top, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(125, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.frame_login = QFrame(Dialog)
        self.frame_login.setObjectName(u"frame_login")
        sizePolicy1.setHeightForWidth(self.frame_login.sizePolicy().hasHeightForWidth())
        self.frame_login.setSizePolicy(sizePolicy1)
        self.frame_login.setMinimumSize(QSize(100, 0))
        self.frame_login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_login = QPushButton(self.frame_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_login)


        self.gridLayout.addWidget(self.frame_login, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.label_username = QLabel(Dialog)
        self.label_username.setObjectName(u"label_username")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy3)
        self.label_username.setMaximumSize(QSize(16777215, 16777215))
        self.label_username.setScaledContents(True)
        self.label_username.setWordWrap(False)

        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 3)

        self.frame_username = QFrame(Dialog)
        self.frame_username.setObjectName(u"frame_username")
        sizePolicy1.setHeightForWidth(self.frame_username.sizePolicy().hasHeightForWidth())
        self.frame_username.setSizePolicy(sizePolicy1)
        self.frame_username.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_username.setFrameShape(QFrame.StyledPanel)
        self.frame_username.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_username)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_username = QLineEdit(self.frame_username)
        self.input_username.setObjectName(u"input_username")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.input_username.sizePolicy().hasHeightForWidth())
        self.input_username.setSizePolicy(sizePolicy4)
        self.input_username.setStyleSheet(u"")
        self.input_username.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.input_username)


        self.gridLayout.addWidget(self.frame_username, 2, 0, 1, 3)

        self.label_pswd = QLabel(Dialog)
        self.label_pswd.setObjectName(u"label_pswd")
        sizePolicy1.setHeightForWidth(self.label_pswd.sizePolicy().hasHeightForWidth())
        self.label_pswd.setSizePolicy(sizePolicy1)
        self.label_pswd.setMaximumSize(QSize(16777215, 16777215))
        self.label_pswd.setTextFormat(Qt.AutoText)
        self.label_pswd.setScaledContents(True)
        self.label_pswd.setWordWrap(False)

        self.gridLayout.addWidget(self.label_pswd, 3, 0, 1, 3)

        self.frame_pswd = QFrame(Dialog)
        self.frame_pswd.setObjectName(u"frame_pswd")
        sizePolicy1.setHeightForWidth(self.frame_pswd.sizePolicy().hasHeightForWidth())
        self.frame_pswd.setSizePolicy(sizePolicy1)
        self.frame_pswd.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_pswd.setFrameShape(QFrame.StyledPanel)
        self.frame_pswd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pswd)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input_pswd = QLineEdit(self.frame_pswd)
        self.input_pswd.setObjectName(u"input_pswd")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.input_pswd.sizePolicy().hasHeightForWidth())
        self.input_pswd.setSizePolicy(sizePolicy5)
        self.input_pswd.setStyleSheet(u"")
        self.input_pswd.setEchoMode(QLineEdit.Password)
        self.input_pswd.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.input_pswd)


        self.gridLayout.addWidget(self.frame_pswd, 4, 0, 1, 3)

        self.label_error = QLabel(Dialog)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy1)
        self.label_error.setMaximumSize(QSize(16777215, 16777215))
        self.label_error.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_error.setScaledContents(False)
        self.label_error.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_error, 6, 0, 1, 3)

        self.label_version = QLabel(Dialog)
        self.label_version.setObjectName(u"label_version")
        sizePolicy1.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy1)
        self.label_version.setScaledContents(True)
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_version, 7, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.img_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Biblioteca Cora Coralina</span><br/>Digite suas credenciais</p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Entrar", None))
        self.label_username.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Nome </span><span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_pswd.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Senha </span><span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.label_error.setText(QCoreApplication.translate("Dialog", u"Erro", None))
        self.label_version.setText(QCoreApplication.translate("Dialog", u"v0.0.0", None))
    # retranslateUi

