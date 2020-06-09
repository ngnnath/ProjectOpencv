# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagerie_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys, subprocess
import PIL
from PIL import Image
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot, QString
from PyQt4.QtGui import QFileDialog, QGraphicsScene, QPixmap 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from shutil import copy

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(938, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 611, 511))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        # Show  image
        self.pic = QtGui.QLabel(self.groupBox)
        self.pic.setGeometry(QtCore.QRect(0, 0, 611, 511))
        default = "./IMG/default.png"
        myPixmap=QtGui.QPixmap(os.path.abspath(default))
        my = myPixmap.scaled(self.groupBox.size(), Qt.KeepAspectRatio)
        self.pic.setPixmap(my)
        
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(649, 29, 251, 511))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.filtre1 = QtGui.QPushButton(self.groupBox_2)
        self.filtre1.setGeometry(QtCore.QRect(30, 210, 75, 23))
        self.filtre1.setObjectName(_fromUtf8("filtre1"))
        self.filtre2 = QtGui.QPushButton(self.groupBox_2)
        self.filtre2.setGeometry(QtCore.QRect(30, 250, 75, 23))
        self.filtre2.setObjectName(_fromUtf8("filtre2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(120, 210, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(120, 250, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.select_img = QtGui.QPushButton(self.groupBox_2)
        self.select_img.setGeometry(QtCore.QRect(20, 30, 120, 23))
        self.select_img.setObjectName(_fromUtf8("select_img"))
        
        self.select_dir = QtGui.QPushButton(self.groupBox_2)
        self.select_dir.setGeometry(QtCore.QRect(20, 70, 120, 23))
        self.select_dir.setObjectName(_fromUtf8("select_dir"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 300, 23))
        self.label_6.setObjectName(_fromUtf8("label_6"))
		
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(120, 290, 131, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.filtre3 = QtGui.QPushButton(self.groupBox_2)
        self.filtre3.setGeometry(QtCore.QRect(30, 290, 75, 23))
        self.filtre3.setObjectName(_fromUtf8("filtre3"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(120, 330, 131, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.filtre4 = QtGui.QPushButton(self.groupBox_2)
        self.filtre4.setGeometry(QtCore.QRect(30, 330, 75, 23))
        self.filtre4.setObjectName(_fromUtf8("filtre4"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(120, 370, 131, 21))
        self.label_7.setObjectName(_fromUtf8("label_6"))        
        self.filtre5 = QtGui.QPushButton(self.groupBox_2)
        self.filtre5.setGeometry(QtCore.QRect(30, 370, 75, 23))
        self.filtre5.setObjectName(_fromUtf8("filtre5"))       
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(120, 410, 131, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))        
        self.filtre6 = QtGui.QPushButton(self.groupBox_2)
        self.filtre6.setGeometry(QtCore.QRect(30, 410, 75, 23))
        self.filtre6.setObjectName(_fromUtf8("filtre6"))      
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
			
        self.retranslateUi(MainWindow)
        

        self.current_image_pathname = os.path.abspath(default)
        self.connect_all_signals(MainWindow)

        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Rendu", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Selection", None))
        self.filtre1.setText(_translate("MainWindow", "Filtre1", None))
        self.filtre2.setText(_translate("MainWindow", "Filtre2", None))
        self.label.setText(_translate("MainWindow", "Detection visage", None))
        self.label_2.setText(_translate("MainWindow", "Documentation", None))
        self.select_img.setText(_translate("MainWindow", "Choisir une image", None))
        self.label_4.setText(_translate("MainWindow", "Vacances", None))
        self.filtre3.setText(_translate("MainWindow", "Filtre3", None))
        self.label_5.setText(_translate("MainWindow", "Visage video", None))
        self.label_6.setText(_translate("MainWindow", "....", None))
        self.filtre4.setText(_translate("MainWindow", "Filtre4", None))
        self.label_7.setText(_translate("MainWindow", "Lunette de soleil", None))
        self.filtre5.setText(_translate("MainWindow", "Filtre5", None))
        self.label_8.setText(_translate("MainWindow", "Lunette de soleil video", None))
        self.filtre6.setText(_translate("MainWindow", "Filtre6", None))
        self.select_dir.setText(_translate("MainWindow", "Choisir un répertoire", None))
    

    def default_image(self):
        default = "./IMG/default.png"
        image_display = default
        filename = default.split("/")
        self.label = QLabel(self.centralwidget)
        pixmap = QPixmap(image_display)
        self.label.setPixmap(pixmap)
        self.centralwidget.resize(pixmap.width(),pixmap.height())
        
    def connect_all_signals(self, MainWindow):
        # connect the signals to the slots
        self.select_img.clicked.connect(self.open_file)
        self.select_dir.clicked.connect(self.open_directory)
        self.filtre1.clicked.connect(self.face_detection_image)
        self.filtre2.clicked.connect(self.traitement_document)
        self.filtre3.clicked.connect(self.vacances)
        self.filtre4.clicked.connect(self.face_detection_video)
        self.filtre5.clicked.connect(self.face_detection_eye)
        self.filtre6.clicked.connect(self.face_detection_eye_video)
    @pyqtSlot()
    def open_file(self):
        print('\n  open_file()')
        # Get filename using QFileDialog
        filepath = QFileDialog.getOpenFileName(self.centralwidget, 'Open File', '/')
        self.update_image(filepath)
		
    def open_directory(self):
        print('\n  open_file()')
        # Get filename using QFileDialog
        directory = QFileDialog.getExistingDirectory(self.centralwidget, 'Open File', '/')
        self.current_directory= directory
        self.label_6.setText(_translate("MainWindow",self.current_directory, None))
        print(self.current_directory)   
		
    def update_image(self, filepath):
        print("\n  in update_image()")
        import platform
        if 'Windows' in platform.platform() and '/' in filepath:
            print('\nwindows')
            print('\n update_image filepath:')
            print(filepath)
            print(type(filepath))
            filepath.replace("/", '\\')
            print('filepath:')
            print(filepath)
        self.current_image_pathname = str(QtCore.QString(filepath))
        print("\n update_image update: "+str(self.current_image_pathname))
        image = QImage(filepath)
        img = Image.open(self.current_image_pathname)      
        img.save("temp.png")
		
		# copy du fichier à l'emplacement choisi	
        myPixmap=QtGui.QPixmap(os.path.abspath("./temp.png"))
        my = myPixmap.scaled(self.groupBox.size(), Qt.KeepAspectRatio)
        self.pic.setPixmap(my)

    
    @pyqtSlot()
    def face_detection_video(self):
        """
        Signal for 'face detection video' filter
        """
        print("\n  in face_detection_video()")
        cmd="python filters/filtre_detection_visage-video/face_img.py "
        subprocess.check_output(cmd, shell=True)
        
    @pyqtSlot()
    def face_detection_image(self):
        """
        Signal for 'face detection image' filter
        """
        print("\n  in face_detection_image()")
        print(self.current_image_pathname)
        cmd="python filters/filtre_detection_visage/face_img.py "+self.current_image_pathname
        subprocess.check_output(cmd, shell=True)
        copy("filters/filtre_detection_visage/resultat.png", self.current_directory+"\\resultat.png")
        self.update_image("./filters/filtre_detection_visage/resultat.png")

        
    @pyqtSlot()
    def traitement_document(self):
        """
        Signal for 'Traitement Document' filter
        """
        print("\n  in traitement_document()")
        cmd="py filters/filtre_doc/traitement_document.py "+self.current_image_pathname
        subprocess.check_output(cmd, shell=True)
		#copy du fichier
        copy("filters/filtre_doc/resultat.png", self.current_directory+"\\resultat.png")
	
        self.update_image("./filters/filtre_doc/resultat.png")
        
    @pyqtSlot()
    def vacances(self):
        """
        Signal for 'Vacances' filter
        """
        print("\n  in vacance()")
        print self.current_image_pathname
        
        print(self.current_directory)  
		
		#commande a executer
        batcmd="python ./filters/filtre_vacances/filtre.py "+str(self.current_image_pathname)
        subprocess.check_output(batcmd, shell=True)
		#copy du fichier 
        copy("filters/filtre_vacances/resultat.png", self.current_directory+"\\resultat.png")
	
        self.update_image("./filters/filtre_vacances/resultat.png")

    def face_detection_eye(self):       
        print("\n  in face_detection_eye()")
        print(self.current_image_pathname)
        cmd="python filters/filtre_lunette/eyes_img.py "+self.current_image_pathname
        subprocess.check_output(cmd, shell=True)
        copy("filters/filtre_lunette/resultat.png", self.current_directory+"\\resultat.png")
        self.update_image("./filters/filtre_lunette/resultat.png") 
		
    def face_detection_eye_video(self): 	
        print("\n  in face_detection_eye_video()")
        cmd="python filters/filtre_lunette-video/eyes_img.py "
        subprocess.check_output(cmd, shell=True)	 
		
if __name__ == "__main__":
    import sys, os
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

