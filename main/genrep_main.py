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


import os
import re
from Lienzo import *

import threading
from gensec_base import *
import time
import datetime

from Dialogs.operationsWid import operationsWid 
from Dialogs.fontSelect import fontS 
from Dialogs.priview import priview
from Dialogs.process import eslWin,irraWin,ilumWin,lmosWin,oslWin,pauseWin,poslWin,pre_heatWin, tlWin
from GenSecLib import createXML,loadXML

class UI_GenRep(UI_GenSec_Base):
	def __init__(self,config,dir=False,parent=None):
		UI_GenSec_Base.__init__(self,config,'GenRep','pixmaps/genrep.png',dir)

		X=[1,5,10,15,16,20,40]
		Y=[1000,200,100,66.4,62.5,50,25]
		self.create_graphic(X,Y)

		self.header=self.treeWidget.header()			
		self.header.setClickable(True)
		self.header.setStyleSheet(HEADER)	
		
		self.form1.resizeEvent = self.onResize
		self.actionAcerda_de.triggered.connect(partial(about,self.form1,'GenRep',QtGui.QApplication.translate("MainWindow", 'Report Generator', None, QtGui.QApplication.UnicodeUTF8),QtGui.QApplication.translate("MainWindow", 'Description', None, QtGui.QApplication.UnicodeUTF8),'1.0.0',"pixmaps/genrep.png"))
		
		self.treeWidget_2.itemClicked.connect(self.change_graphic)
		
		self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"Ready"),2000)
		self.form1.setCursor(QtCore.Qt.ArrowCursor)
		self.treeWidget.customContextMenuRequested.connect(self.popup)
				
		self.selected_row=[False,False]

	def create_graphic(self,X,Y):
		self.pan=False
		self.zoom=False
		self.canvas = Lienzo(X,Y,self.verticalLayoutWidget)		
		self.canvas.mousePressEvent=SpanSelector(
								self.canvas.allGraphic,
								self.canvas.onselect,
								'horizontal',
								useblit=True,
								rectprops=dict(alpha=0.5, facecolor='#c0c0c0') 
								)
								
		def onClick(event):
			if event.button==1 and (not self.pan) and (not self.zoom):
				try:
					if event.inaxes.get_title()=='Signal' and not self.canvas.activeBackground:						
						if not self.canvas.activeSignal:
							self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"Signal area is selected"),3000)
							event.inaxes.patch.set_facecolor('#6C9DEC')
							event.canvas.draw()
							self.canvas.activeSignal=True
						else:
							event.inaxes.patch.set_facecolor('#ffffff')
							event.canvas.draw()
							self.canvas.activeSignal=False
					elif event.inaxes.get_title()=='Background' and not self.canvas.activeSignal:
						if not self.canvas.activeBackground:
							self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"Background area is selected"),3000)
							event.inaxes.patch.set_facecolor('#6C9DEC')
							event.canvas.draw()
							self.canvas.activeBackground=True
						else:
							event.inaxes.patch.set_facecolor('#ffffff')
							event.canvas.draw()
							self.canvas.activeBackground=False					
				except:
					pass
				
		self.canvas.mpl_connect('button_press_event', onClick)		
		
		def enter_axes(event):
			if event.inaxes.get_title()=='Signal' or event.inaxes.get_title()=='Background' :
				self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"Slect area to change"))
				self.form1.setCursor(QtCore.Qt.PointingHandCursor)
				
		def leave_axes(event):
			if event.inaxes.get_title()=='Signal' or event.inaxes.get_title()=='Background' :
				self.form1.statusBar().showMessage(' ')
				self.form1.setCursor(QtCore.Qt.ArrowCursor)
				
		self.canvas.mpl_connect('axes_enter_event', enter_axes)
		self.canvas.mpl_connect('axes_leave_event', leave_axes)
		
		ToolBarr = NavigationToolbar(self.canvas, self.verticalLayoutWidget)
		self.verticalLayoutWidget.setStyleSheet(TOOLBUTTON_STYLE)
		
		def pan_change(event):
			if self.pan:
				self.pan=False
			else:
				self.pan=True
				self.zoom=False
				
		def zoom_change(event):
			if self.zoom:
				self.zoom=False
			else:
				self.zoom=True
				self.pan=False
				
		def home_press(event):
			self.canvas.activeSignal=True
			self.canvas.activeBackground=False
			try:
				self.canvas.onselect(min(self.canvas.Signal_X),max(self.canvas.Signal_X))
			except:
				self.canvas.onselect(self.canvas.Signal_X,self.canvas.Signal_X)
			self.canvas.activeBackground=True
			try:
				self.canvas.onselect(min(self.canvas.Background_X),max(self.canvas.Background_X))
			except:
				self.canvas.onselect(self.canvas.Background_X,self.canvas.Background_X)
			
		for act in ToolBarr.actions():
			toolTip=str(act.toolTip())
			if toolTip=='Configure subplots' or toolTip=='Edit curves line and axes parameters':
				ToolBarr.removeAction(act)
			elif toolTip=='Reset original view':
				act.triggered.connect(home_press)
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Home'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Reset Original View'))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				act.setIcon(icon)				
			elif toolTip=='Back to previous view' or toolTip=='Back to  previous view':
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Back'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Back to previous view'))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				act.setIcon(icon)
			elif toolTip=='Forward to next view':
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Forward'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Forward to next view'))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				act.setIcon(icon)
			elif toolTip=='Pan axes with left mouse, zoom with right':
				act.triggered.connect(pan_change)
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Drag'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Drag with left mouse, zoom with right'))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/transform.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				#act.setIcon(icon)
			elif toolTip=='Zoom to rectangle':
				act.triggered.connect(zoom_change)
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Zoom'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Zoom the rectangle'))
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				act.setIcon(icon)
			elif toolTip=='Save the figure':
				act.setToolTip(QtGui.QApplication.translate("MainWindow", 'Save'))
				act.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Save the figure as image'))		
				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap("pixmaps/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				act.setIcon(icon)
		self.canvas.fig.set_facecolor('#f0f0f0')
		ToolBarr.setStyleSheet('background:#f0f0f0;')
		
		xmin1_label=QtGui.QLabel('start')		
		xmin1_label.setStyleSheet('color:green')
		xmin1_sb = QtGui.QDoubleSpinBox()
		xmin1_sb.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Start channel to signal'))
		xmin1_sb.setMinimum(min(X))
		xmin1_sb.setMaximum(max(X))	
		
		xmax1_label=QtGui.QLabel('end')
		xmax1_label.setStyleSheet('color:green')
		xmax1_sb = QtGui.QDoubleSpinBox()
		xmax1_sb.setStatusTip(QtGui.QApplication.translate("MainWindow", 'End channel to signal'))
		xmax1_sb.setMinimum(min(X))
		xmax1_sb.setMaximum(max(X))
		
		xmin2_label=QtGui.QLabel('start')
		xmin2_label.setStyleSheet('color:#1A297D')
		xmin2_sb = QtGui.QDoubleSpinBox()
		xmin2_sb.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Start channel to Background'))
		xmin2_sb.setMinimum(min(X))
		xmin2_sb.setMaximum(max(X))
		
		xmax2_label=QtGui.QLabel('end')
		xmax2_label.setStyleSheet('color:#1A297D')
		xmax2_sb = QtGui.QDoubleSpinBox()
		xmax2_sb.setStatusTip(QtGui.QApplication.translate("MainWindow", 'End channel to Background'))
		xmax2_sb.setMinimum(min(X))
		xmax2_sb.setMaximum(max(X))
		
		self.verticalLayout.addWidget(xmin1_label,1,0,1,1)
		self.verticalLayout.addWidget(xmin1_sb,2,0,1,1)
		self.verticalLayout.addWidget(xmax1_label,3,0,1,1)
		self.verticalLayout.addWidget(xmax1_sb,4,0,1,1)
		self.verticalLayout.addWidget(xmin2_label,1,14,1,1)
		self.verticalLayout.addWidget(xmin2_sb,2,14,1,1)
		self.verticalLayout.addWidget(xmax2_label,3,14,1,1)
		self.verticalLayout.addWidget(xmax2_sb,4,14,1,1)
		
		self.verticalLayout.addWidget(self.canvas,0,0,10,15)
		self.verticalLayout.addWidget(ToolBarr,11,0,2,15)
		
		def fill_x_1(x1,x2):
			xmin1_sb.setValue(x1)
			xmax1_sb.setValue(x2)			
			
		
		def fill_x_2(x1,x2):
			xmin2_sb.setValue(x1)
			xmax2_sb.setValue(x2)			
		
		def x1_sb_change(buttom):
			self.canvas.activeSignal=True
			if xmax1_sb.value() >=xmin1_sb.value():
				self.canvas.onselect(xmin1_sb.value(),xmax1_sb.value())

			
		def x2_sb_change(buttom):
			self.canvas.activeBackground=True
			if xmax2_sb.value() >=xmin2_sb.value():
				self.canvas.onselect(xmin2_sb.value(),xmax2_sb.value())

			
		xmin1_sb.valueChanged.connect(partial(x1_sb_change,1))
		xmax1_sb.valueChanged.connect(partial(x1_sb_change,2))
		xmin2_sb.valueChanged.connect(partial(x2_sb_change,1))
		xmax2_sb.valueChanged.connect(partial(x2_sb_change,2))	
		self.canvas.signal_change.connect(fill_x_1)
		self.canvas.background_change.connect(fill_x_2)
	

	#****************************************************************************************
	def fillActions(self):
		#Para la grafica
		self.verticalLayoutWidget = QtGui.QWidget()
		self.verticalLayout = QtGui.QGridLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(5, 0, 0, 0)
		
		#isquierda de la grafica
		self.treeWidget_2 = QtGui.QTreeWidget()
		self.treeWidget_2.setIndentation(0)
		font = QtGui.QFont()
		font.setFamily("Novason")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(53)
		self.treeWidget_2.setFont(font)
		self.treeWidget_2.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.treeWidget_2.setFrameShape(QtGui.QFrame.StyledPanel)
		self.treeWidget_2.setFrameShadow(QtGui.QFrame.Sunken)
		self.treeWidget_2.setMidLineWidth(0)
		self.treeWidget_2.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked|QtGui.QAbstractItemView.EditKeyPressed)
		self.treeWidget_2.setTabKeyNavigation(True)
		self.treeWidget_2.setStyleSheet(TREEW2_STYLE)
		self.treeWidget_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		self.treeWidget_2.setUniformRowHeights(True)
		self.treeWidget_2.setHeaderHidden(False)
		self.treeWidget_2.setExpandsOnDoubleClick(False)
		self.treeWidget_2.headerItem().setText(0, QtGui.QApplication.translate('MainWindow',"Columns with data"))
		self.treeWidget_2.header().setDefaultSectionSize(117)
		
		self.mainWidget=QtGui.QWidget()
		self.form1.setCentralWidget(self.mainWidget)
		
		#Panel de abajo
		self.down_area= QtGui.QWidget()
		self.down_area_layout=QtGui.QGridLayout(self.down_area)
		self.active_bar=QtGui.QLabel()
		self.active_bar.mouseDoubleClickEvent=self.chow_hidden_down_area
		self.active_bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.active_bar.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Show/Hidde graphic'))
		self.active_bar.setStyleSheet('background:qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #d3d3d3, stop: 0.1 #d3d3d3,stop: 0.49 #ffffff, stop: 0.5 #ffffff, stop: 0.9 #f0f0f0,stop: 1 #f0f0f0)')
		self.down_area_layout.setContentsMargins(0, 0, 0, 0)
		self.down_area_layout.addWidget(self.active_bar,0,0,1,3)
		self.down_area_layout.addWidget(self.verticalLayoutWidget,1,0,10,2)
		self.down_area_layout.addWidget(self.treeWidget_2,1,2,10,1)
		
		self.layout=QtGui.QGridLayout(self.mainWidget)
		self.layout.setRowMinimumHeight(1,210)		
		#self.layout.setColumnMinimumWidth(3,100)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.addWidget(self.treeWidget, 1, 0, 1, 3)
		self.layout.addWidget(self.down_area,2,0,1,3)
		self.layout.setRowMinimumHeight(2,360)	
		self.layout.setColumnMinimumWidth(0,385)
		self.layout.setColumnMinimumWidth(1,385)
		
		self.m_anim = Animation(self.down_area, 'pos')
		self.m_anim.setEasingCurve(QtCore.QEasingCurve.Linear)
		self.m_anim.setDuration(700)
		self.m_anim.setLoopCount(1)
		self.m_anim.finished.connect(self.detenido)
		
		self.down_area_visible=True
		
		self.fill_aux()
		
	def fill_aux(self):
		self.actionEjecutar_GenRep.setVisible(False)
		
		self.actionNuevo.setVisible(False)
		self.actionPegar.setVisible(False)
		#self.actionCopiar.setVisible(False)
		self.actionCortar.setVisible(False)
		
		#Seleccionar Fila-----------------------------------------------------------------
		self.actionSeleccionar_Fila = QtGui.QAction(self.form1)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("pixmaps/icons/select_row.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSeleccionar_Fila.setIconVisibleInMenu(True)
		self.actionSeleccionar_Fila.setIcon(icon)
		self.actionSeleccionar_Fila.setShortcut("Alt+S")
		self.actionSeleccionar_Fila.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select one row of the table", None, QtGui.QApplication.UnicodeUTF8))
		self.menuEditar.addAction(self.actionSeleccionar_Fila)
		self.actionSeleccionar_Fila.setText(QtGui.QApplication.translate("MainWindow", "&Select Row", None, QtGui.QApplication.UnicodeUTF8))
		self.menuEditar.addSeparator()
		
	def onResize(self,event):
		if not self.down_area_visible:
			self.m_anim.setStartValue(QtCore.QPointF(0,self.mainWidget.height()))
			self.m_anim.setEndValue(QtCore.QPointF(0, self.mainWidget.height()-20))
			self.m_anim.start()
			
	def detenido(self):
		if self.down_area_visible:
			self.layout.addWidget(self.treeWidget, 1, 0,1, -1)
			self.layout.setContentsMargins(0, 0, 0, 0)
			self.verticalLayoutWidget.setEnabled(True)
	
	def chow_hidden_down_area(self,event):
		self.verticalLayoutWidget.setEnabled(False)
		if self.down_area_visible:
			self.layout.addWidget(self.treeWidget, 1, 0,4, -1)
			self.layout.setContentsMargins(0, 0, 0, 20)
			self.m_anim.setStartValue(QtCore.QPointF(0,self.mainWidget.height()-self.down_area.height()))
			self.m_anim.setEndValue(QtCore.QPointF(0, self.mainWidget.height()-20))
			self.down_area_visible=False
		else:
			self.m_anim.setEndValue(QtCore.QPointF(0, self.mainWidget.height()-self.down_area.height()))
			self.m_anim.setStartValue(QtCore.QPointF(0, self.mainWidget.height()-20))
			self.down_area_visible=True			
		self.m_anim.start()

		
	def popup(self,pos):
		menu = QtGui.QMenu()
		menu.addAction(self.actionCopiar)
		action = menu.exec_(self.treeWidget.mapToGlobal(pos))
		
	@cursorAction()
	def save(self,temp=False):
		"""Guarda la informacion en forma de xml"""
		self.closeAllDialogs()
		if self.directorioArchivo=='':
			return self.saveAs()
		else:
			#guardarlo en la dir self.directorioArchivo
			pass
	
	
	@cursorAction()
	def saveAs(self,dir=False):
		"""Ventana para guardar un documanto"""
		self.closeAllDialogs()
		dialog=QtGui.QFileDialog(self.form1)
		if not dir:
			self.directorioArchivo=dialog.getSaveFileName(
				self.form1,
				QtGui.QApplication.translate('MainWindow',"Save"),
				self.fileLocation,
				QtGui.QApplication.translate('MainWindow','File')+' XLS (*.xls);; '+QtGui.QApplication.translate('MainWindow','File')+'RLS (*.rls);; '+QtGui.QApplication.translate('MainWindow','File')+'PDF (*.pdf)',
			)
		else:
			self.directorioArchivo=dir
		if self.directorioArchivo:
			if not (self.directorioArchivo.endswith('.xls') or self.directorioArchivo.endswith('.xml') or self.directorioArchivo.endswith('.pdf')):
				self.directorioArchivo+='.xls'
			return True
		else:
			self.directorioArchivo=''
		return False


	def onCloseEvent(self,event):
		self.closeAllDialogs()
		self.config.save(self.fuente,self.size,self.fileLocation,self.opacity,self.lang)
		event.accept()
	
	
	def copy(self):
		"""Copia el texto de la casilla seleccionada en el clipboard"""
		self.form1.statusBar().showMessage("")
		if self.treeWidget.selectedIndexes():
			text=''
			item=self.treeWidget.selectedIndexes()[0]
			text+=self.treeWidget.topLevelItem(item.row()).text(item.column())
			for item in self.treeWidget.selectedIndexes()[1:]:
				aux=self.treeWidget.topLevelItem(item.row()).text(item.column())
				if aux:
					text+=', '+aux
			clipboard=QtGui.QApplication.clipboard()
			clipboard.setText(text)

	
	def imprimir(self):
		"""Imprime toda la informacion de la aplicacion"""
		printer =QtGui.QPrinter(QtGui.QPrinter.HighResolution)
		if os.sys.platform=='linux' or os.sys.platform=='linux2':
			printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
			printer.setOutputFileName(str(self.fileLocation)+'/gensec.pdf')
		dialog = QtGui.QPrintDialog(printer,self.form1)
		dialog.addEnabledOption(QtGui.QAbstractPrintDialog.PrintSelection)
		dialog.setWindowTitle('Print Table')
		
		if dialog.exec_() == QtGui.QDialog.Accepted:
			document=QtGui.QTextDocument()
			document.setHtml(QtCore.QString.fromUtf8(self.buildHtml()))
			document.print_(printer)
			self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"The document has been printed"))
		dialog.show()	
			
			
	def buildHtml(self):			
		"""Construye una tabla html con estructura igual a la del gensec, con la informacion de esta"""
		hora='<table><tr><td> GenRep : '+str(datetime.datetime.fromtimestamp(time.time()))+'</td></tr></td></tr><tr><td> </td></tr></table>'
		html=''
		cant_filas=0
		for i in range(self.treeWidget.topLevelItemCount()):
			item = self.treeWidget.topLevelItem( i )
			cant_filas+=1
			colum=0
			html+='<tr>'
			for column in range(self.treeWidget.columnCount()):
				if not self.treeWidget.isColumnHidden(column):
					color= item.textColor(column).name()
					font= self.treeWidget.font().family()
					size= str(self.treeWidget.font().pointSize())
					dato=item.text(column)
					html+='<td style="font-family:'+font+'; font-size:'+size+'; color:'+color+';">     '+dato+'     </td>'
			html+='</tr>'
		html+="</table></body></html>"
		
		header='<table border="2"><tr>'
		for column in range(self.treeWidget.columnCount()):
			if not self.treeWidget.isColumnHidden(column):
				columna=self.header.model().headerData(column,QtCore.Qt.Horizontal).toString()
				header+='<td>     '+str(columna)+'     </td>'			
		header+='</tr>'
		
		html=hora+header+html
		return html
		
	
	def addGroup(self):
		"""Adiciona una fila para otra muestra"""
		self.closeAllDialogs()
		self.form1.statusBar().showMessage("")
		item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
		item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
		self.toolButtonHeader = QtGui.QToolButton()
		self.toolButtonHeader.setText(QtGui.QApplication.translate("MainWindow", str(self.grupos+1), None, QtGui.QApplication.UnicodeUTF8))
		font = QtGui.QFont()
		font.setFamily(("Novason"))
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(53)
		font.setStrikeOut(False)
		font.setKerning(False)
		font.setStyleStrategy(QtGui.QFont.PreferDefault)
		self.toolButtonHeader.setFont(font)
		self.toolButtonHeader.setObjectName(("toolButton"))
		self.toolButtonHeader.setStyleSheet(HEADER_TOOLBUTTON_STYLE)
		self.treeWidget.setItemWidget(item_0, 0,self.toolButtonHeader)
		self.toolButtonHeader.clicked.connect(partial(self.selectRow,True,self.grupos+1))
		vs=self.treeWidget.verticalScrollBar()
		vs.setValue(vs.maximum())
		self.grupos+=1
		
	
	def addComand(self):
			"""Adiciona una columna para comandos"""
			self.closeAllDialogs()
			self.treeWidget.headerItem().setText(self.comandos+1, (QtGui.QApplication.translate('MainWindow',"Command ")+str(self.comandos)))
			hs=self.treeWidget.horizontalScrollBar()
			hs.setValue(hs.maximum())			
			self.comandos+=1
			
			
	def change(self):
			"""Cambia el tipo de letra y el tamanno de los elementos de la tabla"""
			self.fuente=self.fontS.fontComboBox.currentFont().toString().split(',')[0]
			self.size=self.fontS.spinBox.value()
			self.fontS.form1.close()
			font = QtGui.QFont()
			font.setFamily(self.fuente)
			font.setPointSize(self.size)
			font.setBold(False)
			font.setItalic(False)
			font.setUnderline(False)
			font.setWeight(53)
			font.setStrikeOut(False)
			font.setKerning(False)
			font.setStyleStrategy(QtGui.QFont.PreferDefault)
			self.treeWidget.setFont(font)
			self.form1.statusBar().showMessage(QtGui.QApplication.translate('MainWindow',"The font has been changed"))
			
	
	def setValue(self,row,column,valor):
		"""Introduce un valor en determinado campo, column, tiene que ser mayor que 0"""
		item=self.treeWidget.topLevelItem( row )
		if not item.text(column):
			item.setTextColor(column,QtGui.QColor('#000000'))
		item.setText(column,valor)
			
	
	def selectRow(self, ok=False, row=False):
			"""Selecciona un conjunto de filas, recibe por parametro un estrin de la forma: row,row,row...."""					
			if not ok:
				row, ok = QtGui.QInputDialog.getInteger(self.form1, QtGui.QApplication.translate('MainWindow','Row Number'), QtGui.QApplication.translate('MainWindow','Row')+':',0,1)			
			if ok:				
				for i in self.treeWidget.selectedIndexes():
					item = self.treeWidget.topLevelItem(i.row())
					item.setSelected(False)				
				row=int(row)-1
				try:
					item = self.treeWidget.topLevelItem(row)
					item.setSelected(True)
					if self.selected_row[1]:
						self.selected_row[1].setStyleSheet(HEADER_TOOLBUTTON_STYLE)
					self.selected_row[1]=self.treeWidget.itemWidget(item,0)
					self.selected_row[1].setStyleSheet(HEADER_TOOLBUTTON_STYLE2)
					self.selected_row[0]=row
					self.clear_lateral_panel()
					self.fill_lateral_panel()
				except:
					pass
					
					
	def clear_lateral_panel(self):
		for i in range(self.treeWidget_2.topLevelItemCount()):
			item = self.treeWidget_2.topLevelItem(i)
			dato=item.text(0)
			if dato!='':
				item.setHidden(True)
	
	
	def fill_lateral_panel(self):
		item = self.treeWidget.topLevelItem(self.selected_row[0])
		for column in range(self.comandos+1)[2:]:
			dato=item.text(column)
			if dato!='':
				info=self.processData[str(self.selected_row[0])+','+str(column)]
				if info['id'] > 1 and info['id'] < 7:
					if info['Curva1'] !='' or info['Curva3'] !='' or info['Curva3'] !='':
						header=self.header.model().headerData(column,QtCore.Qt.Horizontal).toString()
						
						item_2 = QtGui.QTreeWidgetItem(self.treeWidget_2)
						item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
						item_2.setText(0,header)
						self.treeWidget_2.setItemWidget(item_2, 0,QtGui.QWidget())
						
						
	def change_graphic(self,item):
		headerName= str(item.text(0))
		item = self.treeWidget.topLevelItem(self.selected_row[0])
		if item.isSelected():
			for column in range(self.comandos+1)[2:]:
				if self.header.model().headerData(column,QtCore.Qt.Horizontal).toString()==headerName:
					print column
					X=[1,5,10,15]
					Y=[1000,200,100,66.4]
					self.create_graphic(X,Y)

   
class Animation(QtCore.QPropertyAnimation):
    LinearPath, CirclePath = range(2)

    def __init__(self, target, prop):
        super(Animation, self).__init__(target, prop)

        self.setPathType(Animation.LinearPath)

    def setPathType(self, pathType):
        self.m_pathType = pathType
        self.m_path = QtGui.QPainterPath()

    def updateCurrentTime(self, currentTime):
        if self.m_pathType == Animation.CirclePath:
            if self.m_path.isEmpty():
                end = self.endValue()
                start = self.startValue()
                self.m_path.moveTo(start)
                self.m_path.addEllipse(QtCore.QRectF(start, end))

            dura = self.duration()
            if dura == 0:
                progress = 1.0
            else:
                progress = (((currentTime - 1) % dura) + 1) / float(dura)

            easedProgress = self.easingCurve().valueForProgress(progress)
            if easedProgress > 1.0:
                easedProgress -= 1.0
            elif easedProgress < 0:
                easedProgress += 1.0

            pt = self.m_path.pointAtPercent(easedProgress)
            self.updateCurrentValue(pt)
            self.valueChanged.emit(pt)
        else:
            super(Animation, self).updateCurrentTime(currentTime)