#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#~ Copyright (C) 2014 Carlos Manuel Ferras Hernandez
#~ This file is part of LF02_package.

#~ LF02_package is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ LF02_package is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with LF02_package.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore, QtGui
from style import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,title,appIcon):
		self.title=title	
		widget=QtGui.QDesktopWidget()
		mainScreenSize = widget.availableGeometry(widget.primaryScreen())
		self.W= mainScreenSize.width()
		H= mainScreenSize.height()		
		MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,self.W,H).size()).expandedTo(MainWindow.minimumSizeHint())) 
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(appIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 23))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menubar.setStyleSheet(MENU_STYLE)	
		self.menuArchivo = QtGui.QMenu(self.menubar)
		self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
		self.menuEditar = QtGui.QMenu(self.menubar)
		self.menuEditar.setObjectName(_fromUtf8("menuEditar"))
		self.menuOpciones = QtGui.QMenu(self.menubar)
		self.menuOpciones.setObjectName(_fromUtf8("menuOpciones"))
		self.menuOpciones_de_GenSec = QtGui.QMenu(self.menuOpciones)
		self.menuOpciones_de_GenSec.setObjectName(_fromUtf8("menuOpciones_de_GenSec"))
		self.menuLanguage = QtGui.QMenu(self.menuOpciones_de_GenSec)
		self.menuLanguage.setObjectName(_fromUtf8("menuLanguage"))
		self.menuAyuda = QtGui.QMenu(self.menubar)
		self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		#Nuevo---------------------------------------------------------
		self.actionNuevo = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionNuevo.setIconVisibleInMenu(True)
		self.actionNuevo.setIcon(icon)
		self.actionNuevo.setShortcut("Ctrl+N")
		self.actionNuevo.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
		#Abrir-------------------------------------------------
		self.actionAbrir = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAbrir.setIconVisibleInMenu(True)
		self.actionAbrir.setIcon(icon)
		self.actionAbrir.setShortcut("Ctrl+O")
		self.actionAbrir.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open an existing file", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
		#Guardar---------------------------------------------------------
		self.actionGurdar = QtGui.QAction(MainWindow)
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionGurdar.setIconVisibleInMenu(True)
		self.actionGurdar.setIcon(icon)
		self.actionGurdar.setShortcut("Ctrl+S")
		self.actionGurdar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save the document to disk", None, QtGui.QApplication.UnicodeUTF8))
		self.actionGurdar.setObjectName(_fromUtf8("actionGurdar"))
		#GuardarComo--------------------------------------
		self.actionGurdar_como = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionGurdar_como.setIconVisibleInMenu(True)
		self.actionGurdar_como.setIcon(icon)
		self.actionGurdar_como.setShortcut("Ctrl+G")
		self.actionGurdar_como.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save the document under a new name", None, QtGui.QApplication.UnicodeUTF8))
		self.actionGurdar_como.setObjectName(_fromUtf8("actionGurdar_como"))
		#Salir--------------------------------------------
		self.actionDfgfh = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionDfgfh.setIconVisibleInMenu(True)
		self.actionDfgfh.setIcon(icon)
		self.actionDfgfh.setShortcut("Escape")
		self.actionDfgfh.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close the application", None, QtGui.QApplication.UnicodeUTF8))
		self.actionDfgfh.setObjectName(_fromUtf8("actionDfgfh"))
		#Pegar--------------------------------------------------
		self.actionPegar = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionPegar.setIconVisibleInMenu(True)
		self.actionPegar.setIcon(icon)
		self.actionPegar.setShortcut("Ctrl+V")
		self.actionPegar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Paste the clipboard content into the current selection", None, QtGui.QApplication.UnicodeUTF8))
		self.actionPegar.setObjectName(_fromUtf8("actionPegar"))
		#Copiar------------------------------------------------------------
		self.actionCopiar = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCopiar.setIconVisibleInMenu(True)
		self.actionCopiar.setIcon(icon)
		self.actionCopiar.setShortcut("Ctrl+C")
		self.actionCopiar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Copy the current selection content to the clipboard", None, QtGui.QApplication.UnicodeUTF8))
		self.actionCopiar.setObjectName(_fromUtf8("actionCopiar"))
		#Cortar---------------------------------------------------
		self.actionCortar = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCortar.setIconVisibleInMenu(True)
		self.actionCortar.setIcon(icon)
		self.actionCortar.setShortcut("Ctrl+X")
		self.actionCortar.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cut the current selection content to the clipboard", None, QtGui.QApplication.UnicodeUTF8))
		self.actionCortar.setObjectName(_fromUtf8("actionCortar"))
		#Ayuda----------------------------------------------------
		self.actionAyuda = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAyuda.setIconVisibleInMenu(True)
		self.actionAyuda.setIcon(icon)
		self.actionAyuda.setShortcut("F1")
		self.actionAyuda.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open the help of the application", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
		#AcercaDe----------------------------------------------------
		self.actionAcerda_de = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAcerda_de.setIconVisibleInMenu(True)
		self.actionAcerda_de.setIcon(icon)
		self.actionAcerda_de.setShortcut("Ctrl+I")
		self.actionAcerda_de.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show information about the application", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAcerda_de.setObjectName(_fromUtf8("actionAcerda_de"))
		#Imprimir-------------------------------------------------
		self.actionImprimir = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionImprimir.setIconVisibleInMenu(True)
		self.actionImprimir.setIcon(icon)
		self.actionImprimir.setShortcut("Ctrl+P")
		self.actionImprimir.setStatusTip(QtGui.QApplication.translate("MainWindow", "Print the current table", None, QtGui.QApplication.UnicodeUTF8))
		self.actionImprimir.setObjectName(_fromUtf8("actionImprimir"))
		#Fuente---------------------------------------------------------
		self.actionFuente = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/font.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionFuente.setIconVisibleInMenu(True)
		self.actionFuente.setIcon(icon)
		self.actionFuente.setShortcut("Ctrl+F")
		self.actionFuente.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the font type and size", None, QtGui.QApplication.UnicodeUTF8))
		self.actionFuente.setObjectName(_fromUtf8("actionFuente"))
		#Directorio por defecto---------------------------------------------------------
		self.actionDir_defecto = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/default_dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionDir_defecto.setIconVisibleInMenu(True)
		self.actionDir_defecto.setIcon(icon)
		self.actionDir_defecto.setShortcut("Ctrl+D")
		self.actionDir_defecto.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the default file location", None, QtGui.QApplication.UnicodeUTF8))
		self.actionDir_defecto.setObjectName(_fromUtf8("actionDir_defecto"))		
		#Window Opacity---------------------------------------------------------
		self.actionOpacity = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/opacity.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionOpacity.setIconVisibleInMenu(True)
		self.actionOpacity.setIcon(icon)
		self.actionOpacity.setShortcut("Ctrl+Y")
		self.actionOpacity.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the opacity of the windows", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpacity.setObjectName(_fromUtf8("actionOpacity"))
		#Ejecutar Comando***
		self.actionEjecutar_Comando = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEjecutar_Comando.setIconVisibleInMenu(True)
		self.actionEjecutar_Comando.setIcon(icon)
		#self.actionEjecutar_Comando.setShortcut("Ctrl+R")
		self.actionEjecutar_Comando.setObjectName(_fromUtf8("actionEjecutar_Comando"))
		#Ejecutar GenRep -------------------------------------------------------------
		self.actionEjecutar_GenRep = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/genrep.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEjecutar_GenRep.setIconVisibleInMenu(True)
		self.actionEjecutar_GenRep.setIcon(icon)
		#self.actionEjecutar_Analyzer.setShortcut("Ctrl+R")
		self.actionEjecutar_GenRep.setObjectName(_fromUtf8("actionEjecutar_GenRep"))
		#Ejecutar GenSec-------------------------------------------------------------
		self.actionEjecutar_GenSec = QtGui.QAction(MainWindow)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/gensec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEjecutar_GenSec.setIconVisibleInMenu(True)
		self.actionEjecutar_GenSec.setIcon(icon)
		#self.actionEjecutar_GenSec.setShortcut("Ctrl+R")
		self.actionEjecutar_GenSec.setObjectName(_fromUtf8("actionEjecutar_GenSec"))

		self.menuArchivo.addAction(self.actionNuevo)
		self.menuArchivo.addAction(self.actionAbrir)
		self.menuArchivo.addAction(self.actionGurdar)
		self.menuArchivo.addAction(self.actionGurdar_como)
		self.menuArchivo.addSeparator()
		self.menuArchivo.addAction(self.actionImprimir)
		self.menuArchivo.addSeparator()
		self.menuArchivo.addAction(self.actionDfgfh)
		self.menuEditar.addSeparator()
		self.menuEditar.addSeparator()
		self.menuEditar.addAction(self.actionPegar)
		self.menuEditar.addAction(self.actionCopiar)
		self.menuEditar.addAction(self.actionCortar)
		self.menuOpciones_de_GenSec.addAction(self.menuLanguage.menuAction())	
		self.menuOpciones_de_GenSec.addAction(self.actionFuente)
		self.menuOpciones_de_GenSec.addAction(self.actionDir_defecto)
		self.menuOpciones_de_GenSec.addAction(self.actionOpacity)
		self.menuOpciones.addAction(self.menuOpciones_de_GenSec.menuAction())
		self.menuOpciones.addSeparator()
		self.menuOpciones.addAction(self.actionEjecutar_GenSec)
		self.menuOpciones.addAction(self.actionEjecutar_Comando)
		self.menuOpciones.addAction(self.actionEjecutar_GenRep)		
		self.menuAyuda.addSeparator()
		self.menuAyuda.addAction(self.actionAyuda)
		self.menuAyuda.addSeparator()
		self.menuAyuda.addAction(self.actionAcerda_de)
		self.menubar.addAction(self.menuArchivo.menuAction())
		self.menubar.addAction(self.menuEditar.menuAction())
		self.menubar.addAction(self.menuOpciones.menuAction())
		self.menubar.addAction(self.menuAyuda.menuAction())

		self.Standar_ToolBar= MainWindow.addToolBar(QtGui.QApplication.translate("MainWindow","Standar Bar"))
		self.Standar_ToolBar.setStyleSheet(TOOLBUTTON_STYLE)
		self.Standar_ToolBar.addAction(self.actionNuevo)
		self.Standar_ToolBar.addAction(self.actionAbrir)
		self.Standar_ToolBar.addAction(self.actionGurdar)
		self.Standar_ToolBar.addAction(self.actionImprimir )
		
		self.Tools_ToolBar= MainWindow.addToolBar(QtGui.QApplication.translate("MainWindow","Tools Bar"))
		self.Tools_ToolBar.setStyleSheet(TOOLBUTTON_STYLE)
		self.Tools_ToolBar.setVisible(False)
		
		self.Applications_ToolBar= MainWindow.addToolBar(QtGui.QApplication.translate("MainWindow","Applications Bar"))
		self.Applications_ToolBar.setStyleSheet(TOOLBUTTON_STYLE)
		self.Applications_ToolBar.addAction(self.actionEjecutar_GenSec)		
		self.Applications_ToolBar.addAction(self.actionEjecutar_Comando)
		self.Applications_ToolBar.addAction(self.actionEjecutar_GenRep)
		

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(self.title)
		self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
		self.menuEditar.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
		self.menuOpciones.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
		self.menuOpciones_de_GenSec.setTitle(QtGui.QApplication.translate("MainWindow", "Se&ttings", None, QtGui.QApplication.UnicodeUTF8))
		self.menuLanguage.setTitle(QtGui.QApplication.translate("MainWindow", "&Select Language", None, QtGui.QApplication.UnicodeUTF8))
		self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
		self.actionNuevo.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAbrir.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
		self.actionGurdar.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
		self.actionGurdar_como.setText(QtGui.QApplication.translate("MainWindow", "Save &as..", None, QtGui.QApplication.UnicodeUTF8))
		self.actionDfgfh.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
		self.actionPegar.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
		self.actionCopiar.setText(QtGui.QApplication.translate("MainWindow", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
		self.actionCortar.setText(QtGui.QApplication.translate("MainWindow", "C&ut", None, QtGui.QApplication.UnicodeUTF8))		
		self.actionAyuda.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAcerda_de.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
		self.actionImprimir.setText(QtGui.QApplication.translate("MainWindow", "Prin&t", None, QtGui.QApplication.UnicodeUTF8))
		self.actionFuente.setText(QtGui.QApplication.translate("MainWindow", "&Font", None, QtGui.QApplication.UnicodeUTF8))
		self.actionDir_defecto.setText(QtGui.QApplication.translate("MainWindow", "&Default Location", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOpacity.setText(QtGui.QApplication.translate("MainWindow", "Window &Opacity", None, QtGui.QApplication.UnicodeUTF8))
		self.actionEjecutar_Comando.setText(QtGui.QApplication.translate("MainWindow", "Run &Command", None, QtGui.QApplication.UnicodeUTF8))
		self.actionEjecutar_GenRep.setText(QtGui.QApplication.translate("MainWindow", "&Report Generator", None, QtGui.QApplication.UnicodeUTF8))
		self.actionEjecutar_GenSec.setText(QtGui.QApplication.translate("MainWindow", "Sequence &Generator", None, QtGui.QApplication.UnicodeUTF8))
		