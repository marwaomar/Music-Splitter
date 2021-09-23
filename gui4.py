# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'problem4A.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.split = QtWidgets.QPushButton(self.centralwidget)
        self.split.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"")
        self.split.setObjectName("split")
        self.horizontalLayout_3.addWidget(self.split)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.original = QtWidgets.QPushButton(self.centralwidget)
        self.original.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.original.setObjectName("original")
        self.horizontalLayout.addWidget(self.original)
        self.vocal = QtWidgets.QPushButton(self.centralwidget)
        self.vocal.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"")
        self.vocal.setObjectName("vocal")
        self.horizontalLayout.addWidget(self.vocal)
        self.music = QtWidgets.QPushButton(self.centralwidget)
        self.music.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.music.setObjectName("music")
        self.horizontalLayout.addWidget(self.music)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Song = QtWidgets.QAction(MainWindow)
        self.actionOpen_Song.setObjectName("actionOpen_Song")
        self.menuFile.addAction(self.actionOpen_Song)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#aa007f;\">Splitter</span></p></body></html>"))
        self.split.setText(_translate("MainWindow", "Split"))
        self.original.setText(_translate("MainWindow", "Play Original"))
        self.vocal.setText(_translate("MainWindow", "Play Vocal"))
        self.music.setText(_translate("MainWindow", "Play Music"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Song.setText(_translate("MainWindow", "Open Song"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

