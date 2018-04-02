import sys
import os
import ctypes

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from BuildDialogGUI import DirectoryPathEditBox, VersionCodeGroup, BuildOptionGroup

class PoolTimeBuildDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PoolTime Build Dialog'
        self.left = 200
        self.top = 200
        self.width = 340
        self.height = 550
        self.setFixedSize( 320, 500 )
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #make editBox, get project Path
        self.projectPathEditBox = DirectoryPathEditBox(self,"PoolTime 프로젝트 경로", 300, 80)

        #make editBox, input version
        self.versionCodeGroup = VersionCodeGroup(self, "버전", 10, 80, 300, 100)

        #make mode option
        self.buildOptionGroup = BuildOptionGroup(self, "빌드 옵션", 10, 170, 300, 260)

        #make build button
        buildButton = QPushButton("빌드 시작", self)
        buildButton.setGeometry(10, 430, 300, 60)
        buildButton.clicked.connect(self.onClick_Build)

        self.show()

    @pyqtSlot()
    def onClick_Build(self):
        messageResult = QMessageBox.question( self, "PoolTime Build", "Do you want Build?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if messageResult == QMessageBox.Yes :
            self.saveSettings()


    def loadPrevSetting(self):
        print("load prev setting")

    def saveSettings(self):
        print("save prev setting")

        try:
            #f = open(r'BuildSetting.txt', 'w')
            f = None
        except Exception as err:
            expcetMsg = QMessageBox.critical(self, "file read / write error", str(err), QMessageBox.Ok )
        finally:
            f.write( "[ProjectPath] : " + self.projectPathEditBox.path + "\n")
            f.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PoolTimeBuildDialog()
    sys.exit(app.exec_())
