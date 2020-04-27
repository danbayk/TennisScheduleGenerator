# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
import random
import os

players = []

class Players:
    def __init__(self, name):
        self.name = name
        self.playedWith = []

    def addPlayer(self, player):
        self.playedWith.append(player)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(290, 160, 111, 31))
        self.Button1.setObjectName("Button1")
        self.addPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.addPlayer.setGeometry(QtCore.QRect(290, 50, 111, 31))
        self.addPlayer.setObjectName("addPlayer")
        self.deletePlayer = QtWidgets.QPushButton(self.centralwidget)
        self.deletePlayer.setGeometry(QtCore.QRect(290, 90, 111, 31))
        self.deletePlayer.setObjectName("deletePlayer")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit8.setGeometry(QtCore.QRect(30, 260, 113, 20))
        self.lineEdit8.setObjectName("lineEdit8")
        self.lineEdit7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit7.setGeometry(QtCore.QRect(30, 230, 113, 20))
        self.lineEdit7.setObjectName("lineEdit7")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(30, 200, 113, 20))
        self.lineEdit6.setObjectName("lineEdit6")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(30, 170, 113, 20))
        self.lineEdit5.setObjectName("lineEdit5")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(30, 140, 113, 20))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(30, 110, 113, 20))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit9.setGeometry(QtCore.QRect(30, 290, 113, 20))
        self.lineEdit9.setObjectName("lineEdit9")
        self.lineEdit10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit10.setGeometry(QtCore.QRect(30, 320, 113, 20))
        self.lineEdit10.setObjectName("lineEdit10")
        self.lineEdit11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit11.setGeometry(QtCore.QRect(30, 350, 113, 20))
        self.lineEdit11.setObjectName("lineEdit11")
        self.lineEdit15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit15.setGeometry(QtCore.QRect(160, 110, 113, 20))
        self.lineEdit15.setObjectName("lineEdit15")
        self.lineEdit12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit12.setGeometry(QtCore.QRect(30, 380, 113, 20))
        self.lineEdit12.setObjectName("lineEdit12")
        self.lineEdit14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit14.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.lineEdit14.setObjectName("lineEdit14")
        self.lineEdit13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit13.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.lineEdit13.setObjectName("lineEdit13")
        self.lineEdit16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit16.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.lineEdit16.setObjectName("lineEdit16")
        self.roundsLabel = QtWidgets.QLabel(self.centralwidget)
        self.roundsLabel.setGeometry(QtCore.QRect(290, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.roundsLabel.setFont(font)
        self.roundsLabel.setObjectName("roundsLabel")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 130, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.lineEdit18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit18.setGeometry(QtCore.QRect(160, 200, 113, 20))
        self.lineEdit18.setObjectName("lineEdit18")
        self.lineEdit20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit20.setGeometry(QtCore.QRect(160, 260, 113, 20))
        self.lineEdit20.setObjectName("lineEdit20")
        self.lineEdit17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit17.setGeometry(QtCore.QRect(160, 170, 113, 20))
        self.lineEdit17.setObjectName("lineEdit17")
        self.lineEdit19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit19.setGeometry(QtCore.QRect(160, 230, 113, 20))
        self.lineEdit19.setObjectName("lineEdit19")
        self.lineEdit21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit21.setGeometry(QtCore.QRect(160, 290, 113, 20))
        self.lineEdit21.setObjectName("lineEdit21")
        self.lineEdit22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit22.setGeometry(QtCore.QRect(160, 320, 113, 20))
        self.lineEdit22.setObjectName("lineEdit22")
        self.lineEdit23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit23.setGeometry(QtCore.QRect(160, 350, 113, 20))
        self.lineEdit23.setObjectName("lineEdit23")
        self.lineEdit24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit24.setGeometry(QtCore.QRect(160, 380, 113, 20))
        self.lineEdit24.setObjectName("lineEdit24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit9.hide()
        self.lineEdit10.hide()
        self.lineEdit11.hide()
        self.lineEdit12.hide()
        self.lineEdit13.hide()
        self.lineEdit14.hide()
        self.lineEdit15.hide()
        self.lineEdit16.hide()
        self.lineEdit17.hide()
        self.lineEdit18.hide()
        self.lineEdit19.hide()
        self.lineEdit20.hide()
        self.lineEdit21.hide()
        self.lineEdit22.hide()
        self.lineEdit23.hide()
        self.lineEdit24.hide()

        self.Button1.clicked.connect(self.buttonClicked)
        self.addPlayer.clicked.connect(self.addPlayerClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "Generate List"))
        self.addPlayer.setText(_translate("MainWindow", "Add Player"))
        self.deletePlayer.setText(_translate("MainWindow", "Remove Player"))
        self.label.setText(_translate("MainWindow", "Players"))
        self.roundsLabel.setText(_translate("MainWindow", "Rounds:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def buttonClicked(self):
        if self.lineEdit.text() == "":
            pass
        else:
            p1 = Players(self.lineEdit.text())
            self.addToArray(p1)
        if self.lineEdit2.text() == "":
            pass
        else:
            p2 = Players(self.lineEdit2.text())
            self.addToArray(p2)
        if self.lineEdit3.text() == "":
            pass
        else:
            p3 = Players(self.lineEdit3.text())
            self.addToArray(p3)
        if self.lineEdit4.text() == "":
            pass
        else:
            p4 = Players(self.lineEdit4.text())
            self.addToArray(p4)
        if self.lineEdit5.text() == "":
            pass
        else:
            p5 = Players(self.lineEdit5.text())
            self.addToArray(p5)
        if self.lineEdit6.text() == "":
            pass
        else:
            p6 = Players(self.lineEdit6.text())
            self.addToArray(p6)
        if self.lineEdit7.text() == "":
            pass
        else:
            p7 = Players(self.lineEdit7.text())
            self.addToArray(p7)
        if self.lineEdit8.text() == "":
            pass
        else:
            p8 = Players(self.lineEdit8.text())
            self.addToArray(p8)
        if self.lineEdit9.text() == "":
            pass
        else:
            p9 = Players(self.lineEdit9.text())
            self.addToArray(p9)
        if self.lineEdit10.text() == "":
            pass
        else:
            p10 = Players(self.lineEdit10.text())
            self.addToArray(p10)
        if self.lineEdit11.text() == "":
            pass
        else:
            p11 = Players(self.lineEdit11.text())
            self.addToArray(p11)
        if self.lineEdit12.text() == "":
            pass
        else:
            p12 = Players(self.lineEdit12.text())
            self.addToArray(p12)
        if self.lineEdit13.text() == "":
            pass
        else:
            p13 = Players(self.lineEdit13.text())
            self.addToArray(p13)
        if self.lineEdit14.text() == "":
            pass
        else:
            p14 = Players(self.lineEdit14.text())
            self.addToArray(p14)
        if self.lineEdit15.text() == "":
            pass
        else:
            p15 = Players(self.lineEdit15.text())
            self.addToArray(p15)
        if self.lineEdit16.text() == "":
            pass
        else:
            p16 = Players(self.lineEdit16.text())
            self.addToArray(p16)
        if self.lineEdit17.text() == "":
            pass
        else:
            p17 = Players(self.lineEdit17.text())
            self.addToArray(p17)
        if self.lineEdit18.text() == "":
            pass
        else:
            p18 = Players(self.lineEdit18.text())
            self.addToArray(p18)
        if self.lineEdit19.text() == "":
            pass
        else:
            p19 = Players(self.lineEdit19.text())
            self.addToArray(p19)
        if self.lineEdit19.text() == "":
            pass
        else:
            p20 = Players(self.lineEdit20.text())
            self.addToArray(p20)
        if self.lineEdit21.text() == "":
            pass
        else:
            p21 = Players(self.lineEdit21.text())
            self.addToArray(p21)
        if self.lineEdit22.text() == "":
            pass
        else:
            p22 = Players(self.lineEdit22.text())
            self.addToArray(p22)
        if self.lineEdit23.text() == "":
            pass
        else:
            p23 = Players(self.lineEdit23.text())
            self.addToArray(p23)
        if self.lineEdit24.text() == "":
            pass
        else:
            p24 = Players(self.lineEdit24.text())
            self.addToArray(p24)

        self.playerScramble()
        print(players)

    def addToArray(self, p):
        players.append(p)

    def addPlayerClick(self):
        if self.lineEdit9.isHidden():
            self.lineEdit9.show()
            self.lineEdit10.show()
            self.lineEdit11.show()
            self.lineEdit12.show()
            return
        if self.lineEdit13.isHidden():
            self.lineEdit13.show()
            self.lineEdit14.show()
            self.lineEdit15.show()
            self.lineEdit16.show()
            return
        if self.lineEdit17.isHidden():
            self.lineEdit17.show()
            self.lineEdit18.show()
            self.lineEdit19.show()
            self.lineEdit20.show()
            return
        if self.lineEdit21.isHidden():
            self.lineEdit21.show()
            self.lineEdit22.show()
            self.lineEdit23.show()
            self.lineEdit24.show()

    def playerScramble(self):
        fh = open("playersList.txt", "w")
        rounds = self.spinBox.value()
        random.shuffle(players)
        for x in range(rounds):
            y = 0
            courtCount1 = 1
            while y < len(players):
                if y % 2 == 0:
                    if players[y + 1] in players[y].playedWith:
                        random.shuffle(players)
                        y = 0
                    else:
                        y += 1
                else:
                    if players[y - 1] in players[y].playedWith:
                        random.shuffle(players)
                        y = 0
                    else:
                        y += 1
            y = 0
            for z in players:
                if y % 2 == 0:
                    players[y].addPlayer(players[y + 1])
                    y += 1

                else:
                    players[y].addPlayer(players[y - 1])
                    y += 1
            j = 0
            courtCount = str(courtCount1)
            if len(players) == 8:
                while j != len(players):
                    fh.write("Court: " + courtCount + "||    " + players[j].name + ", " + players[j + 1].name + "   -VS-   " + players[j + 2].name + ", " + players[j + 3].name + "    ||    ")
                    j += 4
                    courtCount1 += 1
                    courtCount = str(courtCount1)
                fh.write("\n------------------------------------------------------------------------------------")
                fh.write("------------------------------------------------------------------------------------\n")
            if len(players) == 12:
                while j != len(players):
                    fh.write("Court: " + courtCount + "||     " + players[j].name + ", " + players[j + 1].name + "   -VS-   " + players[j + 2].name + ", " + players[j + 3].name + "    ||    ")
                    j += 4
                    courtCount1 += 1
                    courtCount = str(courtCount1)
                fh.write("\n------------------------------------------------------------------------------------")
                fh.write("------------------------------------------------------------------------------------\n")
            if len(players) == 16:
                while j != len(players):
                    fh.write("Court: " + courtCount + "||     " + players[j].name + ", " + players[j + 1].name + "   -VS-   " + players[j + 2].name + ", " + players[j + 3].name + "    ||    ")
                    j += 4
                    courtCount1 += 1
                    courtCount = str(courtCount1)
                fh.write("\n------------------------------------------------------------------------------------")
                fh.write("------------------------------------------------------------------------------------\n")
            if len(players) == 20:
                while j != len(players):
                    fh.write("Court: " + courtCount + "||     " + players[j].name + ", " + players[j + 1].name + "   -VS-   " + players[j + 2].name + ", " + players[j + 3].name + "    ||    ")
                    j += 4
                    courtCount1 += 1
                    courtCount = str(courtCount1)
                fh.write("\n------------------------------------------------------------------------------------")
                fh.write("------------------------------------------------------------------------------------\n")
            if len(players) == 24:
                while j != len(players):
                    fh.write("Court: " + courtCount + "||     " + players[j].name + ", " + players[j + 1].name + "   -VS-   " + players[j + 2].name + ", " + players[j + 3].name + "    ||    ")
                    j += 4
                    courtCount1 += 1
                    courtCount = str(courtCount1)
                fh.write("\n------------------------------------------------------------------------------------")
                fh.write("------------------------------------------------------------------------------------\n")
        os.startfile("playersList.txt")

        fh.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
