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
    QSpacerItem, QStackedWidget, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_wiget = QWidget(self.centralwidget)
        self.top_wiget.setObjectName(u"top_wiget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_wiget.sizePolicy().hasHeightForWidth())
        self.top_wiget.setSizePolicy(sizePolicy)
        self.top_wiget.setMinimumSize(QSize(0, 30))
        self.top_wiget.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.horizontalLayout = QHBoxLayout(self.top_wiget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_icon = QLabel(self.top_wiget)
        self.logo_icon.setObjectName(u"logo_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_icon.sizePolicy().hasHeightForWidth())
        self.logo_icon.setSizePolicy(sizePolicy1)
        self.logo_icon.setMinimumSize(QSize(50, 0))
        self.logo_icon.setMaximumSize(QSize(50, 16777215))
        self.logo_icon.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.logo_icon)

        self.horizontalSpacer = QSpacerItem(100, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_bar = QLineEdit(self.top_wiget)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy2)
        self.search_bar.setMinimumSize(QSize(0, 0))
        self.search_bar.setFocusPolicy(Qt.ClickFocus)
        self.search_bar.setFrame(True)
        self.search_bar.setCursorPosition(0)
        self.search_bar.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_bar)

        self.horizontalSpacer_2 = QSpacerItem(100, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.actions_frame = QFrame(self.top_wiget)
        self.actions_frame.setObjectName(u"actions_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.actions_frame.sizePolicy().hasHeightForWidth())
        self.actions_frame.setSizePolicy(sizePolicy3)
        self.actions_frame.setMinimumSize(QSize(200, 0))
        self.actions_frame.setMaximumSize(QSize(200, 16777215))
        self.actions_frame.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.actions_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.notification_icon = QLabel(self.actions_frame)
        self.notification_icon.setObjectName(u"notification_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.notification_icon.sizePolicy().hasHeightForWidth())
        self.notification_icon.setSizePolicy(sizePolicy4)
        self.notification_icon.setMaximumSize(QSize(25, 16777215))
        self.notification_icon.setPixmap(QPixmap(u":/icons/icons/deactive-bell.png"))
        self.notification_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.notification_icon)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.user_picture = QLabel(self.actions_frame)
        self.user_picture.setObjectName(u"user_picture")
        self.user_picture.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(20)
        sizePolicy5.setVerticalStretch(20)
        sizePolicy5.setHeightForWidth(self.user_picture.sizePolicy().hasHeightForWidth())
        self.user_picture.setSizePolicy(sizePolicy5)
        self.user_picture.setMinimumSize(QSize(0, 0))
        self.user_picture.setMaximumSize(QSize(25, 16777215))
        self.user_picture.setLayoutDirection(Qt.LeftToRight)
        self.user_picture.setAutoFillBackground(False)
        self.user_picture.setPixmap(QPixmap(u":/icons/icons/user.png"))
        self.user_picture.setScaledContents(True)
        self.user_picture.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.user_picture.setWordWrap(False)
        self.user_picture.setMargin(0)
        self.user_picture.setIndent(-1)

        self.horizontalLayout_2.addWidget(self.user_picture)

        self.user_name_label = QLabel(self.actions_frame)
        self.user_name_label.setObjectName(u"user_name_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.user_name_label.sizePolicy().hasHeightForWidth())
        self.user_name_label.setSizePolicy(sizePolicy6)
        self.user_name_label.setMinimumSize(QSize(0, 0))
        self.user_name_label.setMaximumSize(QSize(100, 16777215))
        self.user_name_label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.user_name_label.setLayoutDirection(Qt.LeftToRight)
        self.user_name_label.setTextFormat(Qt.RichText)
        self.user_name_label.setScaledContents(True)
        self.user_name_label.setAlignment(Qt.AlignCenter)
        self.user_name_label.setWordWrap(False)
        self.user_name_label.setMargin(0)

        self.horizontalLayout_2.addWidget(self.user_name_label)


        self.horizontalLayout.addWidget(self.actions_frame)


        self.gridLayout.addWidget(self.top_wiget, 0, 0, 1, 3)

        self.left_wiget = QWidget(self.centralwidget)
        self.left_wiget.setObjectName(u"left_wiget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.left_wiget.sizePolicy().hasHeightForWidth())
        self.left_wiget.setSizePolicy(sizePolicy7)
        self.left_wiget.setMinimumSize(QSize(150, 0))
        self.left_wiget.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.gridLayout.addWidget(self.left_wiget, 1, 0, 1, 1)

        self.center_widget = QStackedWidget(self.centralwidget)
        self.center_widget.setObjectName(u"center_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.center_widget.sizePolicy().hasHeightForWidth())
        self.center_widget.setSizePolicy(sizePolicy8)
        self.center_widget.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.dashboard_wiget = QWidget()
        self.dashboard_wiget.setObjectName(u"dashboard_wiget")
        self.label = QLabel(self.dashboard_wiget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 40, 47, 13))
        self.label_2 = QLabel(self.dashboard_wiget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 210, 47, 13))
        self.label_3 = QLabel(self.dashboard_wiget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 90, 111, 16))
        self.center_widget.addWidget(self.dashboard_wiget)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.center_widget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.center_widget, 1, 1, 1, 1)

        self.rigth_wiget = QWidget(self.centralwidget)
        self.rigth_wiget.setObjectName(u"rigth_wiget")
        sizePolicy7.setHeightForWidth(self.rigth_wiget.sizePolicy().hasHeightForWidth())
        self.rigth_wiget.setSizePolicy(sizePolicy7)
        self.rigth_wiget.setMinimumSize(QSize(150, 0))
        self.rigth_wiget.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.gridLayout.addWidget(self.rigth_wiget, 1, 2, 1, 1)

        self.bottom_wiget = QWidget(self.centralwidget)
        self.bottom_wiget.setObjectName(u"bottom_wiget")
        sizePolicy.setHeightForWidth(self.bottom_wiget.sizePolicy().hasHeightForWidth())
        self.bottom_wiget.setSizePolicy(sizePolicy)
        self.bottom_wiget.setMinimumSize(QSize(0, 20))
        self.bottom_wiget.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_wiget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.version_label = QLabel(self.bottom_wiget)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setLayoutDirection(Qt.LeftToRight)
        self.version_label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.version_label.setScaledContents(True)
        self.version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.version_label)


        self.gridLayout.addWidget(self.bottom_wiget, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.center_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_icon.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50e Search for book, user or loan", None))
        self.notification_icon.setText("")
        self.user_picture.setText("")
        self.user_name_label.setText(QCoreApplication.translate("MainWindow", u"<b>User Name</b><br>Administrator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"v1.03", None))
    # retranslateUi

