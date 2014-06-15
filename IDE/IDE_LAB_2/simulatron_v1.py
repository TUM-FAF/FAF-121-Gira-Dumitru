#!usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, QtOpenGL



try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_App(QtGui.QWidget):
    
    value = 59
    playerx = 170
    playery = 180
    enemy1x = 260
    enemy1y = 20
    enemy2x = 115    
    enemy2y = 32
    hscore = 0
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.pixmap = QtGui.QPixmap("pic.png")
        self.readFile = open("highscore.txt", "r")
        self.HHscore = int(self.readFile.read())
        self.readFile.close()
        self.setupUi(self)
        
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(600, 400)
        App.setWindowIcon(QtGui.QIcon("icon.ico"))
        App.setFixedSize(600, 400)
        self.horizontalLayoutWidget = QtGui.QWidget(App)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 330, 541, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.insertNameLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.insertNameLabel.setFont(font)
        self.insertNameLabel.setObjectName("insertNameLabel")
        self.horizontalLayout_4.addWidget(self.insertNameLabel)
        self.insertName = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.insertName.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.insertName.setFont(font)
        self.insertName.setMaxLength(15)
        self.insertName.setReadOnly(False)
        self.insertName.setObjectName("insertName")
        self.horizontalLayout_4.addWidget(self.insertName)
        self.submitButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_4.addWidget(self.submitButton)
        self.deleteButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_4.addWidget(self.deleteButton)
        self.frame = QtGui.QFrame(App)
        self.frame.setGeometry(QtCore.QRect(416, 40, 156, 231))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.scoreLabel = QtGui.QLabel(self.frame)
        self.scoreLabel.setGeometry(QtCore.QRect(10, 105, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setObjectName("scoreLabel")
        self.timeLabel = QtGui.QLabel(self.frame)
        self.timeLabel.setGeometry(QtCore.QRect(10, 55, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 160, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.highscoreLabel = QtGui.QLabel(self.frame)
        self.highscoreLabel.setGeometry(QtCore.QRect(10, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.highscoreLabel.setFont(font)
        self.highscoreLabel.setObjectName("highscoreLabel")
        self.time = QtGui.QLabel(self.frame)
        self.time.setGeometry(QtCore.QRect(10, 85, 46, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.score = QtGui.QLabel(self.frame)
        self.score.setGeometry(QtCore.QRect(10, 130, 46, 13))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.highscore = QtGui.QLabel(self.frame)
        self.highscore.setGeometry(QtCore.QRect(10, 200, 46, 13))
       
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.highscore.setFont(font)
        self.highscore.setObjectName("highscore")
        self.playerLabel = QtGui.QLabel(self.frame)
        self.playerLabel.setGeometry(QtCore.QRect(10, 10, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName("playerLabel")
        self.player = QtGui.QLabel(self.frame)
        self.player.setGeometry(QtCore.QRect(10, 36, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.player.setFont(font)
        self.player.setStyleSheet("color: rgb(170, 0, 0);")
        self.player.setText("")
        self.player.setObjectName("player")
        self.displayWnd = QtGui.QGraphicsView(App)
        self.displayWnd.setGeometry(QtCore.QRect(29, 40, 381, 261))
        self.displayWnd.setObjectName("displayWnd")
        self.displayWnd.setViewport(QtOpenGL.QGLWidget())
        self.displayWnd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.displayWnd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.displayWnd.setMouseTracking(True)
        self.displayWnd.installEventFilter(self)
        self.header = QtGui.QLabel(App)
        self.header.setGeometry(QtCore.QRect(210, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False) 
        font.setKerning(False)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.resetButton = QtGui.QPushButton(App)
        self.resetButton.setGeometry(QtCore.QRect(416, 280, 156, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.resetButton.setObjectName("resetButton")
       
        
        self.retranslateUi(App)
        #QtCore.QObject.connect(self.insertName, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.player.setText)
        #QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL("clicked()"), self.insertName.clear)
        QtCore.QMetaObject.connectSlotsByName(App)
        
        self.thememusic = QtGui.QSound("EnemyShips.wav")
        self.thememusic.play()
        
        self.highscore.setText(str(self.HHscore))
        self.submitButton.clicked.connect(self.storeName)
        self.resetButton.clicked.connect(self.resetAll)
        self.deleteButton.clicked.connect(self.deleteName)
        self.timer = QtCore.QTimer()
        
        self.scene = QtGui.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 352, 221)
        self.displayWnd.setScene(self.scene)
        gfxPixItem = self.scene.addPixmap(self.pixmap)
        #gfxPixItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.displayWnd.fitInView(gfxPixItem)
        
        self.playerModel = QtGui.QPixmap("player.png")
        self.playergfx = self.scene.addPixmap(self.playerModel)
        self.playergfx.setPos(self.playerx, self.playery)
        self.plrect = self.playerModel.rect()

        self.enemy1 = QtGui.QPixmap("enemy1.png")
        self.enemy1gfx = self.scene.addPixmap(self.enemy1)
        self.enemy1gfx.setPos(self.enemy1x, self.enemy1y)
        
        self.enemy2 = QtGui.QPixmap("enemy2.png")
        self.enemy2gfx = self.scene.addPixmap(self.enemy2)
        self.enemy2gfx.setPos(self.enemy2x, self.enemy2y)
        
             
        
        
    def keyPressEvent(self, event):
        self.playergfx.setPos(self.playerx, self.playery)
        if event.key() == QtCore.Qt.Key_A:
            self.playerx -= 10
            self.hscore += 1
        if event.key() == QtCore.Qt.Key_S:
            self.playery += 10
            self.hscore += 1
        if event.key() == QtCore.Qt.Key_D:
            self.playerx += 10
            self.hscore += 1
        if event.key() == QtCore.Qt.Key_W:
            self.playery -= 10 
            self.hscore += 1
        if event.key() == QtCore.Qt.Key_Delete:
            self.scene.removeItem(self.enemy1gfx)
            self.scene.removeItem(self.enemy2gfx)
        self.score.setText(str(self.hscore))
        return QtGui.QWidget.keyPressEvent(self, event)
            
            
    def cTimer(self):
        
        if self.value >= 10:
            self.time.setText("0:" + str(self.value))
        elif self.value < 10:
            self.time.setText("0:0" + str(self.value))
        self.value = self.value - 1  
        if self.value == -1:
            msg = QtGui.QMessageBox()
            doc = QtGui.QTextDocument()
            doc.setHtml(self.player.text())
            text = doc.toPlainText()
            doc.setHtml(self.score.text())
            text2 = doc.toPlainText()
            msg.setText(text + ", time is up!  Your score is " + text2)
            msg.setWindowTitle("Notification")
            msg.exec()
            self.resetAll()
            
    def deleteName(self):
        if self.insertName.isReadOnly():
            msg = QtGui.QMessageBox()
            msg.setText("Could not delete, because the player is active!")
            msg.setWindowTitle("Error!")
            msg.exec()
        else:
            self.insertName.clear()
            
            
    def retranslateUi(self, App):
        App.setWindowTitle(_translate("App", "Simulatron", None))
        self.insertNameLabel.setText(_translate("App", "Insert your name", None))
        self.submitButton.setText(_translate("App", "Submit", None))
        self.deleteButton.setText(_translate("App", "Delete", None))
        self.scoreLabel.setText(_translate("App", "Score", None))
        self.timeLabel.setText(_translate("App", "Time remained", None))
        self.highscoreLabel.setText(_translate("App", "Highscore", None))
        self.time.setText(_translate("App", "1:00", None))
        self.score.setText(_translate("App", "0", None))
        self.highscore.setText(_translate("App", "0", None))
        self.playerLabel.setText(_translate("App", "Player name", None))
        self.header.setText(_translate("App", "SIMULATRON", None))
        self.resetButton.setText(_translate("App", "RESET ALL", None))
        
    def storeName(self):
        self.timer.stop()
        self.time.setStyleSheet("color: rgb(170, 0, 0);")
        self.value = 59
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.cTimer)
       
        self.timer.start(1000)
        doc = QtGui.QTextDocument()
        doc.setHtml(self.insertName.text())
        text = doc.toPlainText()
        self.player.setText(str(text))
        self.insertName.setReadOnly(1)
        
        self.storeFile = open("highscore.txt", "w")
        if (self.hscore > self.HHscore):
            self.storeFile.write(str(self.hscore))
            self.HHscore = self.hscore
            self.highscore.setText(str(self.hscore))
        else:
            self.storeFile.write(str(self.HHscore))
        self.hscore = 0
        self.score.setText("0")
        self.storeFile.close()
        
        
        
    def resetAll(self):
        self.insertName.clear()
        self.insertName.setReadOnly(0)
        self.score.setText("0")
        self.player.setText(" ")
        self.time.setText("1:00")
        self.value = 59
        self.timer.stop()
        self.time.setStyleSheet("color: rgb(0, 0, 0);")
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Simulatron v1.0.0',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
        
