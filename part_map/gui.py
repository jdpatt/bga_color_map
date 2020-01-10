# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from part_map.view import PartViewer
from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QUrl
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDocumentMode(False)
        self.actionSave_as_Image = QAction(MainWindow)
        self.actionSave_as_Image.setObjectName("actionSave_as_Image")
        self.actionSave_as_Json = QAction(MainWindow)
        self.actionSave_as_Json.setObjectName("actionSave_as_Json")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRotate = QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionRotate.setCheckable(False)
        self.actionToggle_Shape = QAction(MainWindow)
        self.actionToggle_Shape.setObjectName("actionToggle_Shape")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.view = PartViewer(self.centralwidget)
        self.view.setObjectName("view")

        self.gridLayout.addWidget(self.view, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.actionSave_as_Image)
        self.menuFile.addAction(self.actionSave_as_Json)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionRotate)
        self.menuOptions.addAction(self.actionToggle_Shape)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Part Map", None))
        self.actionSave_as_Image.setText(
            QCoreApplication.translate("MainWindow", "Save as Image", None)
        )
        self.actionSave_as_Image.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+A", None)
        )
        self.actionSave_as_Json.setText(
            QCoreApplication.translate("MainWindow", "Save as Json", None)
        )
        self.actionSave_as_Json.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Q", None))
        self.actionRotate.setText(QCoreApplication.translate("MainWindow", "Rotate", None))
        self.actionRotate.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+R", None))
        self.actionToggle_Shape.setText(
            QCoreApplication.translate("MainWindow", "Toggle Shape", None)
        )
        self.actionToggle_Shape.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+T", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", "&Options", None))

    # retranslateUi