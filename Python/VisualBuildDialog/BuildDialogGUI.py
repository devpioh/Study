import sys
from PyQt5.QtWidgets import (QWidget, QInputDialog, QFileDialog, 
QLineEdit, QCheckBox, QComboBox, QGridLayout, QPushButton, QGroupBox, 
QHBoxLayout, QVBoxLayout, QLabel)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

class DirectoryPathEditBox(QWidget):

    def __init__(self, parent, title, width, height):
        super().__init__()
        self.path = ''
        self.group = QGroupBox(title)
        self.group.setParent(parent)
        self.group.resize(width, height)
        self.group.move(10, 10)

        self.hBoxLayout = QHBoxLayout()
        
        self.pathField = QLineEdit(self)
        self.pathField.resize(300, 20)
        self.hBoxLayout.addWidget(self.pathField)

        self.getPathButton = QPushButton('...', self)
        self.getPathButton.resize(30, 20)
        self.getPathButton.clicked.connect(self.onClick_getPathButton)
        self.hBoxLayout.addWidget(self.getPathButton)
        
        self.group.setLayout(self.hBoxLayout)

    @pyqtSlot()
    def onClick_getPathButton(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.pathField.setText(self.path)



class VersionCodeGroup(QGroupBox):
    
    def __init__(self, parent, title, x, y, width, height):
        super().__init__()
        self.setParent(parent)
        self.setTitle(title)
        self.setGeometry(x, y, width, height)
        
        versionLayout = QVBoxLayout()

        intVersionLayout = QHBoxLayout()
        lbl_intVersion = QLabel("번들 버전 코드(숫자) : ")
        self.intVersionEditBox = QLineEdit(self)
        self.intVersionEditBox.setInputMask("999")
        self.intVersionEditBox.setAlignment(Qt.AlignCenter)
        intVersionLayout.addWidget(lbl_intVersion)
        intVersionLayout.addWidget(self.intVersionEditBox)

        strVersionLayout = QHBoxLayout()
        lbl_strVersion = QLabel("번들 버전 (문자) : ")
        self.strVersionEditBox = QLineEdit(self)
        self.strVersionEditBox.setAlignment(Qt.AlignCenter)
        strVersionLayout.addWidget(lbl_strVersion)
        strVersionLayout.addWidget(self.strVersionEditBox)
        
        versionLayout.addLayout(intVersionLayout)
        versionLayout.addLayout(strVersionLayout)

        self.setLayout(versionLayout)




class BuildOptionGroup(QGroupBox):
    
    def __init__(self, parent, title, x, y, width, height):
        super().__init__()

        self.setParent(parent)
        self.setTitle(title)
        self.setGeometry(x, y, width, height)
        
        vLayout = QVBoxLayout()
        self.makeSvnComboBox(vLayout)
        self.makeBuildModeComboBox(vLayout)
        self.makeGprestoComboBox(vLayout)
        self.makeAdjustComboBox(vLayout)
        self.makeServerModeCheckBox(vLayout)
        
        self.setLayout(vLayout)

    def makeSvnComboBox(self, layout):
        svnUpdateLayout = QHBoxLayout()
        lbl_svnUpdate = QLabel("빌드 전 svn 업데이트 : ")
        svnCombo = QComboBox()
        svnCombo.addItem("Yes")
        svnCombo.addItem("No")
        svnUpdateLayout.addWidget(lbl_svnUpdate)
        svnUpdateLayout.addWidget(svnCombo)
        layout.addLayout( svnUpdateLayout )

    def makeBuildModeComboBox(self, layout):
        buildModeLayout = QHBoxLayout()
        lbl_buildMode = QLabel("빌드 모드 : ")
        buildCombo = QComboBox()
        buildCombo.addItem("Debug")
        buildCombo.addItem("Release")
        buildCombo.addItem("All")
        buildModeLayout.addWidget(lbl_buildMode)
        buildModeLayout.addWidget(buildCombo)
        layout.addLayout( buildModeLayout )

    def makeGprestoComboBox(self, layout):
        gprestoModeLayout = QHBoxLayout()
        lbl_gprestoMode = QLabel("G-presto 모드 : ")
        gprestoCombo = QComboBox()
        gprestoCombo.addItem("Debug")
        gprestoCombo.addItem("Release")
        gprestoModeLayout.addWidget(lbl_gprestoMode)
        gprestoModeLayout.addWidget(gprestoCombo)
        layout.addLayout( gprestoModeLayout )

    def makeAdjustComboBox(self, layout):
        adjustModeLayout = QHBoxLayout()
        lbl_adjustMode = QLabel("Adjust 모드 : ")
        adjustCombo = QComboBox()
        adjustCombo.addItem("Debug")
        adjustCombo.addItem("Release")
        adjustModeLayout.addWidget(lbl_adjustMode)
        adjustModeLayout.addWidget(adjustCombo)
        layout.addLayout( adjustModeLayout )

    def makeServerModeCheckBox(self, layout):
        serverModelayout = QGridLayout()
        serverModelayout.addWidget( QLabel("DEV"), 0, 1, Qt.AlignCenter )
        serverModelayout.addWidget( QLabel("ALPHA"), 0, 2, Qt.AlignCenter )
        serverModelayout.addWidget( QLabel("REAL"), 0, 3, Qt.AlignCenter )
        serverModelayout.addWidget( QLabel("서버 :"), 1, 0, Qt.AlignRight )
        serverModelayout.addWidget( QCheckBox(), 1, 1, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 1, 2, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 1, 3, Qt.AlignCenter )
        serverModelayout.addWidget( QLabel("G-presto :"), 2, 0, Qt.AlignRight )
        serverModelayout.addWidget( QCheckBox(), 2, 1, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 2, 2, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 2, 3, Qt.AlignCenter )
        serverModelayout.addWidget( QLabel("Adjust :"), 3, 0, Qt.AlignRight )
        serverModelayout.addWidget( QCheckBox(), 3, 1, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 3, 2, Qt.AlignCenter )
        serverModelayout.addWidget( QCheckBox(), 3, 3, Qt.AlignCenter )
        layout.addLayout(serverModelayout)