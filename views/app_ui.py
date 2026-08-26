# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"font: \"Arial\"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.center_widget = QStackedWidget(self.centralwidget)
        self.center_widget.setObjectName(u"center_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_widget.sizePolicy().hasHeightForWidth())
        self.center_widget.setSizePolicy(sizePolicy)
        self.center_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.dashboard_wiget = QWidget()
        self.dashboard_wiget.setObjectName(u"dashboard_wiget")
        self.label_title = QLabel(self.dashboard_wiget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 10, 241, 31))
        self.label_title.setStyleSheet(u"font: 20pt;")
        self.label_title.setScaledContents(True)
        self.center_widget.addWidget(self.dashboard_wiget)
        self.book_wiget = QWidget()
        self.book_wiget.setObjectName(u"book_wiget")
        self.book_wiget.setStyleSheet(u"")
        self.label = QLabel(self.book_wiget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 181, 31))
        self.label.setStyleSheet(u"font: 20pt")
        self.center_widget.addWidget(self.book_wiget)

        self.gridLayout.addWidget(self.center_widget, 1, 1, 1, 1)

        self.left_wiget = QWidget(self.centralwidget)
        self.left_wiget.setObjectName(u"left_wiget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_wiget.sizePolicy().hasHeightForWidth())
        self.left_wiget.setSizePolicy(sizePolicy1)
        self.left_wiget.setMinimumSize(QSize(150, 0))
        self.left_wiget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.left_wiget, 1, 0, 1, 1)

        self.top_wiget = QWidget(self.centralwidget)
        self.top_wiget.setObjectName(u"top_wiget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.top_wiget.sizePolicy().hasHeightForWidth())
        self.top_wiget.setSizePolicy(sizePolicy2)
        self.top_wiget.setMinimumSize(QSize(0, 0))
        self.top_wiget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.top_wiget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.img_logo = QLabel(self.top_wiget)
        self.img_logo.setObjectName(u"img_logo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.img_logo.sizePolicy().hasHeightForWidth())
        self.img_logo.setSizePolicy(sizePolicy3)
        self.img_logo.setMinimumSize(QSize(0, 0))
        self.img_logo.setMaximumSize(QSize(40, 40))
        self.img_logo.setSizeIncrement(QSize(100, 100))
        self.img_logo.setBaseSize(QSize(100, 100))
        self.img_logo.setStyleSheet(u"")
        self.img_logo.setPixmap(QPixmap(u":/icons/icons/logo-icon.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setWordWrap(False)
        self.img_logo.setMargin(0)
        self.img_logo.setIndent(-1)

        self.gridLayout_2.addWidget(self.img_logo, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.frame_search = QFrame(self.top_wiget)
        self.frame_search.setObjectName(u"frame_search")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy4)
        self.frame_search.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_search)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input_search = QLineEdit(self.frame_search)
        self.input_search.setObjectName(u"input_search")
        sizePolicy.setHeightForWidth(self.input_search.sizePolicy().hasHeightForWidth())
        self.input_search.setSizePolicy(sizePolicy)
        self.input_search.setStyleSheet(u"")
        self.input_search.setEchoMode(QLineEdit.Normal)
        self.input_search.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.input_search)


        self.gridLayout_2.addWidget(self.frame_search, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.actions_frame = QFrame(self.top_wiget)
        self.actions_frame.setObjectName(u"actions_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.actions_frame.sizePolicy().hasHeightForWidth())
        self.actions_frame.setSizePolicy(sizePolicy5)
        self.actions_frame.setMinimumSize(QSize(200, 0))
        self.actions_frame.setMaximumSize(QSize(0, 43))
        self.actions_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.img_settings = QLabel(self.actions_frame)
        self.img_settings.setObjectName(u"img_settings")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.img_settings.sizePolicy().hasHeightForWidth())
        self.img_settings.setSizePolicy(sizePolicy6)
        self.img_settings.setMaximumSize(QSize(25, 16777215))
        self.img_settings.setPixmap(QPixmap(u":/icons/icons/gear.png"))
        self.img_settings.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.img_settings)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.img_user = QLabel(self.actions_frame)
        self.img_user.setObjectName(u"img_user")
        self.img_user.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy7.setHorizontalStretch(20)
        sizePolicy7.setVerticalStretch(20)
        sizePolicy7.setHeightForWidth(self.img_user.sizePolicy().hasHeightForWidth())
        self.img_user.setSizePolicy(sizePolicy7)
        self.img_user.setMinimumSize(QSize(0, 0))
        self.img_user.setMaximumSize(QSize(25, 16777215))
        self.img_user.setLayoutDirection(Qt.LeftToRight)
        self.img_user.setAutoFillBackground(False)
        self.img_user.setPixmap(QPixmap(u":/icons/icons/user.png"))
        self.img_user.setScaledContents(True)
        self.img_user.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.img_user.setWordWrap(False)
        self.img_user.setMargin(0)
        self.img_user.setIndent(-1)

        self.horizontalLayout_2.addWidget(self.img_user)

        self.label_user_name = QLabel(self.actions_frame)
        self.label_user_name.setObjectName(u"label_user_name")
        sizePolicy2.setHeightForWidth(self.label_user_name.sizePolicy().hasHeightForWidth())
        self.label_user_name.setSizePolicy(sizePolicy2)
        self.label_user_name.setMinimumSize(QSize(0, 40))
        self.label_user_name.setMaximumSize(QSize(16777215, 16777215))
        self.label_user_name.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_user_name.setLayoutDirection(Qt.LeftToRight)
        self.label_user_name.setTextFormat(Qt.RichText)
        self.label_user_name.setScaledContents(True)
        self.label_user_name.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_user_name.setWordWrap(False)
        self.label_user_name.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_user_name)


        self.gridLayout_2.addWidget(self.actions_frame, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.top_wiget, 0, 0, 1, 3)

        self.bottom_wiget = QWidget(self.centralwidget)
        self.bottom_wiget.setObjectName(u"bottom_wiget")
        sizePolicy2.setHeightForWidth(self.bottom_wiget.sizePolicy().hasHeightForWidth())
        self.bottom_wiget.setSizePolicy(sizePolicy2)
        self.bottom_wiget.setMinimumSize(QSize(0, 20))
        self.bottom_wiget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_wiget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_version = QLabel(self.bottom_wiget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setLayoutDirection(Qt.LeftToRight)
        self.label_version.setStyleSheet(u"")
        self.label_version.setScaledContents(True)
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_version)


        self.gridLayout.addWidget(self.bottom_wiget, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.center_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.img_logo.setText("")
        self.input_search.setText("")
        self.input_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start searching...", None))
        self.img_settings.setText("")
        self.img_user.setText("")
        self.label_user_name.setText(QCoreApplication.translate("MainWindow", u"<b>User Name</b><br>Administrator", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v0.0.0", None))
    # retranslateUi

